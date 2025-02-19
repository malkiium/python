def nearest_tens(number):
    # Calculate the nearest multiple of 10
    Tens = (number // 10) * 10
    
    # Check if the number is closer to the lower or upper multiple of 10
    if number / 10 >= Tens:
        # If the number is closer to the lower multiple of 10
        upperTens = Tens
        lowerTens = Tens - 10
    else:
        # If the number is closer to the upper multiple of 10
        upperTens = Tens + 10
        lowerTens = Tens
    
    # Create a tuple with the nearest lower and upper multiples of 10
    nears = (lowerTens, upperTens)
    
    # Print the tuple of nearest tens
    print(nears)
    
    # Return the tuple of nearest tens
    return nears

# Ask the user to input a number
n = int(input("give a number : "))

# Call the function with the user's number
nearest_tens(n)