# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во первого множества: "))
m = int(input("Введите кол-во второго множества: "))

set_one = set((input(f"Введите {n} элемента/ов для первого множества: ")).split())
set_two = set((input(f"Введите {m} элемента/ов для первого множества: ")).split())
union = sorted(list(set_one.union(set_two)))

print(union)