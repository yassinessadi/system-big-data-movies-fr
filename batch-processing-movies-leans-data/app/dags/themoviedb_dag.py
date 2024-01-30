from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.bash import BashOperator



default_args = {
    'owner': 'jane essadi',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 11),
    'email': [],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=60)
}


with DAG('movies_dag',
            default_args=default_args,
            schedule_interval = timedelta(minutes=20),
            catchup=False
        ) as dag:

        extract_movie = BashOperator(task_id="extract_movie", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/Extract/extract_movie_by_popular.py")
        is_files_extracted = BashOperator(task_id="is_files_extracted", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/_init_.py")
        load_actors_data = BashOperator(task_id="load_actors_data", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/load_person.py")
        load_productions_companies_data = BashOperator(task_id="load_productions_companies_data", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/load_productions_companies.py")
        load_FactProductions_movies_data = BashOperator(task_id="load_FactProductions_movies_data", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/load_fact_movies.py")
        load_movie_details_data = BashOperator(task_id="load_movie_details_data", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/load_movie_details.py")

        load_moviecredits_data = BashOperator(task_id="load_moviecredits_data", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/load_moviecredits.py")

        load_movies_genres_data = BashOperator(task_id="load_movies_genres_data", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/load_movies_genres.py")
        load_movies_production_compines_data = BashOperator(task_id="load_movies_production_compines_data", bash_command="python3 /mnt/c/users/youcode/desktop/system-big-data-movies-fr/batch-processing-movies-leans-data/app/load/load_movies_production_compiens.py")
        

        is_movies_api_ready = HttpSensor(
            task_id ='is_movie_api_ready',
            http_conn_id='themoviedb_api',
            endpoint=f'/3/movie/popular?language=en-US&page=1&api_key=56281eca4b19d405a20b1ca2cd04ad9d'
        )
        
        is_movies_api_ready >> extract_movie >> is_files_extracted

        is_files_extracted >> load_FactProductions_movies_data >> load_movies_genres_data

        is_files_extracted >> load_productions_companies_data >> load_movies_production_compines_data

        is_files_extracted >> load_FactProductions_movies_data >> load_movies_production_compines_data

        is_files_extracted >> load_FactProductions_movies_data >> load_movie_details_data

        is_files_extracted >> load_actors_data >> load_moviecredits_data

        is_files_extracted >> load_FactProductions_movies_data >> load_moviecredits_data