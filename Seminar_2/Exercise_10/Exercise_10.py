#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.
#5 -> 1 0 1 1 0
#2
import random


n = int(input("Введите кол-во монеток: "))
coins = []
one = 0
zero = 0
for i in range(n):
    coin = random.randrange(0, 2, 1)
    coins.append(coin)
print(f"У нас получилось:{coins}")

for j in range(0, len(coins)):
    if coins[j] == 1:
        one += 1
    else:
        zero += 1
if one > zero:
    print(f"Необходимо перевернуть {zero} монеток!")
else:
    print(f"Необходимо перевернуть {one} монеток!")