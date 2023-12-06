from typing import List
import re

def main():
    #file = open('day04_part1_example_input.txt', 'r')
    file = open('day04_part1_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    sum = 0

    for line in lines:
        splitted_line = line.split("|")

        first_part = splitted_line[0].split(":")[1]
        second_part = splitted_line[1]

        winning_numbers = re.findall("\d+", first_part)
        card_numbers = re.findall("\d+", second_part)

        got_winning_numbers_count = 0
        card_points = 0

        for card_number in card_numbers:
            if card_number in winning_numbers:
                got_winning_numbers_count += 1

                if got_winning_numbers_count == 1:
                    card_points = 1
                else: 
                    card_points = card_points * 2

        print(f'{winning_numbers}; {card_numbers} --> {got_winning_numbers_count} --> {card_points}')
        sum += card_points

    print(sum)

if __name__ == "__main__":
    main()