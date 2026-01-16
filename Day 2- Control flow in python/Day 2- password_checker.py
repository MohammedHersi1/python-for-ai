#Work 8: Set the correct password
correct_password = "python123"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Login successful!")
        break  # Exit the loop
    else:
        print("Incorrect password. Try again.")