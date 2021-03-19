"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random


def sort(array):
    if len(array) == 1:
        return array
    average = len(array) // 2
    left = sort(array[:average])
    right = sort(array[average:])
    return merge(left, right)


def merge(left, right):
    sorted_ = []
    index_l = index_r = 0

    length_l, length_r = len(left), len(right)

    for _ in range(length_l + length_r):
        if index_l < length_l and index_r < length_r:

            if left[index_l] <= right[index_r]:
                sorted_.append(left[index_l])
                index_l += 1

            else:
                sorted_.append(right[index_r])
                index_r += 1

        elif index_l == length_l:
            sorted_.append(right[index_r])
            index_r += 1

        else:
            sorted_.append(left[index_l])
            index_l += 1

    return sorted_


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49

numbers = [float(random.randrange(MIN_ITEM, MAX_ITEM)) for _ in range(SIZE)]

print(f"Сгенерированный массив {numbers}")

print(f"Отсортированный массив {sort(numbers)}")
