import pandas as pd 
import numpy as np 
import csv
import matplotlib.pyplot as plt  
import seaborn as sns
import warnings


warnings.simplefilter('ignore')
df1=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_credits.csv')
df2=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv')
ratings=pd.read_csv('./tmdb-5000-movie-dataset/ratings.csv')

movie_data = pd.merge(ratings, df2, on='movieId') 
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean()) 
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count()) 
user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating') 
def moviesimilar(moviename):
    forrest_gump_ratings = user_movie_rating[moviename] 
    movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)
    corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])  
    corr_forrest_gump.dropna(inplace=True)
    corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])
    print corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head()


X = raw_input("Enter a movie user watched : ")
print "The movies simlar to ",X
moviesimilar(str(X))