#Create a menu driven calculator
def add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def divide (a,b):
    if b!=0:
        return a/b
    else:
        return "Division by zero is not allowed"
    
while True:
    print("\n--------------Menu-------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-------------------------------")
    
    Choice=float(input("Input your choice: "))
    
    if Choice==5:
        print("Exiting Program...")
        break
    
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    
    if Choice==1:
        print("Result: ", add(num1,num2))
    elif Choice==2:
        print("Result: ", Subtract(num1,num2))
    elif Choice==3:
        print("Result: ", Multiply(num1,num2))
    elif Choice==4:
        print("Result: ", divide(num1,num2))    
    else:
        print("Invalid choice! Try again...")   
        