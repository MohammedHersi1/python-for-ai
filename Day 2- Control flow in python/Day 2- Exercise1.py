#Example 1: Checking a condition
num=-30
if num>0:
    print("Positive Number")
elif num==0:
    print("zero")
else:
    print("Negative number")


#Example 2: Nested Conditions
age=32
if age>18:
    if age<30:
        print("Young Adult")
    else:
        print("Adult")
        
#Syntax for forloop (Loop through a list of items)
fruits=["apple","Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

#Loop with range
for i in range(5):
    print(i)    
    
#Syntax of while loop (Count down from 5)
count= 5
while count>0:
    print(count)
    count -=1 
    
#Using break and Continue for Control Flow
for i in range(10):
    if i==5:
        break
    print(i)
    
count=0
while count>=0:
    if count==11:
        break
    print(count)
    count +=1
for i in range(10):
    if i%2==0:
        continue
    print(i)

    