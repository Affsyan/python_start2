"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
https://drive.google.com/file/d/1bjoGh1HeEYN8-OR9f3lqaLlECameAAhA/view?usp=sharing
"""


def check_number(number):
    try:
        float(number)
        return False
    except ValueError:
        return True


def number_one():
    def_n1 = input("Введите число: ")
    while True:
        if check_number(def_n1):
            def_n1 = input("Введите число: ")
        else:
            break
    return float(def_n1)


def symbol():
    s = input("Введите знак (+ - * /). Для выхода введите 0: ")
    while True:
        if s == '0':
            return 'Exit'
        else:
            if s in '+-*/':
                return s
            else:
                s = input("Введите знак (+ - * /). Для выхода введите 0: ")


def number_two(sign_def):
    def_n2 = input("Введите число: ")
    while True:
        if def_n2 == '0' and sign_def == '/':
            print("Невозможно поделить на 0!")
            def_n2 = input("Введите другое число: ")
        else:
            if check_number(def_n2):
                def_n2 = input("Введите число: ")
            else:
                break
    return float(def_n2)


def calculation(def_n1, def_symbol, def_n2):
    if def_symbol == '+':
        return def_n1 + def_n2
    elif def_symbol == '-':
        return def_n1 - def_n2
    elif def_symbol == '*':
        return def_n1 * def_n2
    else:
        return def_n1 / def_n2


while True:
    n1 = number_one()
    sign = symbol()
    if sign == 'Exit':
        print("Программа завершена")
        break
    else:
        n2 = number_two(sign)
        answer = calculation(n1, sign, n2)
    print(f"{n1} {sign} {n2} = {answer}")

