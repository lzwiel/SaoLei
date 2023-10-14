import random

def generate_minefield(size, num_mines):
    minefield = [[0 for _ in range(size)] for _ in range(size)]
    positions = random.sample(range(size*size), num_mines)

    for pos in positions:
        row = pos // size
        col = pos % size
        minefield[row][col] = "X"

    for row in range(size):
        for col in range(size):
            if minefield[row][col] == "X":
                continue

            count = 0
            for r in range(max(row - 1, 0), min(row + 2, size)):
                for c in range(max(col - 1, 0), min(col + 2, size)):
                    if minefield[r][c] == "X":
                        count += 1
            minefield[row][col] = str(count)

    return minefield

def reveal(minefield, revealed, row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True

    if minefield[row][col] != "0":
        return

    size = len(minefield)
    for r in range(max(row - 1, 0), min(row + 2, size)):
        for c in range(max(col - 1, 0), min(col + 2, size)):
            reveal(minefield, revealed, r, c)

def print_minefield(minefield, revealed):
    size = len(minefield)
    for row in range(size):
        for col in range(size):
            if revealed[row][col]:
                print(minefield[row][col], end=" ")
            else:
                print(".", end=" ")
        print()

def play_minesweeper():
    size = 5
    num_mines = 5
    minefield = generate_minefield(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    game_over = False

    while not game_over:
        print_minefield(minefield, revealed)
        row = int(input("请输入要揭开的行号（1-{}）：".format(size))) - 1
        col = int(input("请输入要揭开的列号（1-{}）：".format(size))) - 1

        if minefield[row][col] == "X":
            game_over = True
            print("很遗憾，你触雷了！游戏结束。")
        else:
            reveal(minefield, revealed, row, col)

        if all(all(revealed[row][col] or minefield[row][col] == "X" for col in range(size)) for row in range(size)):
            game_over = True
            print("恭喜你，揭开了所有的方块！游戏胜利！")

play_minesweeper()
