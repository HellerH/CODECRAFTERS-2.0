import pandas as pd
movies = pd.read_csv('IMDB-Movie-Data.csv',index_col="Title")
print(movies.head())