"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""
import random


def sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item
    return array


number = 5
MIN_ITEM = 0
MAX_ITEM = 1000

numbers = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(2*number + 1)]
numbers1 = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(2*number + 1)]

print(f"Сгенерированный массив {numbers}")
sort_array = sort(numbers)
print(f"Отсортированный массив {sort_array}")
print(f"Медиана с сортировкой: {numbers[(len(sort_array))//2]}")

