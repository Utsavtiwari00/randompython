#taking input
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
#taking operator
operator=input("Choose an operator(+,-,*,/,%): ")
if operator =='+':
        print(num1+num2)
elif operator =='-':
        print(num1-num2)
elif operator =='*':
        print(num1*num2)
elif operator =='/':
        print(num1/num2)
elif operator =='%':
        print(num1%num2)
else:
        print("Invalid operator")

    
