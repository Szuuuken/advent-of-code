from typing import List

def main():
    file = open('day13_example_input.txt', 'r')
    lines = file.readlines()
    file.close()

    isPoint = True
    points: List(Point) = []
    commands: List(Command) = []

    for line in lines:
        line = line.strip()

        print(line)

        if len(line) == 0:
            isPoint = False
            continue

        if isPoint:
            coordinates = line.split(',')
            point = Point(coordinates[0], coordinates[1])
            points.append(point)
        else:
            c = line.spint(' ')
            command = Command(c[0], c[1], c[2])
            commands.append(command)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Command:
    def __init__(self, name, direction, content):
        self.name = name
        self.direction = direction
        self.content = content

class Paper:
    def __init__(self):
        self.points : List(Point) = []
        self.max_x = 0
        self.max_y = 0

    def add(self, point: Point):
        self.points.append(point)

        if(self.max_x < point.x): self.max_x = point.x
        if(self.max_y < point.y): self.max_y = point.y

    def hasPoint(self, x: int, y: int):
        for point in self.points:
            if point.x == x and point.y == y: return True

    def draw(self):
        for row in range(0, self.max_y):
            for column in range(0, self.max_x):
                pass

if __name__ == "__main__":
    main()