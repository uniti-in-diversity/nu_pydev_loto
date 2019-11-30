import loto

class Game:
    def __init__(self):
        self.players = []
        self.winers = []
        self.usererror = False
        self.cause = ''

    def run(self, count_players):
        self.count_players = count_players
        for i in range(self.count_players):
            player_name = input('Введите имя игрока')
            player_type = int(input('Введите тип игрока, Если человек - введите 1, если компьютер - введите 0:'))
            if player_type:
                player = loto.Player(player_name, True, False)
                self.players.append(player)
            else:
                player = loto.Player(player_name, False, False)
                self.players.append(player)

        lottobag = loto.Bag()
        while lottobag.bochonok:
            if self.winers:
                print('Победитель/и:', ', '.join(map(str, self.winers)))
                break
            current_bochonok = str(lottobag.take_bochonok())

            print('Текущий номер бочонка', current_bochonok)
            for player in self.players:
                if player.is_human:
                    player.card.showcard()
                    print('Карту проверяет: ', player.name)
                    answ = input('Введите "д" если хотите закрыть номер в карте: ')
                    if answ == 'д':
                        if player.card.bochonoknum_is_in_card(current_bochonok):
                            player.card.cover_bochonoknum(current_bochonok)
                            if player.card.check_win():
                                print(player.card.check_win())
                                player.winer = True
                                self.winers.append(player.name)
                                print('Живой игрок в список победителей')
                        else:
                            self.usererror = True
                            self.cause = 'Выбрано да, а номера в карте нет'
                    else:
                        if player.card.bochonoknum_is_in_card(current_bochonok):
                            self.usererror = True
                            self.cause = 'Отказались закрыть номер, а номер в карте есть'
                else:
                    print('Ходит робот по имени: ', player.name)
                    print('Проверяем номер в карточках роботов')
                    if player.card.bochonoknum_is_in_card(current_bochonok):
                        player.card.cover_bochonoknum(current_bochonok)
                        player.card.showcard()
                    if player.card.check_win():
                        player.winer = True
                        self.winers.append(player.name)
                        continue
                    player.card.showcard()

            if self.usererror:
                print('Ошибка, ты проиграл: ', self.cause)
                break
