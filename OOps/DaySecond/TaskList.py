class ListOperations:
    student = []

    def Addstudent(self):
        name = input("Enter Student Name: ")
        rno = int(input("Enter Student Roll-Number : "))
        math = int(input("Enter Student Math Marks : "))
        science = int(input("Enter Student Science Marks : "))
        marathi = int(input("Enter Student Marathi Marks : "))
        hindi = int(input("Enter Student Hindi Marks : "))
        st = {"name": name, "rno": rno, "maths": math,
              "scien": science, "marat": marathi, "hind": hindi}
        self.student.append(st)
 

    def Dis(self):
        for s in self.student:
            print(str(s["name"])+" "+str(s["rno"])+" "+str(s["maths"]) +
                  " "+str(s["scien"])+" "+str(s["marat"])+" "+str(s["hind"]))


    def SearchByRoll(self):
        x = int(input("Enter Number Roll-Number: "))
        for c in self.student:
            if c["rno"] == x:
                
                print("Student Name Is :- "+str(c["name"]))
            else:
                print("Roll-Number Is Not-Match :")


    def Calculate(self):
        for s in self.student:
            total = s["maths"]+s["scien"]+s["marat"]+s["hind"]
            d=(total/400)*100
            print(float(d),"%")
            print(total)    
            if d<=35:
                print(str(s["name"])+"  "+"Fail Ho Beta App")
            elif d>=36 and d<=49:
                print(str(s["name"])+"  "+"Pass Ho Beta Tum")
            elif d>=50 and d<=69:
                print(str(s["name"])+"  "+"Achhi Padahi chal Rahi Hai")
            elif d>70 and d<=100:
                print(str(s["name"])+"  "+"congratulations ^Topper^")


    def UpdateName(self):
            name = input("Enter Student Name: ")
            rno = int(input("Enter Student Roll-Number : "))
            math = int(input("Enter Student Math Marks : "))
            science = int(input("Enter Student Science Marks : "))
            marathi = int(input("Enter Student Marathi Marks : "))
            hindi = int(input("Enter Student Hindi Marks : "))
            st = {"name": name, "rno": rno, "maths": math,"scien": science, "marat": marathi, "hind": hindi}
            index=-1
            for d in self.student:
                if (d["rno"]==rno):
                    index=self.student.index(d)
                    break
            self.student[index]=st
            print("Update Succesfully")        
     

    # def DeleteListIteam(self):
    #     for d in self.student:
    #         self.student.remove(d["name"])
    #         print("Remove successful")


    def SearchByName(self):
        x = input("Enter Student Name : ")
        for c in self.student:
            if c["name"] == x:
                print("Student Roll-Number Is :- "+str(c["rno"]))
            else:
                print("Student Name Is Not Match :")


    def PassStudent(self):
        for s in self.student:
            total = s["maths"]+s["scien"]+s["marat"]+s["hind"]
            d=(total/400)*100
            if d>=35:
                 print("Pass student",str(s["name"])+" "+str(s["rno"]))
            else:      
                  print("Fail student",str(s["name"])+" "+str(s["rno"]))




































           