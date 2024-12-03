import re

input_file_name = "input.txt"
input = None

with open(input_file_name) as file:
    input=file.read().strip()

mul_pattern = r"mul\([1-9]{1}[0-9]{0,2},[1-9]{1}[0-9]{0,2}\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
pattern = re.compile(r"{0}|{1}|{2}".format(mul_pattern, do_pattern, dont_pattern))

commands = pattern.findall(input)

sum = 0
do = True

for command in commands:
    matches = re.findall(r"[1-9]{1}[0-9]{0,2}", command)
    
    if command == "do()":
        do = True
        continue
    
    if command == "don't()":
        do = False
        continue

    if do == False:
        continue

    first_number = int(matches[0])
    second_number = int(matches[1])
    command_result = first_number * second_number
    sum += command_result

print(sum)
