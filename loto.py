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

########################################################################################################
########################################################################################################

class Player:

    def __init__(self, name, player_type = False):
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
        print(self.username)
        print('='*27)
        for i in self.array:
            lineforprint = (' '.join(map(str, i.ravel())))
            print(lineforprint.replace('n', ' '))
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
            self.array[indexnum] = '-' + '=' + '-'
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

#Объявляем мешок как константу, всегда 90 шт.
BOCHONKI = [i for i in range(1, 91)]
players = []
winer_exist = False

# count_players = int(input('Введите количество игроков: '))
# for i in range(count_players):
#     player_name = input('Введите имя игрока')
#     player_type = int(input('Введите тип игрока, Человек - введите 1, компьютер - введите 0:'))
#     player_card = Card(player_name)
#     players.append(player_card)

count_players = int(input('Введите количество игроков: '))
for i in range(count_players):
    player_name = input('Введите имя игрока')
    player_type = int(input('Введите тип игрока, Человек - введите 1, компьютер - введите 0:'))
    if player_type:
        player = Player(player_name, True)
        players.append(player)
    else:
        player = Player(player_name, False)
        players.append(player)

#TODO: сделать счетчик ходов
while True:
    #Вытаскиваем случаный бочонок
    current_bochonok = str(BOCHONKI.pop(random.randrange(len(BOCHONKI))))
    print('Текущий номер бочонка', current_bochonok)
    #print(BOCHONKI)

    for player in players:
        if player.is_human:#проверяем цифру в карте человека
            player.card.showcard()
            print(player.is_human, player.name, 'Выбирает')
            answ = input('Закрыть номер бочонка в карте? (Введите да или нет): ')
            if answ == 'да':
                if player.card.bochonoknum_is_in_card(current_bochonok):
                    player.card.cover_bochonoknum(current_bochonok)
                else:
                    print('Ошибка, номера в карте нет, вы проиграли')
                #if player.card.check_win():
                #       print('Человек выиграл')
                #TODO: сменить статус победителя у юзера, чтобы елси комп тоже выиграл то объявить их обоих победителями
            else:
                if player.card.bochonoknum_is_in_card(current_bochonok):
                    print('Ошибка, номер есть в карте, вы проиграли')
        else:
            print('Проверяем номер в карточке компьютера')
            player.card.showcard()
            if player.card.bochonoknum_is_in_card(current_bochonok):
                player.card.cover_bochonoknum(current_bochonok)
                if player.card.check_win():
                    print('Комп выиграл')
                    #TODO: сменить статус победителя у юзера, чтобы елси комп тоже выиграл то объявить их обоих победителями





#while not winer_exist:

    #Вытаскиваем случаный бочонок
#    current_bochonok = str(BOCHONKI.pop(random.randrange(len(BOCHONKI))))
#    print('Текущий номер бочонка', current_bochonok)
    #print(BOCHONKI)

    # maxim_card = Card()
    # #print(maxim_card)
    # maxim_card.showcard()

    # if maxim_card.check_win():
    #     print('победитель')
    # else:
    #     print('еще не все зачеркнули')
    #
    # #проверяем цифру в карте
    # if Card.bochonoknum_is_in_card(maxim_card, current_bochonok):
    #     print('есть в карте')
    #
    #
    # #зачеркиваем цифру
    # #cover_bochonoknum(maxim_card., current_bochonok)
    # maxim_card.cover_bochonoknum(current_bochonok)
    # maxim_card.showcard()
    #
    # #после каждого хода проверяем победителя
    #
    # #игра окончена, объявляем победителя
    #
