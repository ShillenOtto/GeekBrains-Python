#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#n = 5
#1 2 3 4 5
#x = 6
#-> 5
n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число,к которому хотите найти самый близкий по величине элемент: "))
new_list = list()
dif = 10**9
for i in range(1,n+1):
    a = int(input(f"Введите элемент списка №{i}: "))
    new_list.append(a)
print(f"Ваш массив: {new_list}")

for i in new_list:
    j = abs(i - x)
    if j < dif:
        dif = j
        num = i
print(f"Самый близкий к {x} по величине элемент: {num}")