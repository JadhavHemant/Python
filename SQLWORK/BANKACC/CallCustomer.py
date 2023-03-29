from CustomerAdd import BankAccount

a=BankAccount()
i=1
while(i!=0):
    ch=int(input("Enter Choice: \n1.Add New Customer : \n2.Display Customers : \n3.LogIn : \n4.Delete User By Account Number : \n5.Delete User By Id \n6.Update Password :  \n7.Update Name : \n8.Update Mobile : \n9.Update Email : \n10.creidtmoney : "))
    if(ch==1):
        a.InsertData()
    elif(ch==2):
        a.Display()    
    elif(ch==3):
        a.Login()
    elif(ch==4):
        a.DeleteUserAccount()
    elif(ch==5):
        a.DeleteUserId()    
    elif(ch==6):
        a.UpdatePassword()      
    elif(ch==7):
        a.UpdateNameByAccount()   
    elif(ch==8):
        a.UpdateMobileNByAccount()  
    elif(ch==9):
        a.UpdateEmailByAccount()    
    elif(ch==10):
        a.Xyz()                   
    else:
        print("Enter Valid Number:")          
        
    i=int(input("Do You Wants Add More?yes(1)/no(0): "))
