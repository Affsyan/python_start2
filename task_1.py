"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

import random


def bubble(array):
    j = len(array)
    count = 1
    while count < len(array):
        for i in range(0, j - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        j -= 1
        count += 1
    return array


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f"Сгенерированный массив {numbers}")

print(f"Отсортированный массив {bubble(numbers)}")
