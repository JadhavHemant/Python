e=int(input("enter english marks"))
m=int(input("enter mats marks"))
h=int(input("enter hindi marks"))
total=e+m+h
per=total/3

print(total)
print(per)
if(per<40):
    print("poor")
elif(per<=41 and per>=59):
    print("Avarage")    
elif(per<=60 and per>=80):
    print("good")

