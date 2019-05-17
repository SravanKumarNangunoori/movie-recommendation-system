import pandas as pd 
import numpy as np 
import csv
df1=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_credits.csv')
df2=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv')
ratings=pd.read_csv('./tmdb-5000-movie-dataset/ratings_small.csv')

# movie_data = pd.merge(ratings, df2, on='movieId') 


with open('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv','r') as errorinput:
    reader2=csv.reader(errorinput)
    all=[]
    count=0
    row =next(reader2)
    for eachrow in reader2:
        all.append(eachrow[3])
oldmioivieids=[]
acessall=[]
with open('./tmdb-5000-movie-dataset/ratings_small.csv','r') as csvinput:
    reader=csv.reader(csvinput)
    row=next(reader)
    for row in reader:
        oldmioivieids.append(row)
        if row[1] not in acessall:
            acessall.append(row[1])
print len(acessall)
i=0
j=0
for eaval in acessall:
    j=0
    for eachrow in oldmioivieids:
        if int(eachrow[1])==int(eaval):
            eachrow[1]=all[i]
            print eachrow[1],i,j
            j=j+1
    i=i+1
    if i==4803:
        i=0
print oldmioivieids
with open('newdata.csv','w') as filout:
    writer = csv.writer(filout, lineterminator='\n')
    writer.writerows(oldmioivieids)
import pandas as pd 
import numpy as np 
import csv
df1=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_credits.csv')
df2=pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv')
ratings=pd.read_csv('./tmdb-5000-movie-dataset/ratings_small.csv')

# movie_data = pd.merge(ratings, df2, on='movieId') 


with open('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv','r') as errorinput:
    reader2=csv.reader(errorinput)
    all=[]
    count=0
    row =next(reader2)
    for eachrow in reader2:
        all.append(eachrow[3])
oldmioivieids=[]
acessall=[]
with open('./tmdb-5000-movie-dataset/ratings_small.csv','r') as csvinput:
    reader=csv.reader(csvinput)
    row=next(reader)
    for row in reader:
        oldmioivieids.append(row)
        if row[1] not in acessall:
            acessall.append(row[1])
print len(acessall)
i=0
j=0
for eaval in acessall:
    j=0
    for eachrow in oldmioivieids:
        if int(eachrow[1])==int(eaval):
            eachrow[1]=all[i]
            print eachrow[1],i,j
            j=j+1
    i=i+1
    if i==4803:
        i=0
print oldmioivieids
with open('newdata.csv','w') as filout:
    writer = csv.writer(filout, lineterminator='\n')
    writer.writerows(oldmioivieids)
