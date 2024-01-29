import readFiles as Reader
from inserter import Inserter
import pandas as pd

inserter = Inserter()

file_reader = Reader.FileReader(prefix='movies')
df_movies = file_reader.read_files()


movies_production_companies = []
for x in df_movies.itertuples():
    movie_id = x.id
    for production_companie in x.production_companies:
        movies_production_companies.append(
            {
                'movie_id' : movie_id,
                'production_companies_id' : production_companie['id']
            }
        )

df_movies_production_companies= pd.DataFrame(movies_production_companies)
df_movies_production_companies = df_movies_production_companies.drop_duplicates(['movie_id' , 'production_companies_id'])



inserter.insert_or_update_bridge_data(table_name='Movies_ProductionCompanies', data_frame=df_movies_production_companies)

# # Dispose of the engine
# inserter.dispose_engine()