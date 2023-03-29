states=[
    {"state_id":1,"state_name":"maharashtra","cities":[ ]}
    ]


i=1
while(i!=0):
   while (i!=0):
    n=input("Enter city : ")
    states.insert(1,n)
    i=int(input("do you want add more cities? yes(1)/no(0)"))
    print(states)