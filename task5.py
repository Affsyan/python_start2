"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100

numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f"Сгенерированный массив: \n{numbers}")

negative_number = []
max_number = 0

for i in numbers:
    if i < 0:
        negative_number.append(i)

max_number = negative_number[0]

for i in negative_number:
    if max_number < i:
        max_number = i

for i in range(len(numbers)):
    if max_number == numbers[i]:
        print(f"Максимальный отрицательный элемент в массиве {max_number} с индексом {i}")
