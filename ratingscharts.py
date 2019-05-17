import pandas as pd 
import numpy as np 
import csv
import matplotlib.pyplot as plt  
import seaborn as sns  
sns.set_style('dark')  
 
df1=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_credits.csv')
df2=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv')
ratings=pd.read_csv('./tmdb-5000-movie-dataset/newdata.csv')

movie_data = pd.merge(ratings, df2, on='movieId') 

# print movie_data.head() 
# print movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head() 
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean()) 
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count()) 
pd.DataFrame(ratings_mean_count).to_csv("abc.csv", sep=',', encoding='utf-8')
print ratings_mean_count.head()


plt.figure(figsize=(8,6))  
plt.rcParams['patch.force_edgecolor'] = True  
sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4) 
plt.show()