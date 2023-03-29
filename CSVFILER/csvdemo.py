import pandas as pd
data={"employee_id":[1,2,3,4,5],"salary":[1200,10000,2340,4500,9000]}
df=pd.DataFrame(data)
print(df)
df.to_excel("employes.xlsx")