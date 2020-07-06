import pandas as pd
import numpy as nm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as cs
import csv

with open('gamescores.csv','a',newline='') as fp:

  a = csv.writer(fp, delimiter=',')

  def



  cv = CountVectorizer()
  game_file= pd.read_csv('games11.csv')
  game_file.set_index('gameid', drop = False)
  maj_list = []
  min_list = []
  genre = game_file['Genres']
  genre_list = list(genre)
  genre_list_new = []
  #modify the genre column by replacing
  for i in genre_list:
    i = i.replace(',',' ')
    genre_list_new.append(i)

  count_matrix = cv.fit_transform(genre_list_new)
  count_matrix_array = count_matrix.toarray()
  #limits##################################
  init_gameval = 1
  final_gameval = 11000+ 1
  #######################################
  #compare 2 at a time(to increase number of movies that can be used) , use the movie if cs_value > 0.8
  #disrcard others
  for i in range(10950,11001):
    
    print(i)

    for j in range(init_movieval,final_movieval):
      #print(j)
      similarity_scores = cs([count_matrix_array[i],count_matrix_array[j]])
      #discard unnecessary movies
      #print(similarity_scores)
      if similarity_scores[0][1] > 0.82:
        tu = (j,similarity_scores[0][1])
        min_list.append(tu)
    maj_list.append(min_list)
    min_list = []
  a.writerows(maj_list)