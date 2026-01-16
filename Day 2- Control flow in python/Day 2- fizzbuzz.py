#Work 14: FizzBuzz
num3=[]
num5=[]
for i in range(1,51):
    if i%3==0:
        num3.append(i)
    elif i%5==0: 
        num5.append(i)
    continue
    
print(f"Divisible by 3 numbers: {num3}")
print(f"Divisible by 5 numbers: {num5}")