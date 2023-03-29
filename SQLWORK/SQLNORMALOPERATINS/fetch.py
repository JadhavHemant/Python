import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="collagedb")
mycursor=con.cursor()
mycursor.execute("select * from student")
data=mycursor.fetchall()

# print(data)

for i in data:
    print(i)