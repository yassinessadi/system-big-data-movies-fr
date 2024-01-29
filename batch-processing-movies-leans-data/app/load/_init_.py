import readFiles as Reader
# from inserter import Inserter

# inserter = Inserter()
# Create the table
# inserter.create_table()

file_reader = Reader.FileReader(prefix='cast')
file_reader = Reader.FileReader(prefix='movies')
file_reader = Reader.FileReader(prefix='movies_cast')

# inserter.dispose_engine()