#Задача 6: Вы пользуетесь общественным транспортом? 
#Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером,
#где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.
#385916 -> yes
#123456 -> no

num_of_ticket = input("Введите номер вашего билета: ")

def lucky(num_of_ticket):
    if len(num_of_ticket) == 6:
        if (int(num_of_ticket[0]) + int(num_of_ticket[1]) + int(num_of_ticket[2])) \
        == (int(num_of_ticket[3]) + int(num_of_ticket[4]) + int(num_of_ticket[5])):
            print("Yes")
        else:
            print("No")
    else:
        print("Вы ввели не верный номер билета")

print(lucky(num_of_ticket))
