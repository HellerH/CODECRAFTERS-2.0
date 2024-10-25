# from flask import Flask, render_template, request
# import pandas as pd

# app = Flask(__name__)

# #Load the data
# movies = pd.read_csv('IMDB-Movie-Data.csv')

# #Display relevant columns (for Debugging)
# print(movies.head())

# def recommend_movies_based_on_genre(genre, num_recommendations=5):
#     #Filter movies by genre
#     filtered_movies = movies[movies['Genre']].str.contains(genre, case=False, na=False)
#     recommended = filtered_movies.sort_values(by='Metascore', ascending=False).head(num_recommendations)
#     return recommended

# @app.route('/')
# def index():
#     return render_template('x.html')

# @app.route('/recommend',methods=['POST'])
# def recommend():
#     genre = request.form('Genre')
#     recommendations = recommend_movies_based_on_genre(genre)
#     return render_template('recommend.html', recommendations=recommendations)

# if __name__ == '__main__':
#     app.run(debug=True)


# Import necessary libraries
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Create Flask app
app = Flask(__name__)

# Load movie data
movies = pd.read_csv('IMDB-Movie-Data.csv', index_col= 'Rank')  # Ensure you have a CSV file with movies data
tfidf = TfidfVectorizer(stop_words='english')
movies['Description'] = movies['Description'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['Description'] + ' ' + movies['Genre'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(Rank, cosine_sim=cosine_sim):
    idx = movies[movies['Rank'] == Rank].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies[['Title', 'Genre', 'Rank', 'Metascore', 'Revenue']].iloc[movie_indices]

# Define route for recommendations
@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('Title')
    recommendations = get_recommendations(title)
    return jsonify(recommendations.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
