import sys
from typing import List
import re
from functools import cmp_to_key

class Hand:
    def __init__(self, line: str) -> None:
        splitted_line = line.split(" ")
        self.cards = splitted_line[0]
        self.bid = int(splitted_line[1])

        self.check()

    def is_only(self, char_counts: list[int], only_list: list[str]):
        for char_count in char_counts:
            if char_count not in only_list: return False

        return True

    def check(self):

        char_count_list = dict()
        for c in self.cards:
            if c not in char_count_list:
                char_count_list[c] = 1
            else:
                char_count_list[c] += 1
        char_counts = list(char_count_list.values())

        char_count_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        for char_count in char_counts:
            char_count_counts[char_count] += 1

        self.is_five_of_a_kind = char_count_counts[5] == 1
        self.is_four_of_a_kind = char_count_counts[4] == 1 and char_count_counts[1] == 1
        self.full_house = char_count_counts[3] == 1 and char_count_counts[2] == 1
        self.is_three_of_a_kind = char_count_counts[3] == 1 and char_count_counts[1] == 2
        self.two_pair = char_count_counts[2] == 2 and char_count_counts[1] == 1
        self.one_pair = char_count_counts[2] == 1 and char_count_counts[1] == 3
        self.high_card = char_count_counts[1] == 5

    def kind_score(self):
        if(self.is_five_of_a_kind): return 7
        if(self.is_four_of_a_kind): return 6
        if(self.full_house): return 5
        if(self.is_three_of_a_kind): return 4
        if(self.two_pair): return 3
        if(self.one_pair): return 2
        if(self.high_card): return 1

        return None
    
    def card_score(self): 

        scores = {'A': 'D',
                  'K': 'C', 
                  'Q': 'B', 
                  'J': 'A', 
                  'T': '9', 
                  '9': '8', 
                  '8': '7', 
                  '7': '6', 
                  '6': '5', 
                  '5': '4', 
                  '4': '3', 
                  '3': '2', 
                  '2': '1'}
        
        score_string = ""
        for card in self.cards:
            score_string += scores[card]

        score = int(score_string, 16)
        return score

    def fitness(self):
        score = 0x0

        if(self.is_five_of_a_kind): score = 0x10000000000000000000
        if(self.is_four_of_a_kind): score = 0x01000000000000000000
        if(self.full_house): score = 0x00100000000000000000
        if(self.is_three_of_a_kind): score = 0x00010000000000000000
        if(self.two_pair): score = 0x00001000000000000000
        if(self.one_pair): score = 0x00000100000000000000
        if(self.high_card): score = 0x00000010000000000000

        card_score = self.card_score()        
        score += card_score

        #print(f'card_score: {card_score:020b} --> hand:{self.cards}')

        return score

def compare(items: list[Hand]):
    print(items)
    item1 = items[0]
    item2 = items[1]

    if item1.kind_score() < item2.kind_score():
        return -1
    elif item1.kind_score() > item2.kind_score():
        return 1
    elif item1.kind_score() == item1.kind_score():
        if item1.card_score() == item2.card_score():
            return 0
        elif item1.card_score() < item2.card_score():
            return -1
        elif item1.card_score() > item2.card_score():
            return 1
        
    return None

def main():
    #file = open('day07_part1_example_input.txt', 'r')
    #file = open('day07_part1_custom_input.txt', 'r') # https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
    file = open('day07_part1_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    hands = [Hand(line) for line in lines]
    sorted_hands = sorted(hands, key=cmp_to_key(lambda item1, item2: item1.fitness() - item2.fitness()))

    sum = 0
    rank = 0

    for hand in sorted_hands:
        rank += 1
        winnings = rank * hand.bid
        sum += winnings

        #print(f'card_score: {card_score:020b} --> hand:{self.cards}')
        print(f'hand: {hand.cards} score:{hand.fitness():020x} rank: {rank} bid: {hand.bid} winnings: {winnings}')
        
        

    print(sum)
    
if __name__ == "__main__":
    main()