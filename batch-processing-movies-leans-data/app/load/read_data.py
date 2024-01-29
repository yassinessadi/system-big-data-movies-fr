import readFiles as Reader
from inserter import Inserter


file_reader = Reader.FileReader(prefix='movies')
df_movies = file_reader.read_files()

print(df_movies)
#
inserter = Inserter()

print(inserter.check_table("ProductionsCompanies"))
