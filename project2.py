#Simple Calculator

def add(a,b):
    return a+b

def sub(a,b):
    return  a-b

def mul(a,b):
    return a*b

def div(a,b):

    if b!=0:
        return a/b
    else:
        return "Cannot be divide by Zero "

print("Select Operations:")
print("Select 1 for Addition:")
print("Select 2 for subtraction:")
print("Select 3 for multification:")
print("Select 4 for division:")
choice=input("Select from 1 to 4:")

num1=int(input("Enter a first number:"))
num2=int(input("Enter a second number:"))

if choice=='1':
    result=add(num1,num2)
    print("The result is ",result)

elif choice=='2':
    result=sub(num1,num2)
    print("The result is",result)

elif choice=='3':
    result=mul(num1,num2)
    print("the result is",result)

elif choice=='4':
    result=div(num1,num2)
    print("the result is",result)
else:
    print("Invaild Input")



