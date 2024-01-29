import readFiles as Reader
from inserter import Inserter
import pandas as pd

inserter = Inserter()

file_reader = Reader.FileReader(prefix='movies')
df_movies = file_reader.read_files()

movies_genres = []
for x in df_movies.itertuples():
    movie_id = x.id
    for genre in x.genres:
        movies_genres.append(
            {
                'movie_id' : movie_id,
                'genre_id' : genre['id']
            }
        )
df_movies_genres = pd.DataFrame(movies_genres)
json_movie_genres = df_movies_genres.drop_duplicates(['movie_id' , 'genre_id'])


inserter.insert_or_update_bridge_data(table_name='MovieGenres', data_frame=json_movie_genres)

# # Dispose of the engine
# inserter.dispose_engine()