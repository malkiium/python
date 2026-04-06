import random
import time
import math

W = 10
wcount = 1

while True:
    target = random.randint(1, W)
    low = 1
    high = W
    steps = 0
    same = False
    
    print(f"Searching for {target} in range [1, {W}] (10^{wcount})")
    
    while same == False:
        steps += 1
        mid = (low + high) // 2
        
        if mid == target:
            same = True
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
    
    # Number of digits in the range
    num_digits = len(str(W))
    
    # Theoretical maximum steps
    theoretical_max = math.ceil(math.log2(W))
    
    print(f"✓ Found in {steps} steps")
    print(f"Range has {num_digits} digits → needs max {theoretical_max} steps")
    print(f"Formula: {num_digits} digits × 3.32 ≈ {num_digits * 3.32:.1f} steps")
    print(f"Simple rule: digits × 3.5 = {num_digits * 3.5:.0f} steps (safe estimate)\n")
    
    W *= 10
    wcount += 1
    time.sleep(1)