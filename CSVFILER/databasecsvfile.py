import mysql.connector
import pandas as pd
df=pd.read_csv("product.csv")
n=df['name']
r=df['rate']
s=df['stock']
print(n,s,r)
conn=mysql.connector.connect(host="localhost",user="root",password="@vedika",database="product")
mycursor=conn.cursor()
for i in range(0,len(n)):
   print(n[i])
   print(r[i])
   print(s[i])
   sql = "INSERT INTO productdata (name,rate,stock) VALUES (%s, %s, %s)"
   val = (n, r,s)
#    ints='INSERT INTO productdata (name,rate,stock) VALUES('"+n[i]+"',"str(r[i])","+str(s[i])+")'
#    mycursor.execute(ints)   
mycursor.execute(sql, val) 
conn.commit()
# print("successful")
