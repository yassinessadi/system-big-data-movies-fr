import readFiles as Reader
from inserter import Inserter
import pandas as pd
from datetime import datetime



inserter = Inserter()

pd.options.mode.copy_on_write = True


file_reader = Reader.FileReader(prefix='cast')
cast = file_reader.read_files()

# cast.rename(columns={"id":"cast_id"},inplace=True)

df_Person = cast[['id','cast_id','name','gender','popularity','profile_path',"known_for_department"]]

df_Person.loc[:, 'id'] = df_Person['id'].astype(int)
df_Person.loc[:, 'cast_id'] = df_Person['cast_id'].astype(int)
df_Person.loc[:, 'gender'] = df_Person['gender'].replace({0: "Not set / not specified", 1: "Female", 2: "Male", 3: "Not set / not specified"})

df_Person.loc[df_Person['profile_path'].notnull(), 'profile_path'] = 'https://image.tmdb.org/t/p/w500/' + df_Person['profile_path']
df_Person.loc[:, 'profile_path'].fillna('Not Found', inplace=True)
# df_Person['Effective_Date'] = pd.to_datetime(datetime.now()).strftime('%Y-%m-%d %H:%M:%S')





inserter.insert_data(table_name='Actors', data_frame=df_Person)


# inserter.dispose_engine()