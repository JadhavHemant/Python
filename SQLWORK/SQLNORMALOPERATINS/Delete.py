import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="collagedb")
mycursor=con.cursor()
mycursor.execute("DELETE from student where student_id=3")
con.commit()
print("successful")
