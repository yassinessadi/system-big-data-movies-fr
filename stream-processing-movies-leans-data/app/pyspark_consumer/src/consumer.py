import findspark
findspark.init()
from pyspark.sql import functions as F , SparkSession
from pyspark.sql.types import StructType, StructField, StringType,BooleanType, IntegerType, ArrayType,FloatType,LongType
from elasticsearch import Elasticsearch

spark = SparkSession.builder \
    .appName("application-moviesdb") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,"
            "org.elasticsearch:elasticsearch-spark-30_2.12:8.11.0") \
    .getOrCreate()


movie_schema = StructType([
    StructField("adult", BooleanType(), True),
    StructField("backdrop_path", StringType(), True),
    StructField("belongs_to_collection", StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("poster_path", StringType(), True),
        StructField("backdrop_path", StringType(), True),
    ]), True),
    StructField("budget", IntegerType(), True),
    StructField("genres", ArrayType(StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
    ])), True),
    StructField("homepage", StringType(), True),
    StructField("id", IntegerType(), True),
    StructField("imdb_id", StringType(), True),
    StructField("original_language", StringType(), True),
    StructField("original_title", StringType(), True),
    StructField("overview", StringType(), True),
    StructField("popularity", FloatType(), True),
    StructField("poster_path", StringType(), True),
    StructField("production_companies", ArrayType(StructType([
        StructField("id", IntegerType(), True),
        StructField("logo_path", StringType(), True),
        StructField("name", StringType(), True),
        StructField("origin_country", StringType(), True),
    ])), True),
    StructField("production_countries", ArrayType(StructType([
        StructField("iso_3166_1", StringType(), True),
        StructField("name", StringType(), True),
    ])), True),
    StructField("release_date", StringType(), True),
    StructField("revenue", IntegerType(), True),
    StructField("runtime", IntegerType(), True),
    StructField("spoken_languages", ArrayType(StructType([
        StructField("english_name", StringType(), True),
        StructField("iso_639_1", StringType(), True),
        StructField("name", StringType(), True),
    ])), True),
    StructField("status", StringType(), True),
    StructField("tagline", StringType(), True),
    StructField("title", StringType(), True),
    StructField("video", BooleanType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("vote_count", IntegerType(), True),
])


df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "latestmoviesdata") \
  .option("startingOffsets", "earliest") \
  .load()


value_df = df.selectExpr("CAST(value AS STRING)")



exploded_df = value_df.withColumn("values", F.from_json(value_df["value"], movie_schema)).selectExpr("values as result")

selected_cols_df = exploded_df.select(
    F.col("result.adult").alias('adult'),
    F.col("result.backdrop_path").alias('backdrop_path'),
    F.col("result.budget").alias('budget'),
    F.col("result.genres.name").alias('genre'),
    F.col("result.homepage").alias('homepage'),
    F.col("result.id").alias('id'),
    F.col("result.imdb_id").alias('imdb_id'),
    F.col("result.original_language").alias('original_language'),
    F.col("result.original_title").alias('original_title'),
    F.col("result.overview").alias('overview'),
    F.col("result.popularity").alias('popularity'),
    F.col("result.poster_path").alias('poster_path'),
    F.col("result.release_date").alias('release_date'),

    F.col("result.production_companies.id").alias('production_companies_id'),
    F.col("result.production_companies.logo_path").alias('production_companies_logo_path'),
    F.col("result.production_companies.name").alias('production_companies_name'),
    F.col("result.production_companies.origin_country").alias('production_companies_origin_country'),

    F.col("result.revenue").alias('revenue'),
    F.col("result.production_countries.iso_3166_1").alias('production_countries_iso_3166_1'),
    F.col("result.production_countries.name").alias('production_countries_name'),
    F.col("result.spoken_languages.name").alias('spoken_languages_name'),
    F.col("result.spoken_languages.english_name").alias('spoken_languages_english_name'),
    F.col("result.spoken_languages.iso_639_1").alias('spoken_languages_iso_639_1'),
    F.col("result.status").alias('status'),
    F.col("result.tagline").alias('tagline'),
    F.col("result.title").alias('title'),
    F.col("result.vote_average").alias('vote_average'),
    F.col("result.vote_count").alias('vote_count'),
)

# List of string columns
string_columns = [col[0] for col in selected_cols_df.dtypes if col[1] == 'string']

# Replace null values with "not exist" only for string columns
selected_cols_df_filled = selected_cols_df.na.fill("not exist", subset=string_columns)


movies_mappings ={
  "mappings": {
    "properties": {
      "adult": { "type": "boolean" },
      "backdrop_path": { "type": "text" },
      "budget": { "type": "integer" },
      "genre": { "type": "keyword" },
      "homepage": { "type": "text" },
      "id": { "type": "integer" },
      "imdb_id": { "type": "keyword" },
      "original_language": { "type": "keyword" },
      "original_title": { "type": "text" },
      "overview": { "type": "text" },
      "popularity": { "type": "float" },
      "poster_path": { "type": "text" },
      "release_date": { "type": "date" },
      "production_companies_id": { "type": "integer" },
      "production_companies_logo_path": { "type": "text" },
      "production_companies_name": { "type": "text" },
      "production_companies_origin_country": { "type": "keyword" },
      "revenue": { "type": "integer" },
      "production_countries_iso_3166_1": { "type": "keyword" },
      "production_countries_name": { "type": "text" },
      "spoken_languages_name": { "type": "text" },
      "spoken_languages_english_name": { "type": "text" },
      "spoken_languages_iso_639_1": { "type": "keyword" },
      "status": { "type": "keyword" },
      "tagline": { "type": "text" },
      "title": { "type": "text" },
      "vote_average": { "type": "float" },
      "vote_count": { "type": "integer" }
    }
  }
}



# +---+--------+------+------+-------------------+------++-------------------+------+#
#                 connect to elasticsearch and insert into the target index          #
# +---+--------+------+------+-------------------+------++-------------------+------+#
def insert_data(index_name, df, checkpointlocation,_id):
    """
    `index_name` : Elastic search index \n
    `df` : Dataframe that you want to insert into elastic search \n
    `checkpointlocation` : To truncate the logical plan of this DataFrame \n
    `_id` : specefiy the documment id in elasticsearch
    """
    query = df.writeStream \
        .format("org.elasticsearch.spark.sql") \
        .outputMode("append") \
        .option("es.resource", f"{index_name}") \
        .option("es.nodes", "localhost") \
        .option("es.port", "9200") \
        .option("es.mapping.id", _id) \
        .option("es.nodes.wan.only", "false") \
        .option("checkpointLocation", checkpointlocation) \
        .option("es.write.operation", "index") \
        .start()
    return query

#+---+--------+------+------+-------------------+------+#
#                 insert into movie index               #
#+---+--------+------+------+-------------------+------+#
es = Elasticsearch([{'host': 'localhost', 'port':9200, 'scheme':'http'}])
es.options(ignore_status=400).indices.create(index="movies_detailsindex",mappings=movies_mappings)
query = insert_data("movies_detailsindex", selected_cols_df_filled, "./checkpointLocation/movies/","id")


query = selected_cols_df_filled.writeStream.outputMode("append").format("console").start()


query.awaitTermination()








# ----------------------------------------------------------#
# Boolean fields are mapped as "boolean".                   #
# Text fields are mapped as "text".                         #
# Integer fields are mapped as "integer".                   #
# Float fields are mapped as "float".                       #
# Date fields are mapped as "date".                         #
# Keyword fields are used for non-analyzed string fields.   #
# ----------------------------------------------------------#