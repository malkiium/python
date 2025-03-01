# This program generates a multiplication table for a given number.
# The table will display the products of the number with values from 1 to 10.

def table(n: int):
    # Loop through numbers 1 to 10
    for i in range(1, 11):
        print()  # Print a new line for each row
        nmb = n * i  # Calculate the product of the input number and the current row number
        # Loop through numbers 1 to 10 for the columns
        for j in range(1, 11):
            # Print the product of the current row number and column number
            print(nmb * j, end=" ")

# Prompt the user to enter a number
nmb = int(input("Entrez un nombre: "))
# Call the table function with the user input
table(nmb)