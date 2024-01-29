from datetime import datetime
import pandas as pd

class FileReader:
    def __init__(self, prefix):
        self.prefix = prefix
    def read_files(self):
        """
        Reads files based on the specified prefix.
        Example: cast | crew | movie_cast | movie_crew | movies
        """
        if self.prefix == 'genres':
            file_name = f'../../test/{self.prefix}.txt'
            response = pd.read_json(file_name,orient='records', lines=True)
            return response
        else:
            now = datetime.now()
            file_name = now.strftime("%Y-%m-%d-%H")
            # file_name = f'../../test/{self.prefix}_{file_name}.txt'
            file_name = f'/mnt/c/users/youcode/desktop/batch-processing-movies-leans-data/test/{self.prefix}_{file_name}.txt'
            response = pd.read_json(file_name, lines=True)
            return response