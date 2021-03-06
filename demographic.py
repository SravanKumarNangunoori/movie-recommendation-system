import pandas as pd 
import numpy as np 
df1=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_credits.csv')
df2=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv')

C= df2['vote_average'].mean()
m= df2['vote_count'].quantile(0.9)
q_movies = df2.copy().loc[df2['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)
print q_movies[['title', 'score']].head(10)

