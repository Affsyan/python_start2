"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f"Сгенерированный массив: \n{numbers}")
element_index = 0
count = 0
count_max = 0
element_max = 0
count_while = 0

while count_while != SIZE:
    for i in range(len(numbers)):
        if numbers[element_index] == numbers[i]:
            count += 1
        if count_max < count:
            count_max = count
            element_max = numbers[element_index]
    count = 0
    element_index += 1
    count_while += 1

print(f"Число {element_max} встречается в массиве {count_max} раз(а).")
