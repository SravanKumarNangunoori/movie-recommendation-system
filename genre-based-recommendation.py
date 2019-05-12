import pandas as pd
from ast import literal_eval
import warnings


warnings.simplefilter('ignore')

genrestype=["Adventure","Action","Romance","Fantasy","Crime","Family","Science Fiction","Drama","Thriller","Animation"]
md = pd.read_csv('./tmdb-5000-movie-dataset/tmdb_5000_movies.csv')
md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
vote_counts = md[md['vote_count'].notnull()]['vote_count'].astype('int')
vote_averages = md[md['vote_average'].notnull()]['vote_average'].astype('int')
C = vote_averages.mean()
m = vote_counts.quantile(0.95)

s = md.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'genre'
gen_md = md.drop('genres', axis=1).join(s)
def build_chart(genre, percentile=0.85):
    df = gen_md[gen_md['genre'] == genre]
    vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    
    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'vote_count', 'vote_average', 'popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(250)
    
    return qualified
beinloop=True

while beinloop:
    print "The available genres:"
    for i in range(len(genrestype)):
        print i,genrestype[i]

    choice = raw_input("Enter your choice or E for exit : ")
    if choice=='E' or choice=='e':
        break
    else:
        print "You choosed :",genrestype[int(choice)]
        print "The  15 movies we recommend  are"
        temp=build_chart(genrestype[int(choice)]).head(15)
        print temp[['title', 'vote_average']]
