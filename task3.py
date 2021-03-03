"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

number = int(input("Введите натуральное число: "))
number_2 = 0

while number > 0:
    digit = number % 10
    number = number // 10
    number_2 = number_2 * 10
    number_2 = number_2 + digit

print(f"Обратное число будет: {number_2} ")
