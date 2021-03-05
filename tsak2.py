"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

SIZE = 50
MIN_ITEM = 0
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
numbers_index = []

print(f"Сгенерированный массив: \n{numbers}")
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers_index.append(i)
print(f"Четные элементы массива имеют индексы: \n{numbers_index}")