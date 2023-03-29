from TaskList import ListOperations
op=ListOperations()
i=1
while(i!=0):
    ch=int(input("Enter Choice: \n1.Add Student : \n2.Display Student : \n3.Get Student Roll-Number : \n4.calulate student Persentage : \n5.Update Student Name : \n6.delete value from list : \n7.searchbynameRollnumber : \n8.passorfail "))
    if(ch==1):
        op.Addstudent()
    elif(ch==2):
        op.Dis()
    elif(ch==3):
        op.SearchByRoll()
    elif(ch==4):
        op.Calculate()
    elif(ch==5):
        op.UpdateName() 
    # elif(ch==6):
        # op.DeleteListIteam()
    elif(ch==7):
        op.SearchByName() 
    elif(ch==8):
        op.PassStudent()       
    else:
        print("Enter Valid Number:")          
        
    i=int(input("Do You Wants Add More?yes(1)/no(0): "))
