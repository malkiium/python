def generate_suffixes():
    # Basic root suffixes for thousand, million, billion, etc.
    roots = ["", "k", "m", "b", "t", "q", "qd", "sx", "sp", "o", "n", "d"]

    # Latin/Greek prefixes for higher orders
    prefixes = [
        "", "u", "du", "tri", "qtu", "qu", "sx", "sp", "oc", "n",
        "de", "ud", "duo", "tre", "qtuo", "quo", "sxo", "spo", "oco", "no",
        "vi", "uvi", "duvi", "trivi", "qtvi", "quvi", "sxvi", "spvi", "ocvi", "novi",
        # Add more groups of prefixes systematically as needed
    ]

    # Combine prefixes and roots
    suffixes = []
    for prefix in prefixes:
        for root in roots:
            suffixes.append(f"{prefix}{root}")
    return suffixes

# Function to format numbers with the generated suffixes
def format_number(num):
    suffixes = generate_suffixes()
    idx = 0
    while num >= 1000 and idx < len(suffixes) - 1:
        num //= 1000
        idx += 1
    return f"{num}{suffixes[idx]}"

# Example usage
for i in range(1, 2025):  # Print powers of 2 with formatted suffixes
    num = 2 ** i
    print(f"2^{i} = {format_number(num)}")
