import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="collagedb")
mycursor=con.cursor()
mycursor.execute("insert into student(name,english,marathi,hindi) values('jojo',10,10,10)")
con.commit()
print("successful")
