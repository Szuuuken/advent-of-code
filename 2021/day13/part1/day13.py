from typing import List

def main():
    file = open('day13_example_input.txt', 'r')
    lines = file.readlines()
    file.close()

    point_command_separation_index = lines.index("\n")
    point_lines = lines[0:point_command_separation_index]
    command_lines = lines[point_command_separation_index+1:]
    
    paper = Paper(point_lines)

    print(point_lines)
    print(command_lines)

    return

    isPoint = True
    commands: List(FoldCommand) = []
    paper = Paper(lines)

    for line in lines:
        line = line.strip()

        if len(line) == 0:
            isPoint = False
            continue

        if isPoint:
            coordinates = line.split(',')
            point = Point(int(coordinates[0]), int(coordinates[1]))
            paper.add(point)
        else:
            c = line.split(' ')
            c = c[2].split('=')
            command = FoldCommand(c[0], int(c[1]))
            commands.append(command)

    paper.draw()
    for command in commands:
        paper = paper.fold(command)
        paper.draw()
        return

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class FoldCommand:
    def __init__(self, direction: str, index: int):
        self.direction = direction
        self.index = index

class Paper:
    def __init__(self, lines: List(str)):
        self.points : List(Point) = []
        self.max_x: int = 0
        self.max_y: int = 0
        self.grid: List(List(bool))= []

        for line in lines:
            coordinates = line.strip().split(",")
            point = Point(coordinates[0], coordinates[1])
            self.points.append(point)

        if(self.max_x < point.x): self.max_x = point.x
        if(self.max_y < point.y): self.max_y = point.y

        for y in self.max_y:
            self.grid.append([])

            for x in self.max_x:
                self.grid[y].append()

    def add(self, point: Point):
        if self.hasPoint(point.x, point.y): return

        self.points.append(point)

        if(self.max_x < point.x): self.max_x = point.x
        if(self.max_y < point.y): self.max_y = point.y

    def hasPoint(self, x: int, y: int):
        for point in self.points:
            if point.x == x and point.y == y: 
                return True
            
        return False

    def draw(self):
        output = ""

        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x + 1):
                if self.hasPoint(x, y): output += "*"
                else: output += "."

            output += "\n"

        print(output)

    def fold_along_y(self, index: int):
        paper = Paper()

        for y in range(0, self.max_y + 1):
            for x in range(0, self.max_x):
                if y < index and self.hasPoint(x, y):
                    paper.add(Point(x, y))
                elif y > index and self.hasPoint(x,y):
                    new_index = self.max_y-y
                    print(f'fold at {index}: ({x},{y}), new_index:{new_index}')
                    paper.add(Point(x, self.max_y-y))
        return paper

    def fold_along_x(self, index: int):
        pass

    def fold(self, command: FoldCommand):
        if(command.direction == 'y'): return self.fold_along_y(command.index)
        else: return self.fold_along_x(command.index)

if __name__ == "__main__":
    main()