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
#input_file_name = "sampleInput.txt"
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

def check_word(x1: int, y1: int, x2: int, y2: int, x3:int , y3: int, x4: int, y4: int):
    #print((x1,y1), (x2,y2), (x3,y3), (x4,y4))
    mark(x1, y1, x2, y2, x3, y3, x4, y4)
    first_char = input[y1][x1]
    second_char = input[y2][x2]
    thrid_char = input[y3][x3]
    fourth_char = input[y4][x4]
    word = first_char + second_char + thrid_char + fourth_char

    if word != "XMAS" and word[::-1] != "XMAS":
        #print((x1,y1), (x2,y2), (x3,y3), (x4,y4), "-->", word)
        return False
        
    coordinates = str(sorted([[y1,x1], [y2,x2], [y3, x3], [y4, x4]]))
    if coordinates in found_coordinats:
        print(f"{bcolors.WARNING}{(x1,y1)} {(x2,y2)} {(x3,y3)} {(x4,y4)} --> {word}{bcolors.ENDC}")
    
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
    result[y1][x1] = input[y1][x1]
    result[y2][x2] = input[y2][x2]
    result[y3][x3] = input[y3][x3]
    result[y4][x4] = input[y4][x4]

    # ppl(result2)

    return True

for y in range(0, len(input)):
    line = input[y]
    line_len = len(line)

    for x in range(0, line_len):
        #print("------")
        #print((x,y), y +3, line_len, x+3 >= line_len)

        

        # # right   
        if x + 3 < line_len and check_word(x, y, x+1, y, x+2, y, x+3, y):
            count += 1

        # # bottom
        if y + 3 < input_len and check_word(x, y, x, y+1, x, y+2, x, y+3):
            count += 1

        # left bottom
        if y + 3 < line_len and x > 2 and check_word(x-3, y+3, x-2, y+2, x-1, y+1, x, y):
            count += 1

        #bottom right
        if y + 3 < input_len and x + 3 < line_len and check_word(x, y, x+1, y+1, x+2, y+2, x+3, y+3):
            count += 1





        # left
        # if x > 2 and check_word(x-3, y, x-2, y, x-1, y, x, y):
        #     count += 1

        # # top
        # if y > 2 and check_word(x, y-3, x, y-2, x, y-1, x, y):
        #     count += 1

        # # top left
        # if y > 2 and x > 2 and check_word(x-3, y-3, x-2, y-2, x-1, y-1, x, y):
        #     count += 1

        # # top right
        # if y > 2 and x + 3 < line_len and check_word(x+3, y-3, x+2, y-2, x+1, y-1, x, y):
        #     count += 1



            
        #left_word = None if x < 3 else input[y][x-3:x+1]
        #right_word = None if x + 3 > line_len else input[y][x:x+4] # [0,1,2,3,4,5,6,7,8,9] --> len == 10
        #top_word = None if y < 3 else ''.join([l[x] for l in input[y-3:y+1]])
        #bottom_word = None if y + 3 >= input_len else ''.join([l[x] for l in input[y:y+4]])

        #left_bottom_word = None if y + 3 >= line_len or x < 2 else input[y+3][x-3] + input[y+2][x-2] + input[y+1][x-1] + input[y][x]
        #left_top_word = None if y <= 2 or x <= 2 else input[y-3][x-3] + input[y-2][x-2] + input[y-1][x-1] + input[y][x]
        #right_top_word = None if y <= 2 or x + 3 >= line_len else input[y-3][x+3] + input[y-2][x+2] + input[y-1][x+1] + input[y][x]
        #right_bottom_word = None if y + 3 >= input_len or x + 3 >= line_len else input[y+3][x+3] + input[y+2][x+2] + input[y+1][x+1] + input[y][x]

        # print(input_len)
        #print(input[y])
        # print(input[y+1])
        # print(input[y+2])
        # print(input[y+3])

        # if x == 9 and y == 0:
        #     print("left:", left_word)
        #     print("right:", right_word)
        #     print("top:", top_word)
        #     print("bottom:", bottom_word)
        #     print("left-bottom:", left_bottom_word)
        #     print("left-top:", left_top_word)
        #     print("right-top:", right_top_word)
        #     print("right-bottom:", right_bottom_word)
        #print("-------")

        # words = [left_word, right_word, top_word, bottom_word, left_bottom_word, left_top_word, right_top_word, right_bottom_word]
        # for word in words:
        #     if word != None and (word == "XMAS" or word[::-1] == "XMAS"):
        #         count += 1

        #print(words)

ppl(result)
ppl(marked)
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
