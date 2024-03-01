import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Remove numbers greater than 50 and replace others with "XX"
for i in range(len(random_numbers)-1, -1, -1):  # Iterate backwards to avoid index issues when removing items
    if random_numbers[i] > 50:
        random_numbers.pop(i)  # Remove numbers greater than 50
    else:
        random_numbers[i] = "XX"  # Replace other numbers with "XX"

# Print the final list
print(random_numbers)
