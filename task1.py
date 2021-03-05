"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

number = 2

while number != 9:
    count = 0
    number_list = 2
    while number_list != 99:
        if number_list % number == 0:
            count += 1
        number_list += 1
    print(f"Кратных чисел числу {number}: {count}")
    number += 1
