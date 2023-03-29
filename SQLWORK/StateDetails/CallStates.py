from state import state
s=state()
i=1
while (i!=0):
    a=int(input("Enter the \n1.Add State : \n2.Display Data : "))
    if(a==1):
        s.AddData()
    elif(a==2):
        s.GetData()    


