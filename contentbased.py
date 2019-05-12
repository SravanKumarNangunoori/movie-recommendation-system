# coding: utf-8

import pandas
from ast import literal_eval
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def getRecommenadation(input):
    data1 = pandas.read_csv('tmdb_5000_movies.csv');
    data=pandas.read_csv('tmdb_5000_credits.csv');
    print(data.columns);
#    data1.head(5);
 #   data1['overview'].head(5)
    tfidf = TfidfVectorizer(stop_words='english')
    data1['overview'] = data1['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(data1['overview'])
    tfidf_matrix.shape
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pandas.Series(data1.index, index=data1['title']).drop_duplicates()
    idx = indices[input];
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    data33=data1['title'].iloc[movie_indices]
    if data33 is None :
     print "Enter Proper movie name"
    else:
     print(data33)


if __name__ =='__main__':
    while True:
        try:
            inputdata= raw_input("Enter Similar movies you want to watch:\n")
            getRecommenadation(inputdata)
        except ValueError:
             print("Enter correct movie name again ")