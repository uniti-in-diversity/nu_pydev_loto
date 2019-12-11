import loto


class Game:
    def __init__(self):
        self.players = []
        self.winers = []
        self.usererror = False
        self.cause = ''

    def run(self, int_players):
        self.players = int_players
        lottobag = loto.Bag()
        while lottobag.bochonok:
            if self.winers:
                print('Победитель/и:', ', '.join(map(str, self.winers)))
                return True
                #break
            current_bochonok = str(lottobag.take_bochonok())

            print('Текущий номер бочонка', current_bochonok)
            for player in self.players:
                if player.is_human:
                    print(player.card)
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
                        print(player.card)
                    if player.card.check_win():
                        player.winer = True
                        self.winers.append(player.name)
                        continue
                    print(player.card)

            if self.usererror:
                print('Ошибка, ты проиграл: ', self.cause)
                return False
                #break
