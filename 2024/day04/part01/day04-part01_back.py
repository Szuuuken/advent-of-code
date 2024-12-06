import re
import numpy as np

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
#pp(input)
#print("####")

input_len = len(input)
result = ['.'*len(input[0])]*len(input)
#pp(result)


diags = []


t_input = [
        ["abc"],
        ["def"],
        ["ghi"]
        ]
def get_diagonals(matrix):
    diagonals = []

    ndim = matrix.shape[0]
    for i in range(-ndim + 1, ndim):
        diagonal = np.diag(matrix, i)
        diagonal_list = diagonal.tolist()

        for diagonal_sub_list in diagonal_list:
            for diagonal_item in diagonal_sub_list:
                if len(diagonal_item) > 0:
                    diagonals.append(diagonal_item)
    return diagonals

#input_x = [list(e) for e in input]
input_matrix = np.array(t_input)
a = get_diagonals(input_matrix)
#b = get_diagonals(input_matrix.transpose())

print(a)

exit()

# diags = [np.diag(matrix, i).tolist() 

matrix = np.array(input)
ndim = matrix.shape[0]
for i in range(-ndim + 1, ndim):
    d = np.diag(matrix, i).tolist()
    d = sum(d,[])
    b = []
    for e in d:
        #print(e)
        if len(e)>0:
            b.append(e)

    print(b)
    exit()

#diags = [np.diag(matrix, i).tolist() for i in range(-ndim + 1, ndim)][::-1]
#print(diags)

count = 0

exit()

for y in range(0, len(input)):
    line = input[y]
    line_len = len(line)
    result[y] = []

    for x in range(0, line_len):
        #print("------")
        #print((x,y), y +3, line_len, x+3 >= line_len)

        left_word = None if x < 3 else input[y][x-3:x+1]
        right_word = None if x + 3 > line_len else input[y][x:x+4] # [0,1,2,3,4,5,6,7,8,9] --> len == 10
        top_word = None if y < 3 else ''.join([l[x] for l in input[y-3:y+1]])
        bottom_word = None if y + 3 >= input_len else ''.join([l[x] for l in input[y:y+4]])

        left_bottom_word = None if y + 3 >= line_len or x < 2 else input[y+3][x-3] + input[y+2][x-2] + input[y+1][x-1] + input[y][x]
        left_top_word = None if y <= 2 or x <= 2 else input[y-3][x-3] + input[y-2][x-2] + input[y-1][x-1] + input[y][x]
        right_top_word = None if y <= 2 or x + 3 >= line_len else input[y-3][x+3] + input[y-2][x+2] + input[y-1][x+1] + input[y][x]
        right_bottom_word = None if y + 3 >= input_len or x + 3 >= line_len else input[y+3][x+3] + input[y+2][x+2] + input[y+1][x+1] + input[y][x]

        # print(input_len)
        #print(input[y])
        # print(input[y+1])
        # print(input[y+2])
        # print(input[y+3])

        if x == 9 and y == 0:
            print("left:", left_word)
            print("right:", right_word)
            print("top:", top_word)
            print("bottom:", bottom_word)
            print("left-bottom:", left_bottom_word)
            print("left-top:", left_top_word)
            print("right-top:", right_top_word)
            print("right-bottom:", right_bottom_word)
        #print("-------")

        words = [left_word, right_word, top_word, bottom_word, left_bottom_word, left_top_word, right_top_word, right_bottom_word]
        for word in words:
            if word != None and (word == "XMAS" or word[::-1] == "XMAS"):
                count += 1

        #print(words)

print(count)

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
