import pandas as pd

data={
    "employee_id":[1,2,3,4,5,6,7],
    "employee_name":["hemant","rohit","akash","sagar","ganesh","soma","nikhil"],
    "employee_Designation":["devloper","jr.devloper","tester","desiner","devloper","uidesigner","tester"]
}
df=pd.DataFrame(data)
x=df.groupby("employee_Designation")
print(x.get_group("devloper"))
for i in x:
    print(i)