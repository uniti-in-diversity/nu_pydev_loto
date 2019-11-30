import game

while True:
    print('========== Лото ============')
    print('Новая игра - 1')
    print('Выход - 0')

    choice = int(input('Выберите пункт меню: '))
    if choice == 1:
        count_players = int(input('Введите количество игроков: '))
        start = game.Game()
        start.run(count_players)
    elif choice == 0:
        break
    else:
        print('Неверный пункт меню!')