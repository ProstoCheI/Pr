from random import randint
import time
num1 = input('Введите число первого игрока: ')
num2 = input('Введите число второго игрока: ')
a = randint(1, 6)
time.sleep(3)
if num1 == num2:
    print('Введите разные числа')
elif num1 == a:
    print('Победил первый игрок')
elif num2 == a:
    print('Победил второй игрок')
else:
    print('Ничья')
