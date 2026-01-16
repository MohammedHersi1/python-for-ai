# #Work 5: Multiplication table
#Print header row
print("    ", end="")  # Empty corner
for j in range(1, 13):
    print(f"{j:4}", end="")  # Column headers
print("\n" + "-" * 45)  # Divider
for i in range(1, 13):
    print(f"{i:2} |", end="")  # Row header
    for j in range(1, 13):
        print(f"{i*j:4}", end="")  # Product in the grid
    print()  # Move to next row
    