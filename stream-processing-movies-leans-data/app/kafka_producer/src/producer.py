from confluent_kafka import Producer
import requests
import json
import logging
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

bearer_token = os.environ.get("bearer_token")

#----+----+----+----+----+#
#       topic name        #
#----+----+----+----+----+#
topic = "latestmoviesdata"

#----+----+----+----+----+#
#       kafka broker      #
#----+----+----+----+----+#
kafka_config = {
    "bootstrap.servers": "localhost:9092", 
}

#----+----+----+----+----+#
#     Configure logging   #
#----+----+----+----+----+#
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



#----+----+----+----+----+#
#    init kafk producer   #
#----+----+----+----+----+#
producer = Producer(kafka_config)

counter = 1
while True:
    base_url = f"https://api.themoviedb.org/3/movie/now_playing?language=en-US&page={counter}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(base_url,headers=headers)
    if response.status_code == 200:
        time.sleep(7)

        for i in range(len(response.json()['results'])):
            time.sleep(7)
            movie_id = response.json()['results'][i]['id']
            url_movie = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
            response_movie = requests.get(url_movie,headers=headers)
            if response_movie.status_code == 200:
                data = json.dumps(response_movie.json())
                producer.produce(topic, key="key", value=data)
                producer.flush()
                logger.info("Produced message: %s", data)

        counter += 1
        if counter > response.json()['total_pages']:
            counter = 1

    else:
        logger.error("Failed to fetch movie data. HTTP status code: %d", response.status_code)