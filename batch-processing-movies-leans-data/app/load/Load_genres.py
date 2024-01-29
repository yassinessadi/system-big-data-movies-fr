import readFiles as Reader
from inserter import Inserter



file_reader = Reader.FileReader(prefix='genres')
df_genres = file_reader.read_files()


inserter = Inserter()

df_genres = df_genres[['id','name']].drop_duplicates(['id' , 'name'])


# Insert data into the 'Genres' table

inserter.insert_data(table_name='Genres', data_frame=df_genres)
# inserter.dispose_engine()
