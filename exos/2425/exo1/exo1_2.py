# This script calculates the Fibonacci sequence up to the nth number.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# The sequence starts with 1 and 1.

def fib(n: int):
    # If n is less than 2, return 1 as the Fibonacci sequence starts with 1 and 1.
    if n < 2:
        return 1
    else:
        # Initialize a list to store the Fibonacci sequence up to the nth number.
        fibo = [0] * n
        # The first two numbers in the Fibonacci sequence are 1.
        fibo[0] = 1
        fibo[1] = 1
        # Calculate the Fibonacci sequence from the 3rd number to the nth number.
        for i in range(2, len(fibo)):
            fibo[i] = fibo[i - 1] + fibo[i - 2]
        # Return the list containing the Fibonacci sequence.
        return fibo

# Prompt the user to enter a number.
nmb = int(input("Entrez un nombre: "))
# Print the Fibonacci sequence up to the entered number.
print(fib(nmb))