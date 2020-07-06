import pandas as pd
import numpy as nm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

with open('moviescores.csv','a',newline='') as fp:

  a = csv.writer(fp, delimiter=',')

  def get_title_from_index(index):
    return movies_file[movies_file.index == index]['title'].values[0]


  def get_index_from_title(title):
    return movies_file[movies_file.title == title]['movieId'].values[0]

  #change this to a variable later
  movie_user_likes = "Toy Story (1995)"


  cv = CountVectorizer()
  df = pd.read_csv('movied_final_1.csv')
  df=df.set_index('movieId')

  print(df)
  MOV_list=df['movieNO'].tolist()
  print(MOV_list)

  maj_list = []
  min_list = []
  genre = df['genres']
  genre_list = list(genre)
  genre_list_new = []
  #modify the genre column by replacing
  for i in genre_list:
    i = i.replace('|',' ')
    genre_list_new.append(i)


  #count_matrix = cv.fit_transform(genre_list_new)
  #count_matrix_array = count_matrix.toarray()
  #limits##################################
  #print(count_matrix_array)
  #print(genre_list_new)
  features=['genres']
  def combine_features(row):
    return row['genres']
  df['combined_features']=df.apply(combine_features,axis=1)
  #print(df["combined_features"])
  cv=CountVectorizer()
  count_matrix=cv.fit_transform(df["combined_features"])
  cosine_sim=cosine_similarity(count_matrix)
  #print(cosine_sim)
  maj_list=[]
  b=0
  for m in cosine_sim:
     print(b+1)
     b=b+1

    # print(m)
     for i in range(0,9998):
       tu=(MOV_list[i],m[i])
       #print(tu)
       min_list.append(tu)
     sorted_sim_movies=sorted(min_list,key=lambda x:x[1],reverse=True)
     sorted_movies=sorted_sim_movies[:20]
       #print(sorted_movies
     maj_list.append(sorted_movies)

  a.writerows(maj_list)

