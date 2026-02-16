from fractions import Fraction

res = Fraction(1, 1)
iter = 0
x = 2

while iter < 100: 
    term = Fraction(1, x)
    res += term
    iter += 1
    x *= 2
    
    print(f"at {iter} the num + 1/{x-2} the result is : {float(res):.30f}")
