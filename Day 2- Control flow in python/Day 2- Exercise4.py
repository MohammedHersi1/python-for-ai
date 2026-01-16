#Factorial Number
print("----------------Menu---------------")
print("1. Find the factorial of a number")
print("2. Exit the Program")
print("-----------------------------------")
Choice=int(input("\nEnter the Choice: "))
while True:
    if Choice==2:
        print("Exiting Program.........")
        break
    elif Choice==1:
        n=int(input("\nEnter the Number: "))
        if n<0:
            print("Factorial is not defined by for negative numbers")
        else: 
            factorial=1
            for i in range(1, n+1):
                factorial*=i
                
            print("Factorial of ",n, " is: ",factorial)
    else:
        print("Invalid Choice")
        
        
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a number: "))
# print("Factorial is:", factorial(num))