import readFiles as Reader
from inserter import Inserter
import pandas as pd
import numpy as np



file_reader = Reader.FileReader(prefix='movies')
df_movies = file_reader.read_files()

inserter = Inserter()


production_companies = []
for production_companies_i in df_movies['production_companies'].interpolate():
    for production_companie_j in production_companies_i:
        production_companies.append(production_companie_j)
df_production_companies = pd.DataFrame(production_companies)
df_production_companies['id'] = df_production_companies['id'].astype(int)

df_unique_production_companies = df_production_companies.drop_duplicates(['id', 'logo_path','name','origin_country'])
df_unique_production_companies.loc[df_unique_production_companies['logo_path'].notnull(), 'logo_path'] = 'https://image.tmdb.org/t/p/w500/' + df_unique_production_companies['logo_path']
df_unique_production_companies['logo_path'].fillna('Not Found',inplace=True)
df_unique_production_companies['origin_country'].replace({'':'Not Exist'},inplace=True)



# Insert data into the 'ProductionsCompanies' table

inserter.insert_data(table_name='ProductionsCompanies', data_frame=df_unique_production_companies)

# inserter.dispose_engine()