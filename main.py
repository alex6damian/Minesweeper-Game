import random as r
import numpy as np

def euclidian_distance(x1,x2):
    return ((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2)**0.5

def play():
    global bombs_exploded
    bombs_exploded=0
    print("Difficulty levels: Easy, Medium, Hard")
    difficulty = input("Choose a difficulty level: ").strip().capitalize()
    table = [['-'] * 10 for i in range(10)]
    opened = []
    bombs = []
    score = 0
    max_bombs = 0
    moves = 0
    def explode(x, y):
        global bombs_exploded
        bombs_exploded += 1
        opened.append((x,y))
        for i in range(-1,2):
            for j in range(-1,2):
                if x+i>=0 and x+i<10 and y+j>=0 and y+j<10:
                    table[x + i][y + j] = 'X'
                    if  (x+i, y+j) in bombs and x+i!=x and y+j!=y and (x+i, y+j) not in opened:
                        explode(x+i, y+j)
                    opened.append((x+i, y+j))

    print("You chose: " + difficulty)
    if difficulty=="Easy":
        max_bombs=2
    elif difficulty=="Medium":
        max_bombs=4
    elif difficulty=="Hard":
        max_bombs=6
    for i in range(max_bombs*2):
        while True:
            (x, y) = (r.randint(0, 9), r.randint(0, 9))
            if (x, y) not in bombs:
                bombs.append((x, y))
                break
    max_moves=100-max_bombs*9
    while bombs_exploded<max_bombs and moves<max_moves:
        while True:
            try:
                x, y = map(int, input("Enter the coordinates of the cell you want to open (x y): ").split())
                if (x, y) not in opened:
                    if (x, y) in bombs:
                        table[x][y] = 'X'
                        explode(x, y)
                    elif table[x][y] == '-':
                        table[x][y] = 'O'
                    opened.append((x, y))
                    break
                else:
                    print("Cell already opened. Try another one.")
            except ValueError:
                print("Invalid input. Enter coordinates in the format 'x y'.")
        moves += 1
        score=0
        for lines in table:
            print(*lines)
            score += lines.count('O')
        print("Score: " + str(score) + " | Bombs exploded: " + str(bombs_exploded) + " | Bombs left to explode: " + str(max_bombs - bombs_exploded) + " out of " + str(max_bombs) + " | Moves left: " + str(max_moves - moves))

    print("Game Over! Total score: " + str(score))
    return
def main():
    print("Welcome!")
    play()
if __name__=='__main__':
    main()