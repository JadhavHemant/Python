import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="collagedb")
mycursor=con.cursor()
mycursor.execute("UPDATE student SET name='jojo',english=13,marathi=34,hindi=23 where student_id=1")
con.commit()
print("successful")
