import readFiles as Reader
import pandas as pd
from datetime import datetime
from inserter import Inserter



file_reader = Reader.FileReader(prefix='movies')
df_movies = file_reader.read_files()

inserter = Inserter()

df_movies = df_movies[['id','budget','popularity','revenue','runtime','vote_average','vote_count']]
df_movies.fillna(0,inplace=True)
# df_movies['Effective_Date'] = pd.to_datetime(datetime.now()).strftime('%Y-%m-%d %H:%M:%S')

# Insert data into the 'FactMovies' table

inserter.insert_data(table_name='FactProductions', data_frame=df_movies)

# inserter.dispose_engine()