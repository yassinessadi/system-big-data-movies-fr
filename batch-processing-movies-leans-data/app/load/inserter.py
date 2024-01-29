# from sqlalchemy import create_engine
# import createTables
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import inspect
# from sqlalchemy.exc import IntegrityError
import pyodbc as Context

class Inserter:
    """
    """
    def __init__(self):
        # self.engine = create_engine("mssql+pyodbc://jane_essadi:123123@172.16.9.85/TheMoviesDB?driver=ODBC+Driver+17+for+SQL+Server", echo=True)
        # self.Session = sessionmaker(bind=self.engine)

        self.server = '192.168.1.2' 
        self.database = 'TheMoviesDB' 
        self.username = 'jane_essadi' 
        self.password = '123123' 
        self.context = Context.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER='+
                                       self.server+';DATABASE='+
                                       self.database+';UID='+
                                       self.username+';PWD='+ 
                                       self.password,autocommit=True)
        self.cursor = self.context.cursor()
        
    # def check_table(self, table_name):
    #     # Check if the table exists using inspect(engine)
    #     insp = inspect(self.engine)
    #     if insp.has_table(table_name):
    #         return True
    #     else:
    #         return False
        
    # def create_table(self):
    #     # Create the table in the database
    #     createTables.Base.metadata.create_all(bind=self.engine,checkfirst=True)

    def insert_data(self, table_name, data_frame):
        try:
            for row in data_frame.itertuples(index=False):
                # Check if the row with the given primary key already exists
                self.cursor.execute(
                    f'''
                        SELECT id FROM {table_name}
                        WHERE id = ?
                    ''',
                    row.id
                )
                existing_row = self.cursor.fetchone()
                
                if existing_row:
                    # If the row exists, update its values
                    update_columns = ', '.join([f'{col} = ?' for col in data_frame.columns if col != 'id'])
                    update_query = f'''
                        UPDATE {table_name}
                        SET {update_columns}
                        WHERE id = ?
                    '''
                    update_values = tuple(getattr(row, col) for col in data_frame.columns if col != 'id')
                    self.cursor.execute(update_query, update_values + (row.id,))
                else:
                    # If the row doesn't exist, insert a new row
                    insert_columns = ', '.join(data_frame.columns)
                    insert_values = ', '.join(['?' for _ in range(len(data_frame.columns))])
                    insert_query = f'''
                        INSERT INTO {table_name} ({insert_columns})
                        VALUES ({insert_values})
                    '''
                    self.cursor.execute(insert_query, [getattr(row, col) for col in data_frame.columns])

            self.cursor.close()
        except Exception as e:
            # Handle exceptions here
            print(f"Error: {e}")
    # def insert_data(self, table_name, data_frame):
    #     try:
    #         # data_frame.to_sql(name=table_name, con=self.engine, index=False, if_exists='append')
    #     except IntegrityError as e:
    #         print(f"IntegrityError: {e}")
            
    def insert_or_update_bridge_data(self, table_name, data_frame):
        try:
            for row in data_frame.itertuples(index=False):
                # Construct the WHERE clause based on the primary key columns
                where_clause = ' AND '.join([f'{col} = ?' for col in data_frame.columns])

                # Check if the row with the given primary key already exists
                self.cursor.execute(
                    f'SELECT * FROM {table_name} WHERE {where_clause}',
                    *(getattr(row, col) for col in data_frame.columns)
                )
                existing_row = self.cursor.fetchone()

                if existing_row:
                    # If the row exists, update its values
                    update_columns = ', '.join([f'{col} = ?' for col in data_frame.columns])
                    update_query = f'UPDATE {table_name} SET {update_columns} WHERE {where_clause}'
                    update_values = tuple(getattr(row, col) for col in data_frame.columns) + \
                                    tuple(getattr(existing_row, col) for col in data_frame.columns)
                    self.cursor.execute(update_query, update_values)
                else:
                    # If the row doesn't exist, insert a new row
                    insert_columns = ', '.join(data_frame.columns)
                    insert_values = ', '.join(['?' for _ in range(len(data_frame.columns))])
                    insert_query = f'INSERT INTO {table_name} ({insert_columns}) VALUES ({insert_values})'
                    self.cursor.execute(insert_query, [getattr(row, col) for col in data_frame.columns])


            self.cursor.close()
        except Exception as e:
            # Handle exceptions here
            print(f"Error: {e}")


    def insert_or_update_movie_credits(self, table_name, data_frame):
        try:
            for row in data_frame.itertuples():
                self.cursor.execute(
                    f"""
                    MERGE INTO {table_name} AS target
                    USING (VALUES (?, ?, ?, ?, ?)) AS source(cast_id, movie_id, character, credit_id, [order])
                    ON target.cast_id = source.cast_id AND target.movie_id = source.movie_id
                    WHEN MATCHED THEN
                        UPDATE SET target.character = source.character, target.credit_id = source.credit_id, target.[order] = source.[order]
                    WHEN NOT MATCHED THEN
                        INSERT (cast_id, movie_id, character, credit_id, [order])
                        VALUES (source.cast_id, source.movie_id, source.character, source.credit_id, source.[order]);
                """,
                row.cast_id, 
                row.movie_id, 
                row.character, 
                row.credit_id, 
                row.order
                )
                print(row.order)

            self.cursor.close()
        except Exception as e:
            # Handle exceptions here
            print(f"Error: {e}")


            
    # def dispose_engine(self):
    #     # Dispose of the engine
    #     self.engine.dispose()