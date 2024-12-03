import re

with open('input.txt') as f:
    lines = [line for line in f]

first_numbers = []
second_numbers = []

for line in lines:
    first_number = int(re.search(r"^\d+", line).group())
    second_number = int(re.search(r"\d+$", line).group())

    first_numbers.append(first_number)
    second_numbers.append(second_number)

first_numbers.sort()
second_numbers.sort()

difference_sum = 0

for i in range(0, len(first_numbers)):
    first_number = first_numbers[i]
    second_number = second_numbers[i]
    difference = abs(first_number - second_number)
    difference_sum += difference

print(difference_sum)
    