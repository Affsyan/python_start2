"""
 Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""


def calculation(def_n):
    if def_n == 1:
        return 1
    else:
        return 1 + (-0.5) * calculation(def_n - 1)


n = int(input("Введите число НЕ БОЛЬШЕ 998!: "))
print(calculation(n))
