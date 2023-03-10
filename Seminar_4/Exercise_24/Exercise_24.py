# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

quantiti_of_bushes = int(input("Введите кол-во высаженных кустов: "))
mass = list(int(input(f"Введите сколько на {num} кусте ягод: ")) for num in range(1, quantiti_of_bushes + 1))
count_of_berry = list()

for i in range(len(mass) - 1):
    count_of_berry.append(mass[i - 1] + mass[i] + mass[i + 1])
count_of_berry.append(mass[0] + mass[-1] + mass[-2])
print(f"Максимальное кол-во ягод с трех кустов составляет: {max(count_of_berry)}")