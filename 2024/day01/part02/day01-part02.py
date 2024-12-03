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

similarity_score = 0

for left_number in first_numbers:
    matches = 0

    for right_number in second_numbers:
        if left_number == right_number:
            matches += 1

    number_score = left_number * matches
    similarity_score += number_score

print(similarity_score)
    