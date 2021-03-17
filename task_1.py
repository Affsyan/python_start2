"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
Под переменные будет выделенно 376 памяти. Разрядность os 64  интерпретатор 3.8
"""

import random
from sys import getsizeof

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_number = numbers[0]
min_number = numbers[0]

min_number_index = 0
max_number_index = 0

print(f"Сгенерированный массив: \n{numbers}")

for i in range(len(numbers)):
    if max_number < numbers[i]:
        max_number = numbers[i]
        max_number_index = i
    if min_number > numbers[i]:
        min_number = numbers[i]
        min_number_index = i

print(f"Максимальное число {max_number} с индексом {max_number_index}")
print(f"Минимальное число {min_number} с индексом {min_number_index}")

numbers[max_number_index], numbers[min_number_index] = numbers[min_number_index], numbers[max_number_index]

print(f"После смены мест максимального и минимального элемента : \n{numbers}")

memory_sum = [getsizeof(SIZE), getsizeof(MIN_ITEM), getsizeof(MAX_ITEM), getsizeof(max_number), getsizeof(min_number),
              getsizeof(min_number_index), getsizeof(max_number_index), getsizeof(numbers)]
print(f'Под переменные будет выделенно {sum(memory_sum)} памяти')
