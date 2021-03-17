"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
from sys import getsizeof

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_number = numbers.index(max(numbers))
min_number = numbers.index(min(numbers))

print(f"Сгенерированный массив: \n{numbers}")

numbers[max_number], numbers[min_number] = numbers[min_number], numbers[max_number]

print(f"После смены мест максимального и минимального элемента : \n{numbers}")

memory_sum = [getsizeof(SIZE), getsizeof(MIN_ITEM), getsizeof(MAX_ITEM), getsizeof(max_number),
              getsizeof(min_number), getsizeof(numbers)]

print(f'Под переменные будет выделенно {sum(memory_sum)} памяти')
