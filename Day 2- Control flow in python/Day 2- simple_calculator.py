# work 16: Simple Calculator

while True:
    print("\n","-"*10, "Simple Menu","-"*10)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    Choice=int(input("Choose the menu: "))
    if Choice==5:
        print("Exiting Program.....")
        break
    elif Choice==1:
         num1=int(input("Enter the first Number: "))
         num2=int(input("Enter the Second Number: "))
         print("Result of the sum= ", num1+num2)
    elif Choice==2:
         num1=int(input("Enter the first Number: "))
         num2=int(input("Enter the Second Number: "))
         print("Result of the subtraction= ", num1-num2)
    elif Choice==3:
         num1=int(input("Enter the first Number: "))
         num2=int(input("Enter the Second Number: "))
         print("Result of the Multiplication= ", num1*num2)
    elif Choice==4:
         num1=int(input("Enter the first Number: "))
         num2=int(input("Enter the Second Number: "))
         if num2!=0:
            print("Result of the subtraction= ", num1/num2)
         else: 
            print("Division by zero not allowed")
    else:
        print("Choose between 1-5")