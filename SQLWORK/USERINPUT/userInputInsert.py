import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="@vedika",database="collagedb")
mycursor=conn.cursor()
n=input("Enter Student Name  : ")
e=int(input("Enter English Marks : "))
m=int(input("Enter Marathi Marks : "))
h=int(input("Enter Hindi Marks   : "))
ints='INSERT INTO student(name,english,marathi,hindi) VALUES(%s,%s,%s,%s)'
data=(n,e,m,h)
mycursor.execute(ints,data)    
conn.commit()
print("successful")

