from typing import List
import re

blacklist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "\n"]

def get_numbers_of_line(numbers_inline: list, line: str):
    result = re.finditer(r'\d+', line)

    if result is not None:
        print("+")
        numbers_inline.append(result)

def is_gear(gear_index: int, first_number_start: int, first_number_end: int, second_number_start: int, second_number_end: int):
    print("n")
    return True

def main():
    #file = open('day03_part2_custom_input.txt', 'r')
    #file = open('day03_part2_custom_input_2.txt', 'r')
    file = open('day03_part2_example_input.txt', 'r')
    #file = open('day03_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    sum = 0
    line_index = 0

    for line in lines:
        numbers_inline = []

        for possible_gear_search_result in re.finditer(r'\*', line):
            possible_gear_index = possible_gear_search_result.start()

            if(line_index > 0): get_numbers_of_line(numbers_inline, lines[line_index - 1])
            if(line_index < len(lines)): get_numbers_of_line(numbers_inline, lines[line_index - 1])
            get_numbers_of_line(numbers_inline, line)

        if len(numbers_inline) == 2 and is_gear(possible_gear_index, numbers_inline[0].start(), numbers_inline[0].end(), numbers_inline[1].start(), numbers_inline[1].stop()):
            print('asd')

        line_index += 1
        print(f'#{line_index}: {numbers_inline}, {len(numbers_inline)}')         


    print(sum)

if __name__ == "__main__":
    main()