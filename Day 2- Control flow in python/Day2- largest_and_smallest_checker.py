#Work2: Largest and smallest number
n=int(input("How many numbers you wanna compare: "))
numbers=[]
for i in range(1,n+1):
    num=numbers.append(input("Enter the numbers: "))
greatest=numbers[0]
minimum=numbers[0]
for i in numbers:
    if i>greatest:
        greatest=i
    elif i<minimum:
         minimum=i
print("The greatest number of the list is: ", greatest)
print("The Smallest number of the list is: ", minimum)