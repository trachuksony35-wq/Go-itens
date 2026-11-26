# ігрове поле для гри в хрестики-нулики 
from tkinter import FALSE

import colorama
import random




colorama.init(autoreset=True)

LEN_BOARD = 3
BOARD = []
BOARD_REVERSE = []
USER_1 = colorama.Fore.BLUE + "X" + colorama.Fore.RESET
USER_2 = colorama.Fore.RED + "O" + colorama.Fore.RESET

for _ in range(LEN_BOARD):
    row =[]
    for _ in range(LEN_BOARD):
        row.append(" ")

    BOARD.append(row)
    BOARD_REVERSE.append(row.copy())

user = 1 
while True:
    X_R = random.randint(0, 2)
    Y_R = random.randint(0, 2)

    board = []
    for row in BOARD:
        board.append("|".join(row))

    board_str = "\n-----\n".join(board)
    print(board_str)

    if [USER_1] * LEN_BOARD in BOARD or [USER_2] * LEN_BOARD in BOARD:
        print(f"\nГравець № {1 if user == 2 else 2} переміг!\n")
        break

    for i in range(LEN_BOARD):
        for j in range(LEN_BOARD):
            BOARD_REVERSE[i][j] = BOARD[j][i]

    if [USER_1] * LEN_BOARD in BOARD_REVERSE or [USER_2] * LEN_BOARD in BOARD_REVERSE:
        print(f"\nГравець № {1 if user == 2 else 2} виграв цей раунд!\n")
        break

    win_line_1 = []
    for i in range(LEN_BOARD):
        win_line_1.append(BOARD[i][i])

    win_line_2 = []
    for i in range(LEN_BOARD):
        win_line_2.append(BOARD[i][LEN_BOARD-i-1])

    if (win_line_1 in [[USER_1] * LEN_BOARD, [USER_2] * LEN_BOARD] or
        win_line_2 in [[USER_1] * LEN_BOARD, [USER_2] * LEN_BOARD]):
        print(f"\nГравець № {1 if user == 2 else 2} виграв цей раунд!\n")
        break


    is_free = FALSE
    for line in BOARD:
        if " " in line:
            is_free = True

    if not is_free:
        print("\nВиграла дружба 😎\n")
        break


    if user ==1:
        coord = input(f"\n Гравець № {user} введи координату клітини через пробіл: ")
        x, y = coord.split()
    else:
        x, y = X_R, Y_R

    if BOARD[int(y)-1][int(x)-1] != " ":
        print(colorama.Fore.RED + "\nЦя клітина вже зайнята, Вибери іншу.\n")
        continue

    if user == 1:
        BOARD[int(y)-1][int(x)-1] = USER_1
        user = 2
    else:
        BOARD[int(y)-1][int(x)-1] = USER_2
        user = 1

print("\n----------------------------------------\n")