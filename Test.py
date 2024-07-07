from random import randint
import time
name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ')
num1 = input('Введите число первого игрока: ')
num2 = input('Введите число второго игрока: ')
a = randint(1, 6)
time.sleep(3)
if num1 == a:
    print('Победил', name1)
elif num2 == a:
    print('Победил', name2)
else:
    print('Ничья')
