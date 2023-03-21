f=float(input("Enter Number:"))
g=float(input("Enter Number:"))
operator=input("Enter operator:")
if operator=='+':
    print(f+g)
elif operator=='-':
    print(f-g)
elif operator=='*':
    print(f*g)
elif operator=='/':
    print(f/g)


else:
    print("Invalid operation.Please try again")
    print(operator)




