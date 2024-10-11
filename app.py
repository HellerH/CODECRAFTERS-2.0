from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

#Load the data
movies = pd.read_csv('IMDB-Movie-Data.csv')

#Display relevant columns (for Debugging)
print(movies.head())

def recommend_movies_based_on_genre(genre, num_recommendations=5):
    #Filter movies by genre
    filtered_movies = movies[movies['Genre']].str.contains(genre, case=False, na=False)
    recommended = filtered_movies.sort_values(by='Metascore', ascending=False).head(num_recommendations)
    return recommended

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend():
    genre = request.form('Genre')
    recommendations = recommend_movies_based_on_genre(genre)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
