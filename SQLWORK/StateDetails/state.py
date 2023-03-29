import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="Datastate")

class state:
   def AddData(self):
        mycursor=con.cursor()
        sname=input("enter stae name : ")
        i=1
        cities=[]
        while(i!=0):
            cname=input("enter city : ")
            cities.append(cname)
            i=int(input("want more data? yes(1)/no(0)"))
        st={"state_name":sname,"cities":cities}
        print(st)
        mycursor.execute("insert into states(state_name) values('"+sname+"')") 
        con.commit()
        mycursor.execute("select max(state_id) state_id from states")  
        data=mycursor.fetchall()
        print(data)
        sid=data[0][0]
        for c in cities:
            mycursor.execute("insert into cities(city_name,state_id) values('"+c+"',"+str(sid)+")")
            con.commit()



   def GetData(self):
        mycursor=con.cursor()
        sname=input("enter stae name : ")
        mycursor.execute("select s.state_id,state_name,city_id,city_name from states s join cities c on s.state_id=c.state_id where state_name like '%"+sname+"%'")
        data=mycursor.fetchall()
        for d in data:
            print(d[1]+" "+d[3])


    


