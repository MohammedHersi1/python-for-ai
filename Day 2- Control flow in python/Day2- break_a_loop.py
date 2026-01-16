# Work 7: Print numbers until 0 is entered
while True:  # Infinite loop
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:  # Check if the number is 0
        print("Stopping the loop.")
        break  # Exit the loop
    print("You entered:", num)