import re

input_file_name = "input.txt"
input = None
with open(input_file_name) as file:
    input=file.read().strip()


commands = re.findall(r'mul\([1-9]{1}[0-9]{0,2},[1-9]{1}[0-9]{0,2}\)', input)

sum = 0
for command in commands:
    matches = re.findall(r"[1-9]{1}[0-9]{0,2}", command)
    first_number = int(matches[0])
    second_number = int(matches[1])
    command_result = first_number * second_number
    sum += command_result

    print("{0} --> {1}*{2}={3}".format(command, first_number, second_number, command_result))

print(sum)
