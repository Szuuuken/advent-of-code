import re

def pp(matrix: []):
    for line in matrix:
        print(line)

input_file_name = "sampleInput.txt"
input = []
input2 = []
with open(input_file_name) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        if len(line) > 0:
            input.append(line)
            input2.append(list(line))
pp(input)
print("####")
result = []

input_len = len(input)
for y in range(0, len(input)):
    line = input[y]
    line_len = len(line)

    for x in range(0, line_len):
        print("------")
        print((x,y), y+3, input_len, y+3 >= input_len)

        left_word = None if x < 3 else input[y][x-3:x+1]
        right_word = None if x + 3 > line_len else input[y][x:x+4] # [0,1,2,3,4,5,6,7,8,9] --> len == 10
        top_word = None if y < 3 else ''.join([l[x] for l in input[y-3:y+1]])
        bottom_word = None if y + 3 >= input_len else ''.join([l[x] for l in input[y:y+4]])
        left_bottom_word = None if y > 2 and x > 2 else input[y-3][x-3] + input[y-2][x-2] + input[y-1][x-1] + input[y][x]
        left_top_word = None if y + 3 >= input_len and x > 2 else input[y+3][x-3] + input[y+2][x-2] + input[y+1][x-1] + input[y][x]

        # print(input_len)
        #print(input[y])
        # print(input[y+1])
        # print(input[y+2])
        # print(input[y+3])



        #print(left_word)
        #print(right_word)
        #print(top_word)
        #print(bottom_word)
        print(left_bottom_word)
        #print("-------")



# pp(input)
exit()

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
