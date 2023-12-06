from typing import List
import re

class Card:
    def __init__(self, id: int, winning_numbers: list[int], card_numbers: list[int]) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers
        self.score = self.calculcate_winning_score()

    def calculcate_winning_score(self):
        score = 0
        
        for card_number in self.card_numbers:
            if card_number in self.winning_numbers:
                score += 1

        return score


def create_card(line: str) -> Card:
    splitted_line = line.split("|")

    splitted_first_part = splitted_line[0].split(":")
    id = int(re.search(r'\d+', splitted_first_part[0]).group())

    first_part = splitted_first_part[1]
    second_part = splitted_line[1]

    winning_numbers = re.findall(r'\d+', first_part)
    card_numbers = re.findall(r'\d+', second_part)

    return Card(id, winning_numbers, card_numbers)

def create_sub_cards(original_cards: dict, card: Card) -> list[Card]:
    if card.score == 0: return []
    
    #print(f'id:{card.id}; score:{card.score}')

    new_cards = []
    for i in range(card.id + 1, card.score + card.id + 1):
        if i in original_cards:
            original_card = original_cards[i]
            new_cards.append(Card(i, original_card.winning_numbers, original_card.card_numbers))

    return new_cards

def main():
    #file = open('day04_part2_example_input.txt', 'r')
    file = open('day04_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    orignial_cards = dict()

    for line in lines:
        card = create_card(line)
        orignial_cards[card.id] = card

    queue: list[Card] = [] + list(orignial_cards.values())
    processed_cards: list[Card] = []
    len

    while len(queue) > 0:
        card = queue.pop()
        sub_cards = create_sub_cards(orignial_cards, card)
        
        for sub_card in sub_cards:
            queue.append(sub_card)

        processed_cards.append(card)

        if (len(processed_cards) % 10000) == 0:
            print(f'queue:{len(queue)}; processed:{len(processed_cards)}')

    print(f'queue:{len(queue)}; processed:{len(processed_cards)}')

if __name__ == "__main__":
    main()