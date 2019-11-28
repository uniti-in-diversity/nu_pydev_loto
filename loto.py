import numpy as np
import random

def add_separators(f):
    def inner(*args, **kwargs):
        print ('=' * 25)
        result = f(*args, **kwargs)
        print('=' * 25)
        return result
    return inner

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

def create_card():
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
    print(nums)
    nums = np.reshape(nums, (3, 5))
    nums = nums.astype('str')
    zero = np.array((['n', 'n', 'n', 'n'], ['n', 'n', 'n', 'n'], ['n', 'n', 'n', 'n']), str)
    array = np.concatenate([nums, zero], axis = 1)
    #далее перемешиваем в каждой строке элементы случайным образом
    x, y = array.shape
    rows = np.indices((x, y))[0]
    cols = [np.random.permutation(y) for _ in range(x)]
    #print(array[rows, cols])
    return array[rows, cols]

#Отобразить карточку
@add_separators
def showcard(card):
    '''
    Печатает массив в виде игровой карточки лото, нули заменяются пустыми строками (одиночными пробелами)
    :param card: массив элементов
    :return: Print в консоль
    '''
    for i in card:
        lineforprint = (' '.join(map(str, i.ravel())))
        print(lineforprint.replace('n', ' '))

#Создаем объект карту
card_max = create_card()
#Печатает карту
showcard(card_max)
#print(type(card_max))

#Объявляем мешок как константу, всегда 90 шт.
BOCHONKI = [i for i in range(1, 91)]
#print(BOCHONKI)

#Вытаскиваем случаный бочонок
current_bochonok = str(BOCHONKI.pop(random.randrange(len(BOCHONKI))))
print('Текущий номер бочонка', current_bochonok)
#print(BOCHONKI)


#a = '35'
# if a in card_max:
#     #print(np.unique(card_max == a, return_index=True))
#     print(np.where(card_max == a))
#     indexnum = np.where(card_max == a)
#     card_max[indexnum] = '-'+a+'-'
# print('Карта после вычеркивания')
# showcard(card_max)


def bochonoknum_is_in_card(card, current_bochonok):
    '''
    Проверяет есть ли номер бочонка в карте
    :param card: карта игрока (массив)
    :param bochonok: номер бочонка пробразованный в строку
    :return: True если есть
    '''
    # print(np.unique(card_max == a, return_index=True))
        #print(np.where(card_max == a))
    if current_bochonok in card:
        indexnum = np.where(card == current_bochonok)
        return indexnum

def cover_bochonoknum(card, current_bochonok):
    if current_bochonok in card:
        indexnum = bochonoknum_is_in_card(card, current_bochonok)
        card[indexnum] = '-'+current_bochonok+'-'
    return card

#проверяем цифру в карте
if bochonoknum_is_in_card(card_max, current_bochonok):
    print('есть в карте')


#зачеркиваем цифру
card_max = cover_bochonoknum(card_max, current_bochonok)
showcard(card_max)

#после каждого хода проверяем победителя
#если в массиве количество n = 27
#игра окончена, объявляем победителя

