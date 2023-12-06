from typing import List
import re

class Card:
    def __init__(self, id: int, winning_numbers: list[int], card_numbers: list[int]) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
        self.score = self.calculcate_winning_score()

    def calculcate_winning_score(self):
        pass

def create_card(line: str):
    splitted_line = line.split("|")

    first_part = splitted_line[0].split(":")[1]
    second_part = splitted_line[1]

    winning_numbers = re.findall("\d+", first_part)
    card_numbers = re.findall("\d+", second_part)

    return Card(winning_numbers, card_numbers)

def main():
    #file = open('day04_part1_example_input.txt', 'r')
    file = open('day04_part1_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    sum = 0

    for line in lines:
        card = create_card(line)

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