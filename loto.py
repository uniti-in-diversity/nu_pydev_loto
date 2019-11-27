import numpy as np

def add_separators(f):
    def inner(*args, **kwargs):
        print ('=' * 25)
        result = f(*args, **kwargs)
        print('=' * 25)
        return result
    return inner

def create_card():
    '''
    Генерация рандом массива 3 на 5 с заполнением случаными чилами от 1 до 90
    Генерация нулевого массива 3 на 4
    Конкатенация массивов по столбцам (axis = 1)
    Переемешиваем эелементы массива случайным образов в рамках каждой строки
    :return: Массив 3 на 9, 5 элементов из 9 в каждой строке случайные числа, о
    стальные элементы 0. Тип элементов строка.
    '''
    nums = np.random.randint(1, 90, size=(3, 5))
    nums = nums.astype('str')
    zero = np.zeros((3, 4), int)
    zero = zero.astype('str')
    array = np.concatenate([nums, zero], axis = 1)
    #далее перемешиваем в каждой строке элементы случайным образом
    x, y = array.shape
    rows = np.indices((x, y))[0]
    cols = [np.random.permutation(y) for _ in range(x)]
    return array[rows, cols]

#Отобразить карточку
@add_separators
def showcard(card):
    '''
    Печатает массив в виде игровой карточки лото, нули заменяются пустыми строками (одиночными пробелами)
    :param card: массив элементов
    :return:
    '''
    for i in card:
        lineforprint = (' '.join(map(str, i.ravel())))
        print(lineforprint.replace('0', ' '))

c = create_card()
showcard(c)


