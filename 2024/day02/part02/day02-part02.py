import re

def report_is_safe(levels: [int]):
    last_level = levels[0]
    last_direction = None

    for level in levels[1:]:
        diff = last_level - level

        if abs(diff) > 3:
            return False

        direction = None

        if diff > 0:
            direction = "+"
        elif diff < 0:
            direction = "-"
        else:
            return False

        if last_direction != None and last_direction != direction:
            return False

        last_direction = direction
        last_level = level

    return True

def create_mutations(levels: [int]):
    mutations = []

    for i in range(0, len(levels)):
        mutation = levels[:i] + levels[i+1:]
        mutations.append(mutation)
        
    return mutations

input_file_name = "input.txt"
with open(input_file_name) as f:
    lines = [line for line in f]

safe_count = 0

for line in lines:
    levels = list(map(int, str.split(line)))
    
    if report_is_safe(levels):
        safe_count += 1
    else:
        mutations = create_mutations(levels)

        for mutation in mutations:
            mutation_result = report_is_safe(mutation)

            if mutation_result == True:
                safe_count += 1
                break


print(safe_count)
