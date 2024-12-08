import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def pp(matrix: []):
    for line in matrix:
        print(line)

def ppl(matrix: []):
    for line in matrix:
        print("".join(line))

input_file_name = "input.txt"
input_file_name = "sampleInput.txt"
#input_file_name = "customInput01.txt"
#input_file_name = "customInput02.txt"
#input_file_name = "customInput03.txt"
#input_file_name = "customInput04.txt"
#input_file_name = "customInput05.txt"
#input_file_name = "customInput06.txt"
#input_file_name = "customInput07.txt"
#input_file_name = "customInput08.txt"
#input_file_name = "customInput09.txt"
#input_file_name = "customInput10.txt"
#input_file_name = "customInput11.txt"
#input_file_name = "customInput12.txt"
#input_file_name = "customInput13.txt"
#input_file_name = "customInput14.txt"

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
result = []
marked = []
for y in range(0, len(input)):
    line = []
    marked_line = []
    line_len = len(line)

    for x in range(0, len(input[0])):
        line.append('.')
        marked_line.append('.')

    result.append(line)
    marked.append(marked_line)

#print(result2)

count = 0

def mark(x1: int, y1: int, x2: int, y2: int, x3:int , y3: int, x4: int, y4: int):
    marked[y1][x1] = '○'
    marked[y2][x2] = '○'
    marked[y3][x3] = '○'
    marked[y4][x4] = '○'

found_coordinats = set()

def check_word(x: int, y: int):

    left_first_char = input[y][x]
    left_second_char = input[y+1][x+1]
    left_third_char = input[y+2][x+2]

    left_word = left_first_char + left_second_char + left_third_char

    right_first_char = input[y][x+2]
    right_second_char = input[y+1][x+1]
    right_third_char = input[y][x]

    right_word = right_first_char + right_second_char + right_third_char

    if right_word != "XMAS" and right_word[::-1] != "XMAS":
        #print((x1,y1), (x2,y2), (x3,y3), (x4,y4), "-->", word)
        return False
    
    if left_word != "XMAS" and left_word[::-1] != "XMAS":
        #print((x1,y1), (x2,y2), (x3,y3), (x4,y4), "-->", word)
        return False
        
    coordinates = str(sorted([[y,x], [y+1,x+1], [y+2, x+2], [y,x+2], [y+1, x+1], [y+2,x]]))
    if coordinates in found_coordinats:
        return False
        #print(f"{bcolors.WARNING}{(x1,y1)} {(x2,y2)} {(x3,y3)} {(x4,y4)} --> {word}{bcolors.ENDC}")
    
    found_coordinats.add(coordinates)


    # first_result_char = result[y1][x1]
    # second_result_char = result[y2][x2]
    # thrid_result_char = result[y3][x3]
    # fourth_result_char = result[y4][x4]

    # if first_result_char != "." and second_result_char != "." and thrid_result_char != "." and fourth_result_char != ".":
    #     print(f"{bcolors.WARNING}{(x1,y1)} {(x2,y2)} {(x3,y3)} {(x4,y4)} --> {word}{bcolors.ENDC}")
    #     return False
    
    print(f"{bcolors.OKGREEN}{(x1,y1)} {(x2,y2)} {(x3,y3)} {(x4,y4)} --> {word}{bcolors.ENDC}")
    #print(result[y1][x1])
    result[y][x] = input[y][x]
    result[y+1][x+1] = input[y+1][x+1]
    result[y+2][x+2] = input[y+2][x+2]

    result[y][x+2] = input[y][x+2]
    result[y+1][x+1] = input[y+1][x+1]
    result[y][x] = input[y][x]

    ppl(result)

    return True

for y in range(0, len(input)):
    line = input[y]
    line_len = len(line)

    for x in range(0, line_len):
        #print("------")
        #print((x,y), y +3, line_len, x+3 >= line_len)

        if x > 1 and y > 2 and  x + 2 < line_len and y + 2 < line_len and check_word(y, x):
            count += 1

ppl(result)
ppl(marked)
print(count)