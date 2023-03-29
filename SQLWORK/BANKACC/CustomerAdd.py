import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="bank")
mycursor=con.cursor()

class BankAccount:

    def InsertData(self):
        n=input("Enter Customer Name  : ")
        an=int(input("Enter Account Number : "))
        mn=input("Enter Mobile Number : ")
        ei=input("Enter Email_id   : ")
        at=input("Enter Account Type   : ")
        ab=int(input("Enter Account Balance : "))
        pa=input("Enter Account password : ")
        ints='INSERT INTO customer(customer_name,account_number,mobile_number,email_id,account_type,account_balance,password) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        data=(n,an,mn,ei,at,ab,pa)
        mycursor.execute(ints,data)    
        con.commit()
        print("successful")



    def Display(self):
       mycursor=con.cursor()
       mycursor.execute("select * from customer")
       data=mycursor.fetchall()
       for d in data:
           print(d)



    def Login(self):
        a=int(input("Enter Account Number : "))
        p=input("Enter Password : ")
        mycursor=con.cursor()
        mycursor.execute("select * from customer where account_number="+str(a)+" and  password="+p+"")
        data=mycursor.fetchall()
        if(len(data)>0):
            print(data)
        else:
            print(" ::: Check The Account Number And Password ::: ")   


    def DeleteUserAccount(self):
        a=int(input("Enter Account Number Which One You Want To Delete : "))
        mycursor=con.cursor()
        mycursor.execute("delete from customer where  account_number= "+str(a)+" ")
        con.commit()
        print("successful") 


        
    def DeleteUserId(self):
        a=int(input("Enter Customer Id Which One You Want To Delete : "))
        mycursor=con.cursor()
        mycursor.execute("delete from customer where  customer_id= "+str(a)+" ")
        con.commit()
        print("successful") 



    def UpdatePassword(self):
        i=int(input("Enter Customer Account Number : "))
        p=input("Enter The New Password : ")
        mycursor=con.cursor()
        mycursor.execute("update customer set password='"+str(p)+"' where account_number="+str(i)+"")
        con.commit()
        print("update success")



    def UpdateNameByAccount(self):
        i=int(input("Enter Account Number : "))
        n=input("Enter The Name : ")
        mycursor=con.cursor()
        mycursor.execute("update customer set customer_name='"+n+"' where account_number="+str(i)+"")
        con.commit()
        print("update success")   

    

    def UpdateMobileNByAccount(self):
        i=int(input("Enter Account Number : "))
        n=input("Enter The Mobile Number : ")
        mycursor=con.cursor()
        mycursor.execute("update customer set mobile_number="+str(n)+" where account_number="+str(i)+"")
        con.commit()
        print("update success")  



    def UpdateEmailByAccount(self):
        i=int(input("Enter Account Number : "))
        n=input("Enter New Email : ")
        mycursor=con.cursor()
        mycursor.execute("update customer set email_id='"+n+"' where account_number="+str(i)+"")
        con.commit()
        print("update success")      
















