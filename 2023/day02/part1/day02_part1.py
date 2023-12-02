from typing import List
import re

class GameSet:
    def __init__(self, set_string: str) -> None:
        self.red_cubes: int = 0
        self.blue_cubes: int = 0
        self.green_cubes: int = 0

        red_cubes_search = re.search("(?<= )[0-9]{1,2}(?= red)", set_string)
        blue_cubes_search = re.search("(?<= )[0-9]{1,2}(?= blue)", set_string)
        green_cubes_search = re.search("(?<= )[0-9]{1,2}(?= green)", set_string)

        if red_cubes_search is not None: self.red_cubes = int(red_cubes_search.group())
        if blue_cubes_search is not None: self.blue_cubes = int(blue_cubes_search.group())
        if green_cubes_search is not None: self.green_cubes = int(green_cubes_search.group())
        
class Game:
    def __init__(self, line: str):
        self.id = int(re.search("(?<=Game )[0-9]{1,3}(?=:)", line).group())
        self.sets: List(GameSet) = []
        
        for set in line.split(":")[1].split(";"):
            game_set = GameSet(set)
            self.sets.append(game_set)

            #print(f'red: {game_set.red_cubes}, blue: {game_set.blue_cubes}, green: {game_set.green_cubes}')

    def is_possible(self, red_max: int, green_max: int, blue_max: int) -> bool:
        for set in self.sets:
            if set.red_cubes > red_max or set.blue_cubes > blue_max or set.green_cubes > green_max:
                return False

        return True

def main():
    #file = open('day02_part1_example_input.txt', 'r')
    file = open('day02_part1_real_input.txt', 'r')
    lines = file.readlines()
    file.close()

    games: List(Game) = []
    sum = 0

    for line in lines:
        game = Game(line)
        games.append(game)
        
        if game.is_possible(12, 13, 14):
            print(f'game id: {game.id} is possible')
            sum += game.id
        else:
            print(f'game id: {game.id} is NOT possible')

    print(sum)

if __name__ == "__main__":
    main()