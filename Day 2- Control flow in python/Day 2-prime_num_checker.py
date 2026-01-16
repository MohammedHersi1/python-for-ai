#work 13: Prime number checking

num=int(input("Enter the number: "))
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print(f"{num:4} is not prime number", end=" ") 
    else:
         print(f"{num:4} is a prime number", end=" ")