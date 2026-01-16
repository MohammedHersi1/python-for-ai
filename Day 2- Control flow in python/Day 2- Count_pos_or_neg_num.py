#Work 10: Count Positive and negative numbers
n=int(input("Choose number of elements to Enter: "))
numbers=[]
positive_num=0
negative_num=0
for i in range(1, n+1):
    num=numbers.append(int(input("Enter the elements: ")))

for num in numbers:
    if num >= 0:
        positive_num+=1
    else:
        negative_num+=1
        
print("The total positive numbers are: ", positive_num)
print("While the the negative numbers are: ", negative_num,end="")