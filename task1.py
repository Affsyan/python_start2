"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
"""


def test(a, i=1, str_hash=None):
    if len(a) == 0:
        return print("Пустая строка")
    if str_hash is None:
        str_hash = []
    for x in range(0, len(a), 1):
        if hash(a[x:x + i]) not in str_hash:
            str_hash.append(hash(a[x:x + i]))
    i += 1
    if i == len(a):
        return print(f'Количество подстрок в строке {a} равно:{len(str_hash)}')
    return test(a, i, str_hash)


test(input("Введите строку: "))
