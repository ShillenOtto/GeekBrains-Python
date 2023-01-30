#Задача 2: Найдите сумму цифр трехзначного числа.
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

num = int(input("Введите трехзначное число: "))


first = num // 100
second = num // 10 % 10
third = num % 10

print(first + second + third)