"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict
from collections import deque


def calculation(n1_n2):
    n1_n2.reverse()
    for i in range(len(n1_n2)):
        if n1_n2[i] // 16 != 0:
            if i + 1 >= len(n1_n2):
                n1_n2.append(0)
            n1_n2[i + 1] = n1_n2[i + 1] + n1_n2[i] // 16
            n1_n2[i] = n1_n2[i] % 16
    n1_n2.reverse()

    for index in range(len(n1_n2)):
        n1_n2[index] = number_value.get(n1_n2[index])

    return n1_n2


number = defaultdict(int)
number_value = defaultdict(int)
for counter, value in enumerate("0123456789ABCDEF"):
    number[value] = counter
    number_value[counter] = value

n_1 = list(input("Введите 1вое число в шестнадцатеричной системе счисления: ").upper())
n_2 = list(input("Введите 2рое число в шестнадцатеричной системе счисления: ").upper())

n_len = len(n_1) - len(n_2)
if n_len < 0:
    n_1 = ["0"] * abs(n_len) + n_1
else:
    n_2 = ["0"] * abs(n_len) + n_2

for i in range(len(n_1)):
    n_1[i] = number.get(n_1[i])
    n_2[i] = number.get(n_2[i])


n1_n2_sum = deque([x + y for x, y in zip(n_1, n_2)])

print("".join(calculation(n1_n2_sum)))


