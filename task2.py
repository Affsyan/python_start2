"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def calculation(def_n1):
    even_number = 0
    odd_number = 0
    for i in def_n1:
        if int(i) % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    return f"В числе {def_n1} Чётных чисел {even_number}, а нечетных {odd_number}"


number = input("Введите натуральное число: ")
print(calculation(number))
