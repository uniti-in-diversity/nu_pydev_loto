import numpy as np
import random
from collections import Counter

def check_unic_nums(array):
    '''
    Так как np.random.randint генерирует ОДНО случайное число,
    следовательно при заполнении массива, чем больше размерность массив тем больше повторений.
    Даже на размерности 10, повторения случаются достаточно часто.
    Фукция проверяет есть ли неуникальные элементы в массиве
    :param array: передаем массив для проверки
    :return: True если массив неуникальный, None если уникальный.
    '''
    trigger = []
    for i in array:
        trigger.append(i)
    #print(trigger)
    i = [i for i in trigger if trigger.count(i) > 1]
    if i:
        return i

# def check_win(card):
#     '''
#     Проверка карты, все ли зачеркнуты номера,
#     :param card: карта игрока для проверки
#     :return: True если все номера зачеркнуты, т.е. n = 27
#     '''
#     templist = []
#     for i in card:
#         for n in i:
#             templist.append(n)
#     if Counter(templist).get('n') == 27:
#         return True
#     else:
#         return False

class Player:

    def __init__(self, name, player_type = False, winer = False):
        self.is_human = player_type
        self.winer = False
        self.name = name
        self.card = Card(name)

class Card():

    def __init__(self, username):
        self.username = username
        '''
        Генерация рандом массива 3 на 5 с заполнением случаными чилами от 1 до 90
        Генерация нулевого массива 3 на 4
        Конкатенация массивов по столбцам (axis = 1)
        Переемешиваем элементы массива случайным образом в рамках каждой строки
        :return: Массив 3 на 9, 5 элементов из 9 в каждой строке случайные числа,
        остальные элементы 0. Тип элементов строка.
        '''
        nums = np.random.randint(1, 91, size=(15))
        while check_unic_nums(nums):
            nums = np.random.randint(1, 91, size=(15))
        #print(nums)
        nums = np.reshape(nums, (3, 5))
        nums = np.sort(nums)
        nums = nums.astype('str')
        zero = np.array((['n', 'n', 'n', 'n'], ['n', 'n', 'n', 'n'], ['n', 'n', 'n', 'n']), str)
        array = np.concatenate([nums, zero], axis = 1)
        x, y = array.shape
        rows = np.indices((x, y))[0]
        cols = [np.random.permutation(y) for _ in range(x)]
        array = array[rows, cols]
        self.array = array

    def showcard(self):
        '''
        Печатает массив в виде игровой карточки лото, нули заменяются пустыми строками (одиночными пробелами)
        :param card: массив элементов
        :return: Print в консоль
        '''
        print('='*27)
        print('Карта игрока:', self.username)
        print('='*27)
        for i in self.array:
            lineforprint = (' '.join(map(str, i.ravel())))
            print(lineforprint.replace('n', '-=-'))
        print('='*27)

    def bochonoknum_is_in_card(self, current_bochonok):
        '''
        Проверяет есть ли номер бочонка в карте
        :param card: карта игрока (массив)
        :param bochonok: номер бочонка пробразованный в строку
        :return: индекс позиции номера бочонка в карте
        '''
        if current_bochonok in self.array:
            indexnum = np.where(self.array == current_bochonok)
            return indexnum

    def cover_bochonoknum(self, current_bochonok):
        '''
        Вычеркивает номер бочонка изкарты, если номер есть в карте.
        Наличия номера бокочнка проверяется функцией "bochonoknum_is_in_card"
        :param card: карта игрока
        :param current_bochonok: номер вытянутого из мешка бочонка
        :return: Карту с вычернкутым номером
        '''
        if current_bochonok in self.array:
            indexnum = self.bochonoknum_is_in_card(current_bochonok)
            self.array[indexnum] = 'n'
        return self.array

    def check_win(self):
        '''
        Проверка карты, все ли зачеркнуты номера,
        :param card: карта игрока для проверки
        :return: True если все номера зачеркнуты, т.е. n = 27
        '''
        templist = []
        for i in self.array:
            for n in i:
                templist.append(n)
        if Counter(templist).get('n') == 27:
            return True
        else:
            return False

class Bag:
    def __init__(self):
        self.bochonok = [i for i in range(1, 91)]

    def take_bochonok(self):
        return self.bochonok.pop(random.randrange(len(self.bochonok)))

#################################################### GAME #########################################

# #class Game:
# players = []
# winers = []
# usererror = False
# cause = ''
# # count_players = int(input('Введите количество игроков: '))
# # for i in range(count_players):
# #     player_name = input('Введите имя игрока')
# #     player_type = int(input('Введите тип игрока, Человек - введите 1, компьютер - введите 0:'))
# #     player_card = Card(player_name)
# #     players.append(player_card)
#
# count_players = int(input('Введите количество игроков: '))
# for i in range(count_players):
#     player_name = input('Введите имя игрока')
#     player_type = int(input('Введите тип игрока, Если человек - введите 1, если компьютер - введите 0:'))
#     if player_type:
#         player = Player(player_name, True, False)
#         players.append(player)
#     else:
#         player = Player(player_name, False, False)
#         players.append(player)
#
#
# lottobag = Bag() #инициализиурем мешок бочонков
# while lottobag.bochonok: #пока есть бочонки в мешке, играем
#     #print('Победители', winers)
# #    if not winers:
# #        print('False')
# #    else:
# #        print('True')
#     if winers:
#         print('Победитель/и:', ', '.join(map(str, winers)))
#         break
#     current_bochonok = str(lottobag.take_bochonok())
#     #print(current_bochonok)
#     #Вытаскиваем случаный бочонок
#     #try:
#     #    current_bochonok = str(BOCHONKI.pop(random.randrange(len(BOCHONKI))))
#     #except ValueError:
#     #    print()
#     #if current_bochonok:
#     print('Текущий номер бочонка', current_bochonok)
#     #print('Играют: ', players[0].__dict__.values(), players[1].__dict__.values())
#     for player in players:
#         if player.is_human:
#             player.card.showcard()
#             print('Карту проверяет: ', player.name)
#             answ = input('Введите "д" если хотите закрыть номер в карте: ')
#             if answ == 'д':
#                 if player.card.bochonoknum_is_in_card(current_bochonok):
#                     player.card.cover_bochonoknum(current_bochonok)
#                     if player.card.check_win():
#                         print(player.card.check_win())
#                         player.winer = True
#                         winers.append(player.name)
#                         print('Живой игрок в список победителей')
#                 else:
#                     usererror = True
#                     cause = 'Выбрано да, а номера в карте нет'
#             else:
#                 if player.card.bochonoknum_is_in_card(current_bochonok):
#                     usererror = True
#                     cause = 'Отказались закрыть номер, а номер в карте есть'
#         else:
#             print('Ходит робот по имени: ', player.name)
#             print('Проверяем номер в карточках роботов')
#             if player.card.bochonoknum_is_in_card(current_bochonok):
#                 player.card.cover_bochonoknum(current_bochonok)
#                 player.card.showcard()
#             if player.card.check_win():
#                 player.winer = True
#                 winers.append(player.name)
#                 #print('Комп в списке победителей')
#                 continue
#             player.card.showcard()
#
#     if usererror:
#         print('Ошибка, ты проиграл: ', cause)
#         break
