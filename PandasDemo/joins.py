import pandas as pd

students={"rno":[1,2,3,4,5,6,7],"names":["Ajay","Amit","Sagar","Suraj","Dinesh","Deepak","Amay"]}
studentsubjects={"rno":[1,3,5,7,9,10,8],"subject":["English","Maths","Science","Hindi","History","Python","Java"]}
left=pd.DataFrame(students)
right=pd.DataFrame(studentsubjects)
# print(left)
# print(right)

# data=pd.merge(left,right,on="rno")
# data=pd.merge(left,right,on="rno",how="right")
# data=pd.merge(left,right,on="rno",how="left")
# data=pd.merge(left,right,on="rno",how="left")
data=pd.merge(left,right,on="rno",how="outer")



print(data)