import sys
from typing import List
import re

def get_race_options(race_time, best_distance):
    #print(f'race_time: {race_time}, best_distance: {best_distance}')
    winning_options = []

    for button_time in range(race_time, -1, -1):
        remaining_time = race_time - button_time
        distance = button_time * remaining_time
        #print(f'{button_time}')

        if distance > best_distance:
            winning_options.append(button_time)

    return winning_options

def main():
    #file = open('day06_part2_example_input.txt', 'r')
    file = open('day06_part2_real_input.txt', 'r')
    lines = file.read().split('\n')
    file.close()

    races = []
    time_list = re.findall(r'\d+', lines[0])
    max_distance_list = re.findall(r'\d+', lines[1])
    winning_options = []
    result = 0
    
    for i in range(0, len(time_list)):
        availabe_time = int(time_list[i])
        max_distance = int(max_distance_list[i])
        races.append((availabe_time, max_distance))

        race_options = get_race_options(availabe_time, max_distance)
        winning_options_count = len(race_options)
        winning_options.append(winning_options_count)

        if result == 0: result = winning_options_count
        else: result *= winning_options_count
    
    print(result)
    
if __name__ == "__main__":
    main()