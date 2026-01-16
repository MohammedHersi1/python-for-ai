# Work 9: Print only the even numbers
n=int(input("Enter a number show:  "))
for i in range(0,n+1):
    if i%2!=0:
      print(f"{i:3}",end="")  
      continue