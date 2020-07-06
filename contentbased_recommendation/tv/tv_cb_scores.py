import pandas as pd
import numpy as nm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

with open('scores_tv.csv','a',newline='') as fp:



  cv = CountVectorizer()
  df = pd.read_csv('tvdata.csv')

  #df.set_index('movieId', drop = False)
  maj_list = []
  min_list = []
  genre = df['listed_in']
  genre_list = list(genre)
  genre_list_new = []
  #modify the genre column by replacing
  for i in genre_list:
    i = i.replace('|',' ')
    genre_list_new.append(i)

  features=['listed_in']
  def combine_features(row):
    return row['listed_in']
  df['combined_features']=df.apply(combine_features,axis=1)

  cv=CountVectorizer()
  count_matrix=cv.fit_transform(df["combined_features"])
  cosine_sim=cosine_similarity(count_matrix)

  maj_list=[]
  for m in range(1,1969):
     similar_movies=list(enumerate(cosine_sim[m],start=1))
     print(m)
     sorted_similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)
     sorted_movies=sorted_similar_movies[:20]
     print(sorted_movies)
     maj_list.append(sorted_movies)
     min_list = []
  a.writerows(maj_list)








