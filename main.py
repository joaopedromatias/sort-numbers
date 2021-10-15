from random import randint

r = int(input('What is the size of the array? '))
numbers_raw = []
numbers_sorted = []

for i in range (0, r):
    numbers_raw.append(randint(1,100))

print(f'Numbers in random order: {numbers_raw}')

def sort_numbers(numbers):
    j = len(numbers)
    for i in range(0, j):
        if i == 0:
            minor_value = numbers[i]
        elif numbers[i] < minor_value:
            minor_value = numbers[i]
    numbers_sorted.append(minor_value)
    numbers.remove(minor_value)

    if len(numbers_sorted) < r:
        return sort_numbers(numbers_raw)
    else: 
        return numbers_sorted

output = sort_numbers(numbers_raw)

print(f'Numbers in ascending order: {output}')