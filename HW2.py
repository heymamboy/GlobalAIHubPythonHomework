lis=[]
for i in range(0,4):
    if i==0:
        n=input("Please write your first name: ")
        lis.append(n)
    elif i==1:
        n=input("Please write your last name: ")
        lis.append(n)
    elif i==2:
        n=int(input("Please write your age: "))
        lis.append(n)
    else:
        n=int(input("Please write your date of birth (just year): "))
        lis.append(n)
        
print(lis)  

if lis[2]<18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street.")      
