#Покажи свой проект!
#хорошо
print("*" * 10, 'Крестики-Нолики', '*' * 10)
board = list(range(1,10))
for i in range(3):
    print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

while True:
    player_1 = int(input("выберите число для x:"))
    if player_1 in list(range(1,10)):
        board[player_1 - 1] = "x"
        for i in range(3):
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

    if (board[0] == "x" and board[1] == "x" and board[2] == "x") or \
       (board[3] == "x" and board[4] == "x" and board[5] == "x") or \
       (board[6] == "x" and board[7] == "x" and board[8] == "x") or \
       (board[0] == "x" and board[3] == "x" and board[6] == "x") or \
       (board[1] == "x" and board[4] == "x" and board[7] == "x") or \
       (board[2] == "x" and board[5] == "x" and board[8] == "x") or \
       (board[0] == "x" and board[4] == "x" and board[8] == "x") or \
       (board[2] == "x" and board[4] == "x" and board[3] == "x"):
            print("первый игрок выйграл")
            break
    player_2 = int(input("выберите число для О:"))
    if player_2 in list(range(1,10)):
        board[player_2 - 1] = "о"
        for i in range(3):
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

    if (board[0] == "о" and board[1] == "о" and board[2] == "о") or \
       (board[3] == "о" and board[4] == "о" and board[5] == "о") or \
       (board[6] == "о" and board[7] == "о" and board[8] == "о") or \
       (board[0] == "о" and board[3] == "о" and board[6] == "о") or \
       (board[1] == "о" and board[4] == "о" and board[7] == "о") or \
       (board[2] == "о" and board[5] == "о" and board[8] == "о") or \
       (board[0] == "о" and board[4] == "о" and board[8] == "о") or \
       (board[2] == "о" and board[4] == "о" and board[3] == "о"):
            print("второй игрок выйграл")
            break 