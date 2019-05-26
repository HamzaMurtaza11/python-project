num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
operator=str(input("enter the operator you want to perform operation!!"))
if operator=='+':
    add=num1+num2
    print("the sum of num1 and num2 is"+str(add))
    
elif operator=='-':
    subtract=num1-num2
    print("the subtraction of num1 and num2 is "+str(subtract))
    
elif operator=='*':
    multiply=num1*num2
    print("the multiplication of num1 and num2 is"+str(multiply))
elif operator=='/':
    divide=("the division of num1 and num2 is"+str(divide))
else:
    print("invalid operator!!")
    


