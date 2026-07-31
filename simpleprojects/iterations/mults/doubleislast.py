def generate_numbers(max_digits: int = 100):
    results = []

    for digits in range(2, max_digits + 1):
        power = 10 ** (digits - 1)

        for last_digit in range(1, 10):
            numerator = last_digit * (power - 2)

            if numerator % 19 == 0:
                prefix = numerator // 19
                n = prefix * 10 + last_digit

                if len(str(n)) == digits:
                    results.append(n)

    return results


for n in generate_numbers(100):
    print()
    print(n, "->", n * 2)