from typing import List


def main(commands: List[str]):
    x, z, aim = 0, 0, 0
    for command in commands:
        direction, distance = command.split()
        distance = int(distance)
        if direction == 'forward':
            x += distance
            z += distance * aim
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
        else: raise ValueError()
    return x * z


if __name__ == '__main__':
    print(main(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']))
    print(main([l for l in open('input.txt').readlines()]))
