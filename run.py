import game
import loto

if __name__ == '__main__':

    while True:
        print('========== Лото ============')
        print('Новая игра - 1')
        print('Выход - 0')

        choice = int(input('Выберите пункт меню: '))
        if choice == 1:
            int_players = []
            count_players = int(input('Введите количество игроков: '))
            for i in range(count_players):
                player_name = input('Введите имя игрока')
                player_type = int(input('Введите тип игрока, Если человек - введите 1, если компьютер - введите 0:'))
                if player_type:
                    player = loto.Player(player_name, True, False)
                    int_players.append(player)
                else:
                    player = loto.Player(player_name, False, False)
                    int_players.append(player)

            start = game.Game()
            start.run(int_players)
        elif choice == 0:
            break
        else:
            print('Неверный пункт меню!')