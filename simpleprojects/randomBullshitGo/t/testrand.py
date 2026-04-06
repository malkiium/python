import random

max_value = 2
min_value = 1
total_over = 1
total_under = 1

def generate_random_number():
    return random.randint(min_value, max_value)

for i in range(9999999):
    generate_random_number()
    if generate_random_number() > (max_value + min_value) / 2:
        total_over += 1
    else:
        total_under += 1
    tots = (total_over/(total_over + total_under))*100

print("\n\n percent over:", tots)