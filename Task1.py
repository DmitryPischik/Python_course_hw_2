# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input("Введите количество монет: "))
coins = []
for i in range(n):
    coins.append(random.randint(0, 1))
print(coins)
heads = coins.count(1)
tails = n - heads
if heads < tails:
    print(heads)
else:
    print(tails)
