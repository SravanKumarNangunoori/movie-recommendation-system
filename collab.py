from surprise import SVD
from surprise import Reader
from surprise import Dataset
from surprise import evaluate
import pandas as pd
from pandas import plotting
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter('ignore')
reader = Reader()
ratings = pd.read_csv('ratings_small.csv')
ratings.head()

data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
data.split(n_folds=5)

svd = SVD()
evaluate(svd, data, measures=['RMSE', 'MAE'])

trainset = data.build_full_trainset()
svd.fit(trainset)
X = raw_input("Select a UserId")
Y = raw_input("Select a MovieId")
print(svd.predict(int(X),int(Y) ,3))

