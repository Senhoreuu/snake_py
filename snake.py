import os
import random


def setup():
    global currentLine, currentColumn, lastLine, lastColumn, starting, wayLine, wayColumn, foodLine, foodColumn, way, score
    currentLine = 0
    currentColumn = 0
    wayLine = 10
    wayColumn = 8
    lastLine = 0
    lastColumn = 0
    foodLine = 0
    foodColumn = 0
    starting = False
    score = 0

    way = [['🟦' for i in range(wayColumn)] for j in range(wayLine)]


def draw_way(show: bool = True):
    global wayLine, wayColumn, lastLine, lastColumn, foodLine, foodColumn, way, score, currentLine, currentColumn

    os.system('cls' if os.name == 'nt' else 'clear')

    way[lastLine][lastColumn] = '🟦'
    way[currentLine][currentColumn] = '🟩'

    lastLine = currentLine
    lastColumn = currentColumn

    eat = check_if_eat_food()

    if eat:
        way = send_food(draw=False, way=way)
    else:
        way[foodLine][foodColumn] = '🍎'

    if show:
        print(f"Score: {score}")
        print('_' * 20)

        for row in way:
            print(' '.join(row))

        print('_' * 20)
        print('\n')

    return way


def check_if_eat_food():
    global lastLine, lastColumn, foodLine, foodColumn, score

    eat = lastLine == foodLine and lastColumn == foodColumn

    if eat:
        score += 1

    return eat


def move_to_direction(direction: str):
    global lastLine, lastColumn, wayColumn, wayLine, currentLine, currentColumn

    if direction == 'w':
        currentLine -= 1
    elif direction == 's':
        currentLine += 1
    elif direction == 'a':
        currentColumn -= 1
    elif direction == 'd':
        currentColumn += 1

    if currentLine > wayLine or currentColumn > wayColumn or currentLine < 0 or currentColumn < 0:
        return end_game()

    draw_way()


def send_food(draw: bool = False, way: list = []):
    global wayLine, wayColumn, currentLine, currentColumn, foodLine, foodColumn

    foodLine = random.randint(0, wayLine - 1)
    foodColumn = random.randint(0, wayColumn - 1)

    while (foodLine == currentLine and foodColumn == currentColumn):
        foodLine = random.randint(0, wayLine - 1)
        foodColumn = random.randint(0, wayColumn - 1)

    if draw:
        draw_way()
        
    if len(way) > 0:
        way[foodLine][foodColumn] = '🍎'
        
        return way


def start_game():
    global wayLine, wayColumn, starting, currentLine, currentColumn

    starting = True

    print(f"Score: {score}")
    send_food(draw=True)

    while starting:

        direction = input('Choose a direction (w, s, a, d): ').lower()

        if direction in ['end', 'fim']:
            end_game()
            break

        if direction not in ['w', 's', 'a', 'd']:
            print('Invalid direction!')
            continue

        move_to_direction(direction)


def end_game():
    global starting
    print('End Game!')
    starting = False


def main():
    setup()
    start_game()


if __name__ == "__main__":
    main()
