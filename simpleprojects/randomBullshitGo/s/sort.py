import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [random.randint(0, 9999) for i in range(9999)]

num_runs = random.randint(1, 99999)
total_time = 0

for _ in range(num_runs):
    start_time = time.time()
    sorted_arr = quicksort(arr)
    end_time = time.time()
    total_time += (end_time - start_time) * 1000

average_time = total_time / num_runs
print(f"\nNumber of runs: {num_runs}")
print(f"Average time taken: {average_time:.3f} milliseconds")