# from flask import Flask,redirect,url_for

# app = Flask(__name__)


# @app.route("/")


# def home():
#     return 'Hello world <h1>HELLO<h1>'

# @app.route('/<name>')
# def user(name):
#     return f'Hello {name}'

# @app.route('/admin')
# def admin():
#     return redirect(url_for('home'))

# if __name__ == "__main__":
#     app.run(debug = True)

from flask import Flask, request, render_template
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

#Load the Dataset
df = pd.read_csv('IMDB-Movie-Data.csv')

# Preprocess the data
tfidf = TfidfVectorizer(stop_words='english')
df['overview'] = df['overview'].fillna('')
tfidf_matrix = tfidf .fit_transform(df['overview'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recomendations(title, cosine_sim=cosine_sim):
    idx = df[df['title']] == [title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend' , methods=['POST'])
def recommend():
    movie = request.form['movie']
    recommendations = get_recomendations(movie)
    return render_template('recommend.html', movie=movie, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)