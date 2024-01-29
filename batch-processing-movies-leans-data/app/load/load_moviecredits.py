import readFiles as Reader
from inserter import Inserter


file_reader = Reader.FileReader(prefix='movie_cast')
movie_cast = file_reader.read_files()

inserter = Inserter()

movie_cast['character'].replace({"":"Unknown"},inplace=True)
movie_cast = movie_cast.drop_duplicates(['cast_id' , 'movie_id','character','order'])
inserter.insert_or_update_movie_credits(table_name='MovieCredits', data_frame=movie_cast)

# # Dispose of the engine
# inserter.dispose_engine() 