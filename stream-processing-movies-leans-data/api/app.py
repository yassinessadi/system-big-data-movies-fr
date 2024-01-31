from elasticsearch import Elasticsearch
from flask import Flask,jsonify,url_for,redirect,render_template,request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from math import ceil


app = Flask(__name__)

vectorizer = CountVectorizer()


client = Elasticsearch(
    "http://localhost:9200",  # Elasticsearch endpoint
    )

def get_total_movies():
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
            "popularity": {
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
    total_movies = get_total_movies()
    total_pages = ceil(total_movies / size)
    return render_template("index.html",movies=movies,top_movies=top_movies, page=page, size=size, total_pages=total_pages)


def get_all_movies():
    # Fetch all movies without pagination
    query = {
        "query": {
            "match_all": {}
        },
        "size": 10000  # Adjust the size parameter to a value large enough to cover all your movies
    }

    result = client.search(index='movies_detailsindex', body=query)
    return result['hits']['hits']

# 
#  Search By title
# 
def search_movies(query, size=100):
    # Perform a search in Elasticsearch
    search_query = {
        "query": {
            "match": {
                "title": query
            }
        },
        "size": size
    }

    result = client.search(index='movies_detailsindex', body=search_query)
    return result['hits']['hits']



def cosine_similarity_search(query_title, search_size=100, threshold=0.5):
    # Fetch all movies without pagination
    all_movies = get_all_movies()
    titles = [movie['_source']['title'] for movie in all_movies]

    # Fit the vectorizer on all titles
    title_matrix = vectorizer.fit_transform(titles).toarray()

    # Search for movies in Elasticsearch
    search_results = search_movies(query_title, size=search_size)

    # Extract titles from the search results
    search_titles = [movie['_source']['title'] for movie in search_results]

    # If no search results, return an empty list
    if not search_titles:
        return []

    # Transform the search title using the fitted vectorizer
    query_vector = vectorizer.transform([query_title]).toarray()
    title_matrix_search = vectorizer.transform(search_titles).toarray()

    # Calculate cosine similarity
    similarities = cosine_similarity(query_vector, title_matrix_search)
    # Get indices of top N similar movies
    top_indices = [i for i, x in enumerate(similarities[0]) if x >= threshold]

    # Get the actual movies based on top indices
    top_movies = [search_results[i] for i in top_indices]

    return top_movies


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if query:

        search_result = cosine_similarity_search(query)
        top_movies = get_top_movies()
        # Search using Elasticsearch
        # results = client.search(index='movies_detailsindex', body=es_query,size=1000)
        # search_results = results['hits']['hits']
        return render_template("search.html",search_results=search_result,top_movies=top_movies)
    else:
       return render_template("page_404.html")



if __name__ == '__main__':
    app.run(debug=True)