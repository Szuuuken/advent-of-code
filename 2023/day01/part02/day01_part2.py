from typing import List
import re

def get_number(num):
    if num == "zero" or num == "0": return 0
    if num == "one" or num == "1": return 1
    if num == "two" or num == "2": return 2
    if num == "three" or num == "3": return 3
    if num == "four" or num == "4": return 4
    if num == "five" or num == "5": return 5
    if num == "six" or num == "6": return 6
    if num == "seven" or num == "7": return 7
    if num == "eight" or num == "8": return 8
    if num == "nine" or num == "9": return 9

def get_number_of_line(line):
    strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers = dict()

    for st in strings:
        for m in re.finditer(st, line):
            index = m.start()
            
            if index > -1:
                numbers[index] = get_number(st)
    
    indexes = sorted(numbers.keys())
    sorted_dict = {i: numbers[i] for i in indexes}
    #indexes = indexes.sort()
    first_index = indexes[0]
    first_number = sorted_dict[first_index]
    last_index = indexes[-1]
    last_number = sorted_dict[last_index]

    blubb = f'{first_number}{last_number}'
    print(f'{line} --> {sorted_dict} --> {blubb}')
    return int(blubb)

def main():
    #file = open('day01_part2_example_input.txt', 'r')
    file = open('day01_part2_real_input.txt', 'r')
    lines = file.readlines()
    file.close()

    numbers: List(int) = []
    sum = 0

    for line in lines:
        line = line.strip()
        number = get_number_of_line(line)
        numbers.append(number)
        sum += number

        #print(f'{line} --> {number}\n')

    print("")
    print(f'{numbers} => {sum}')

if __name__ == "__main__":
    main()