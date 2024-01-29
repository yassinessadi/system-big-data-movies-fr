import readFiles as Reader
from inserter import Inserter
import pandas as pd
from datetime import datetime

file_reader = Reader.FileReader(prefix='movies')
df_movies = file_reader.read_files()


inserter = Inserter()
 

df_movies = df_movies[['id','title','overview','adult','homepage','original_language','original_title','imdb_id','poster_path','release_date','status','tagline','video']]
# df_movies.fillna(0,inplace=True)
df_movies.loc[df_movies['poster_path'].notnull(), 'poster_path'] = 'https://image.tmdb.org/t/p/w500/' + df_movies['poster_path']
df_movies['poster_path'].fillna('Not Found' ,inplace=True)
df_movies['poster_path'].fillna('Not Found' ,inplace=True)
df_movies['overview'].fillna('No Overview',inplace=True)
# --------------------------------------------------------------------------------//
#    if empty or With None Value will replace with 'No Link Or URL Provided'     //
# ------------------------------------------------------------------------------//
df_movies['homepage'].fillna('No Link or Url Provided',inplace=True)
df_movies['homepage'].replace({"":'No Link or Url Provided'},inplace=True)

# -------------------------------------------------------------------------------------------------------//
#  Tags are provided as keywords for the movie; if they do not exist, I'll replace them with 'No Tag'.  //
# -----------------------------------------------------------------------------------------------------//
df_movies['tagline'].fillna('No Tag',inplace=True)
df_movies['tagline'].replace({"":'No Tag'},inplace=True)
# df_movies['Effective_Date'] = pd.to_datetime(datetime.now()).strftime('%Y-%m-%d %H:%M:%S')

# Insert data into the 'MovieDetails' table
inserter.insert_data(table_name='MovieDetails', data_frame=df_movies)
# inserter.dispose_engine()