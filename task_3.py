"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
from sys import getsizeof

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_min_numbers = sorted(numbers)
max_numbers = numbers.index(max_min_numbers[1])
min_numbers = numbers.index(max_min_numbers[0])

print(f"Сгенерированный массив: \n{numbers}")

numbers[max_numbers], numbers[min_numbers] = numbers[min_numbers], numbers[max_numbers]

print(f"После смены мест максимального и минимального элемента : \n{numbers}")

memory_sum = [getsizeof(SIZE), getsizeof(MIN_ITEM), getsizeof(MAX_ITEM), getsizeof(max_min_numbers),
              getsizeof(max_numbers), getsizeof(min_numbers), getsizeof(numbers)]

print(f'Под переменные будет выделенно {sum(memory_sum)} памяти')
