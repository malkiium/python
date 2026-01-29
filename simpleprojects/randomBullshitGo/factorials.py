import sys
import time
import math

# Increase maximum string digits for large integer conversion
sys.set_int_max_str_digits(10**6)

def factorial_scientific():
    x = 5500000
    print("Calculating the factorial of", x)
    print("This may take a while...")

    start_time = time.time()
    y = math.factorial(x)  # Much faster and safer than manual loop
    elapsed = time.time() - start_time

    # Convert to scientific notation
    digits = len(str(y))
    mantissa = int(str(y)[:16])  # Take first 16 digits
    mantissa_float = mantissa / (10 ** (len(str(mantissa)) - 1))

    print(f"The factorial of {x} is approximately:")
    print(f"{mantissa_float:.15f}e+{digits - 1}")
    print(f"Calculation took {elapsed:.2f} seconds.")

factorial_scientific()
