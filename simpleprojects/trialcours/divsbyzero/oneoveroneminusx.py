from fractions import Fraction

res = Fraction(1, 1)
iter = 0
x = 2

while iter < 100:  # or any number of iterations you want
    term = Fraction(1, x)
    res += term
    iter += 1
    x *= 2
    
    # Print as float with limited decimals for readability
    print(f"at {iter} the num + 1/{x-2} the result is : {float(res):.30f}")