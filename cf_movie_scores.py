import pandas as pd
import sqlite3
conn=sqlite3.connect("movies_database_output.sqlite")
b=conn.cursor()
b.execute("SELECT * FROM movies ")
movies=b.fetchall()
con=sqlite3.connect('movies_scores_database.sqlite')
c=con.cursor()
c.execute("SELECT * FROM movies_scores_final")
data=c.fetchall()
#print(data)
b='Eat a Bowl of Tea '
for row in movies:
    g=list(row)

    if g[2]==b:
        a=g[0]
        break
print(a)
a=int(a)
meow=[]

for row in data:
     l=list(row)
     m=l[0]
     m=int(m)
     if m==a:
        mi_list=l[1:]
        print(mi_list)
        break

for item in mi_list:
    q = (int(item.split(',')[0].split('(')[1]))
    for row in movies:
             f=list(row)
             if f[0]==q:
                 mdict={
                 "title":f[2],
                 "year":f[3],
                 "genres":f[4]
                  }
                # print(mdict)
                 meow.append(mdict)
print(meow)





