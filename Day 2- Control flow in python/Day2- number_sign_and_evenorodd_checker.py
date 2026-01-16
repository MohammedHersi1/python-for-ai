#work1: Even or Odd && Positive, Negative and Zero
num=int(input("Enter the number: "))
if num%2==0:
    print("Number ",num," is an even number")
else:
     print("Number ",num," is an odd number")
     
if num>0:
    print("Number ",num," is a positive number")
elif num==0:
    print("Number ",num," neither positive not negative")
else:
    print("Number ",num," is a negative number")