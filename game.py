import loto
import random

def game():
    games = []
    for gamer in gamers:
        games.append(Card(gamer))



    loop = True
    bag = Bag()
    msg = ''

    while loop:
        barrel, rest_num = bag.next_barrel()
        for game in games:
            game.show()
            des = game.decision(barrel, rest_num)
            answer = game.cover(barrel, des)
            loop = answer[0]
            msg = answer[1]
            if not loop:
                break
        if rest_num == 0:
            loop = False
            msg = 'Игра окончена!'

