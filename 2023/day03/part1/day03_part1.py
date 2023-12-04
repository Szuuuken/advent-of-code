from typing import List
import re

blacklist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "\n"]

def is_a_valid_part(lines: list[str], lineIndex: int, startIndex: int, endIndex: int, line: str, value: str):
    #value = lines[lineIndex][startIndex:endIndex]
    line_length = len(line)
    
    if True:
        print(f'len(lines): {len(lines)}; lineIndex: {lineIndex}; len(line): {line_length}; startIndex: {startIndex}; endIndex: {endIndex}; value: {value}')
        print(f'line_length > endIndex --> {line_length > endIndex}; line[endIndex + 1]: {line[endIndex + 1]}')
        print(line[endIndex])

    if startIndex > 0 and lineIndex > 0 and lines[lineIndex - 1][startIndex - 1] not in blacklist : return True # links oben
    if startIndex > 0 and line[startIndex - 1] not in blacklist : return True # links
    if startIndex > 0 and len(lines) - 1 > lineIndex and lines[lineIndex + 1][startIndex - 1] not in blacklist : return True # links unten
    
    if lineIndex > 0 and line_length > endIndex and lines[lineIndex - 1][endIndex + 1] not in blacklist : return True # rechts oben
    if line_length > endIndex and line[endIndex + 1] not in blacklist : return True # rechts
    if len(lines) - 1 > lineIndex and line_length > endIndex and lines[lineIndex + 1][endIndex + 1] not in blacklist : return True # rechts unten

    for i in range(startIndex, endIndex + 1):
        if lineIndex > 0 and lines[lineIndex - 1][i] not in blacklist : return True

        #print(f'len(lines): {len(lines)}; lineIndex: {lineIndex};')
        if lineIndex + 1 < len(lines) and lines[lineIndex + 1][i] not in blacklist : return True

    return False

def main():
    #file = open('day03_part1_custom_input.txt', 'r')
    #file = open('day03_part1_custom_input_2.txt', 'r')
    #file = open('day03_part1_example_input.txt', 'r')
    file = open('day03_part1_real_input.txt', 'r')
    lines = file.readlines()
    file.close()

    sum = 0
    lineIndex = 0
    #lines = list(map(lambda x: x.strip(), lines))

    for line in lines:
        searchResult = re.finditer(r'\d*', line)
        if searchResult is None: continue

        numbers = []
        line_sum = 0

        for searchResultItem in searchResult:
            value = searchResultItem.group()

            if len(value) > 0 and is_a_valid_part(lines, lineIndex, searchResultItem.start(), searchResultItem.end() -1, line, value):
                numbers.append(value)
                line_sum += int(value)

        sum += line_sum
        print(f'{numbers} --> {line_sum}')
        lineIndex += 1

    print(sum)

if __name__ == "__main__":
    main()