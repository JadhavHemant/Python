import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="bank")

mycursor=con.cursor()
a=int(input("enter acc no"))
b=int(input("balance enter"))
mycursor.execute("select account_balance+"+str(b)+" from customer where account_number="+str(a)+"")
con.commit()
print("*****")