# Lab6C.py
# Prints a pyramid pattern using numbers
while True:
    rows = int(input("Enter Number for Rows or 0 to quit: "))

    if rows == 0:
        print("Goodbye!")
        break

    for r in range(1, rows + 1):
        # Print spaces to center the pattern
        spaces = rows - r
        print(" " * spaces, end='')

        # Print decreasing numbers from r to 1
        for i in range(r, 0, -1):
            print(i, end='')

        # Print increasing numbers from 2 to r
        for i in range(2, r + 1):
            print(i, end='')

        print()  # Move to the next line
