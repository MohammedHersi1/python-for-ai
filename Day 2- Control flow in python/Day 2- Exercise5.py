# #Create a program to find the largest number in a list using a for loop
# list=[1,4,2,3,5]
# num=list[0]
# for i in list:
#    if i > num:
#        num=i    
# print("The greatest number is: ",num)

# Using a user input
n = int(input("How many numbers? "))
first = int(input("Enter numbers: "))
greatest = first

for i in range(n - 1):
    num = int(input("Enter number: "))
    if num > greatest:
        greatest = num

print("Greatest number is:", greatest)

# # Using a range and input
# numbers = []
# for i in range(5):
#     numbers.append(int(input("Enter a number: ")))

# greatest = numbers[0]
# for num in numbers:
#     if num > greatest:
#         greatest = num

# print("Greatest:", greatest)

