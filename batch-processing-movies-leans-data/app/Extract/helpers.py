import os
from datetime import datetime


def readIndexOfRows(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as index_file:
            index = int(index_file.read().strip())
    else:
        index = 1
    return index

def writeIndexOfRows(file_path,index,page_after):
    with open(file_path, 'w') as index_file:
            index_file.write(str(index + page_after))

def writeDataToHDFS(prefix,content):
    """
    args:{
        `prefix` : name of the file will be added before the date.
        `content` : data will saved in the file
    }
    """
    # -------------------//
    # create file name  //
    # -----------------//
    now = datetime.now()
    file_name = now.strftime("%Y-%m-%d-%H")
    file_name = prefix + '_' + file_name + '.txt'
    with open(f"/mnt/c/users/youcode/desktop/batch-processing-movies-leans-data/test/{file_name}", "a+") as file:
        file.write(content)