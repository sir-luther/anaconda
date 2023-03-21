num=int(input("Enter number:"))
flag= False
if num== 1:
    print("Number is nor prime")
elif num>1 :
    for i in range(2,num):
        if (num%i)==0:
            flag = True
if flag:
    print(num,"is not prime")
else :
    print(num,"is prime")
