import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import  cosine_similarity
import os

reccomov=[]

movies=pd.read_csv("books.csv",encoding='latin1',low_memory=False)
ratings=pd.read_csv('bookratings.csv',encoding='latin1',low_memory=False)
print(movies.tail())
print(ratings.head())
M=ratings.pivot_table(index=['user_id'],columns=['book_id'],values='rating')
print(M)

M=M.fillna(0)
def standardize(row):
    new_row=(row-row.mean())/(row.max()-row.min())
    return new_row
M_std=M.apply(standardize)
print(M_std)
item_similarity=cosine_similarity(M_std.T)
print(item_similarity)
item_similarity_df = pd.DataFrame(item_similarity,index=M.columns,columns=M.columns)
print(item_similarity_df)
def get_similar_movies(book_id,rating):
    similar_score =item_similarity_df[book_id]*rating
    similar_score=similar_score.sort_values(ascending=False)
    return similar_score
#a=input("enter movie id")

#b=input("enter rating")
#a=int(a)
#b=int(b)

M=pd.read_csv('RAT.csv')
df_list=M.values.tolist()
#rint(df_list)
for item in df_list:
   pilist=item
   for a in pilist:
        try:

            P = get_similar_movies(a, 5)
            p = P[:16]
            pdf = pd.DataFrame(p)

            os.remove('temp.csv')
            pdf.to_csv('temp.csv', index=True)
            rec = pd.read_csv("temp.csv")
            # qdf.to_csv('kfdk.csv')
            # kfdk=pd.read_csv('kfdk.csv')
            mi = rec['book_id']
            mi_list = list(mi)
            # os.remove('kfdk.csv')
            # print(mi_list)
            qdf = pd.DataFrame(mi_list)
            qdf.columns = ['book_id']

            K = qdf.T

            K.to_csv('bookscores.csv', mode='a', header=False)
           # print(a)
        except:
            continue



