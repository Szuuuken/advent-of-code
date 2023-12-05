from typing import List
import re
from dataclasses import dataclass

@dataclass
class FoundNumber:
    start: int
    end: int
    value: int


blacklist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "\n"]


def get_numbers_of_line(numbers_inline: list, line: str):
    result = re.finditer(r'\d+', line)

    if result is not None:
        for result_item in result:
            #print(f'#### {result_item.start()}')
            numbers_inline.append(result_item)

def is_gear(gear_index: int, numbers_in_lines: list):
    #print(numbers_in_lines)
    gear_numbers = []

    for number in numbers_in_lines:
        value = number.group()
        start = number.start()
        end = number.end()
        print(f'::: {value}')

        if len(value) > 1: end = start
        x = range(start, end + 1)

        print(f'gear_index: {gear_index}; {start}-{end} -> {x}')

        for number_index in x:
            print(f'{gear_index}-{number_index}={gear_index == number_index}')
    
        print('')
    return True

def get_gear_number(lines: [str], line_index: int, gear_index: int):
    numbers = []
    #print(f'line: {line_index}')

    current_line_result = re.finditer(r'\d+', lines[line_index])
    if(current_line_result is not None):
        for num in current_line_result:
            value = num.group()
            start = num.start()
            end = num.end() - 1
            print(f'{start}-{end}-{len(value)}; {value} x {gear_index}')

            if start == gear_index + 1 or end == gear_index - 1:
                numbers.append(value)


    if(line_index > 0):
        current_prev_line_result = re.finditer(r'\d+', lines[line_index - 1])
        if(current_prev_line_result is not None):
            for num in current_prev_line_result:
                value = num.group()
                start = num.start()
                end = num.end() - 1
                r = range(start, end + 1)
                print(f'{start}-{end}-{len(value)}; {value} x {gear_index}; {list(r)}')
                hit = False

                for i in r:    
                    if i == gear_index - 1 or i == gear_index or i == gear_index + 1:
                        hit = True

                if hit:        
                    numbers.append(num.group())

    if(line_index < len(lines)):
        current_prev_line_result = re.finditer(r'\d+', lines[line_index + 1])
        if(current_prev_line_result is not None):
            for num in current_prev_line_result:
                value = num.group()
                start = num.start()
                end = num.end() - 1
                r = range(start, end + 1)
                print(f'{start}-{end}-{len(value)}; {value} x {gear_index}; {list(r)}')
                hit = False

                for i in r:    
                    if i == gear_index - 1 or i == gear_index or i == gear_index + 1:
                        hit = True

                if hit:        
                    numbers.append(num.group())

    print(numbers)

    if len(numbers) == 2: return int(numbers[0]) * int(numbers[1])
    return None

def main():
    
    #file = open('day03_part2_custom_input.txt', 'r')
    #file = open('day03_part2_custom_input_2.txt', 'r')
    #file = open('day03_part2_example_input.txt', 'r')
    file = open('day03_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    sum = 0
    line_index = 0

    for line in lines:
        numbers_inline = []

        for possible_gear_search_result in re.finditer(r'\*', line):
            possible_gear_index = possible_gear_search_result.start()
            #print(f'{possible_gear_search_result.start()}x{possible_gear_search_result.end()}')

            gear_number = get_gear_number(lines, line_index, possible_gear_index)

            if gear_number is not None:
                sum += gear_number

        #     if(line_index > 0): get_numbers_of_line(numbers_inline, lines[line_index - 1])
        #     if(line_index < len(lines)): get_numbers_of_line(numbers_inline, lines[line_index - 1])
        #     get_numbers_of_line(numbers_inline, line)

        # if len(numbers_inline) >= 2 and is_gear(possible_gear_index, numbers_inline):
        #     pass #print('asd')

        line_index += 1
        #print(f'#{line_index}: {numbers_inline}, {len(numbers_inline)}')         


    print(f'sum: {sum}')

if __name__ == "__main__":
    main()