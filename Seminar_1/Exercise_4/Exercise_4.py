#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, 
#что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#6 -> 1 4 1
#24 -> 4 16 4
#60 -> 10 40 10

qunt = int(input("Введите сколько журавликов сделали дети: "))

k = int(qunt * (2/3))
c = int(qunt * (0.5/3))
p = int(qunt * (0.5/3))

print(p, k, c)