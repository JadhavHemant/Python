import pandas as pd
import mysql.connector

db = mysql.connector.connect(user = 'root', database = 'research_ms')
cursor = db.cursor()

query = "select text , user_name from tweets_data"
cursor.execute(query)

myallData = cursor.fetchall()

all_user_name = []
all_tweets = []
for  text,user_name in myallData:
    all_user_name.append(user_name)
    all_tweets.append(text)

#we need to store this data to CSV
dic = {'user_name' : all_user_name , 'tweets':all_tweets}
df = pd.DataFrame (dic)
df_csv = df.to_csv('E:/Nasir_Soft.csv')