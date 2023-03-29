# import pandas as pd
# import numpy as np
# import mysql.connector
# conn = mysql.connector.connect(user="root",host="localhost",password="@vedika",database="product")
# # data = pd.read_csv("product.csv")
# # dt=pd.DataFrame(data)
# # a=dt["name"].to_list()
# # b=dt["rate"].to_list()
# # c=dt["stock"].to_list()
# mycursor=conn.cursor()
# ints='INSERT INTO new_table(pro_name,pro_rate,pro_rate) VALUES ("mobile",1000,12)'         #(%s,%s,%s)'
# # values=(a,b,c)
# mycursor.execute(ints)    
# conn.commit()
# print("successful")
     
