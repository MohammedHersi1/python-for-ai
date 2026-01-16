#Work 11: Stop loop when number > 50
while True:
    num=int(input("Enter a number: "))
    if num>50:
        print("Number is greater than 50! Breaking...")
        break
    else:
        print("The number is:", num)