#Work 3: Grade calculator
print("----------------Grade Calculator----------------")
print("A: Astonishing")
print("B: Clever")
print("C: Improvement needed")
print("D: Poor")
print("E: Very Poor")
print("F Failed")
Grade=int(input("Enter your Grade Marks: "))
if Grade>=90 and Grade<=100:
    print("Your Grade is 'A'")
elif Grade>=80 and Grade<90:
    print("Your Grade is 'B'")
elif Grade>=70 and Grade<80:
    print("Your Grade is 'C'")
elif Grade>=60 and Grade<70:
    print("Your Grade is 'D'")
elif Grade>=50 and Grade<60:
    print("Your Grade is 'E'")
elif Grade<50 and Grade>=0:
    print("Your Grade is 'F'")
else:
    print("The Number should be between 1-100")