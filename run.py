from game import *

while True:
    print('Лото')
    print('Новая игра нажмте 1')
    print('Выход введите 0')

    choice = int(input('Выберите пункт меню: '))
    if choice == 1:
        game()
    elif choice == 0:
        loop = False
    else:
        print('Неверный пункт меню!')