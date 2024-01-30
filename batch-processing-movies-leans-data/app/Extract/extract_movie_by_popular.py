import requests
import pandas as pd
import json
import helpers
import requests
import pandas as pd
import json

def getMovies():
    page_file_path = '/mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/index.txt'
    page = helpers.readIndexOfRows(page_file_path)
    url_movie = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}&api_key=56281eca4b19d405a20b1ca2cd04ad9d"
    response_movies = requests.get(url_movie)
    if response_movies.status_code == 200:
        helpers.writeIndexOfRows(page_file_path,page,1)
        return response_movies.text.encode('utf-8')
    else:
        return None
    

res = getMovies()
if res != None:
    data_movies = json.loads(res)
    movie_id = [data_movies["results"][x]['id'] for x in range(len(data_movies["results"]))]
    for _id in movie_id:
        url_movie = f"https://api.themoviedb.org/3/movie/{_id}?language=en-US&api_key=56281eca4b19d405a20b1ca2cd04ad9d"
        response_movie = requests.get(url_movie)
        if response_movie.status_code == 200:
            df_movie = pd.DataFrame([response_movie.json()])
            json_movie = df_movie.to_json(orient='records',lines=True)
            helpers.writeDataToHDFS('movies',json_movie)
            
        # -------------------------------------------------------------?
        url_credits = f"https://api.themoviedb.org/3/movie/{_id}/credits?language=en-US&api_key=56281eca4b19d405a20b1ca2cd04ad9d"
        response_credits = requests.get(url_credits)
        if response_credits.status_code == 200:
            data_credits = response_credits.json()
            # # actors
            df_people_cast = pd.DataFrame(data_credits['cast'])
            json_people_cast = df_people_cast.to_json(orient='records',lines=True)
            helpers.writeDataToHDFS('cast',json_people_cast)


            # ------------------------//
            #   movie cast           //
            # ----------------------//
            cast_id = df_people_cast['id']
            cast_character = df_people_cast['character']
            cast_credit_id = df_people_cast['credit_id']
            cast_order = df_people_cast['order']
            print(cast_credit_id)
            movie_cast = {
                "cast_id" : cast_id,
                'movie_id' : _id,
                'character' : cast_character,
                'credit_id' : cast_credit_id,
                'order' : cast_order
            }
            df_people_movie_cast = pd.DataFrame(movie_cast)
            json_people_movie_cast = df_people_movie_cast.to_json(orient='records',lines=True)
            helpers.writeDataToHDFS('movie_cast',json_people_movie_cast)

            # ---------------------//
            # movie producer      //
            # -------------------//
            #  # # crew
            # df_people_crew = pd.DataFrame(data_credits['crew'])
            # json_people_crew = df_people_crew.to_json(orient='records',lines=True)
            # helpers.writeDataToHDFS('crew',json_people_crew)
            # crew_id = df_people_crew['id']
            # movie_crew = {
            #     "crew_id" : crew_id,
            #     'movie_id' : _id
            # }
            # df_people_movie_crew = pd.DataFrame(movie_crew)
            # json_df_people_movie_crew = df_people_movie_crew.to_json(orient='records',lines=True)
            # helpers.writeDataToHDFS('movie_crew',json_df_people_movie_crew)