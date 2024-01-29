from elasticsearch import Elasticsearch
from flask import Flask,jsonify,url_for,redirect,render_template,request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from math import ceil


app = Flask(__name__)


client = Elasticsearch(
    "http://localhost:9200",  # Elasticsearch endpoint
    )

def get_all_movies():
    query = {
        "query": {
             "match_all": {}
        }
    }
    result = client.search(index='movies_detailsindex', body=query)
    total_movies = result['hits']['total']['value']
    return total_movies



def get_movies(page=1, size=10):
    if page <= 0:
        page = 1
    query = {
        "query": {
            "match_all": {}
        },
        "from": (page - 1) * size,
        "size": size
    }
    result = client.search(index='movies_detailsindex', body=query)
    return result['hits']['hits']

def get_top_movies():
  query = {
    "query": {
        "match_all": {}
    },
    "sort": [
        {
            "vote_count": {
                "order": "desc"
            }
        }
    ]
  }
  result = client.search(index='movies_detailsindex', body=query,size=5)
  return result['hits']['hits']


@app.route('/api/movies/<string:movie_id>', methods=['GET'])
def get_movie(movie_id):
  try:
    movie_details = client.get(index="movies_detailsindex", id=movie_id)
    details = movie_details['_source']
    return render_template("details.html",movie_details=details)
  except Exception as e:
    return jsonify({"error": f"Movie with ID {movie_id} {e} not found"}), 404



@app.route('/', methods=['GET'])
def index():
    page = int(request.args.get('page', 1))
    if(page <= 0):
       page = 1
    size = int(request.args.get('size', 10))
    movies = get_movies(page,size)
    top_movies = get_top_movies()
    total_movies = get_all_movies()
    total_pages = ceil(total_movies / size)
    return render_template("index.html",movies=movies,top_movies=top_movies, page=page, size=size, total_pages=total_pages)


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')

     # Elasticsearch query to search by title
    es_query = {
        "query": {
            "match": {
                "title": query
            }
        }
    }
    top_movies = get_top_movies()
    # Search using Elasticsearch
    results = client.search(index='movies_detailsindex', body=es_query,size=1000)
    search_results = results['hits']['hits']
    return render_template("search.html",search_results=search_results,top_movies=top_movies)



if __name__ == '__main__':
    app.run(debug=True)