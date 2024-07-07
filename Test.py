from random import randint
import time
num1 = input()
num2 = input()
a = randint(1, 6)
time.sleep(3)
if num1 == a:
    print('Победил первый игрок')
elif num2 == a:
    print('Победил второй игрок')
else:
    print('Ничья')
