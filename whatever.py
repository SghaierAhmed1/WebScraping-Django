import json
import sqlite3


with open('cdis.txt') as f1:
    k1 = f1.readlines()
    ch1 = ''
    ch3 = ch1.join(k1)
    d1 = json.loads(ch3)

sqliteConnection = sqlite3.connect('db.sqlite3')
cursor1 = sqliteConnection.cursor()

for i1 in d1["cdis"]:
    print(i1)
    cursor1.execute('''INSERT INTO main_app_games(title,genre,price ,image) VALUES (?,?,?,?)''',
(i1, d1['cdis'][i1]['Genre'], d1['cdis'][i1]['Prix'], d1['cdis'][i1]['Image']))
sqliteConnection.commit()
f1.close()



