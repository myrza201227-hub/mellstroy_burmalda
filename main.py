import random
import time

player_score = 0
comp_score = 0

while True:
    player = input("камень/ножницы/бумага").lower()
    comp = random.choice(["камень", "ножницы","бумага"])
    print(comp)

    #делаем код которая сравнивает выбор игрока и компютера.
    #пока что делаем код выйгрыша компютера
    if comp == "камень" and player == "ножницы":
        print("компютер выйграл")
        comp_score += 1
        print("очки у компа:",comp_score)
    elif comp == "ножницы" and player == "бумага":
        print("компютер выйграл")
        comp_score += 1
        print("очки у компа:",comp_score)
    elif comp == "бумага" and player == "камень":
        print("компютер выйграл")
        comp_score += 1
        print("очки у компа:",comp_score)
    elif comp == player:
        print("ничья")
        print("очки у игрока:",player_score)
        print("очки у компа:",comp_score)
    else:
        print("такой команды не существует")
    #теперь код выйгрыша игрока
    if comp == "камень" and player == "бумага":
        print("вы выйграли")
        player_score += 1
        print("очки у игрока:",player_score)
    elif comp == "ножницы" and player == "камень":
        print("вы выйграли")
        player_score += 1
        print("очки у игрока:",player_score)
    elif comp == "бумага" and player == "ножницы":
        print("вы выйграли")
        player_score += 1
        print("очки у игрока:",player_score)
    else:
        print("такой команды не существует")