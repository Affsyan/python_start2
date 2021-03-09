"""
Задание 4 из урока 2.
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
https://docs.google.com/spreadsheets/d/1z2b2mDUj8vwiH9p359TSL0AmwK9fdVf44H_Zqdv02oc/edit?usp=sharing
"""

import timeit
import cProfile

n = 500


def calculation_rec(def_n_rec):
    if def_n_rec == 1:
        return 1
    else:
        return 1 + (-0.5) * calculation_rec(def_n_rec - 1)


"""
         503 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    500/1    0.000    0.000    0.000    0.000 task1.py:11(calculation_rec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def calculation_cycle(def_n_cycle):
    sum_ = 0
    for i_cycle in range(def_n_cycle):
        sum_ = sum_ + ((-0.5) ** i_cycle)
    return sum_


"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1.py:18(calculation_cycle)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def calculation_cycle_sum(def_n_cycle):
    sum_ = []
    for i_cycle_sum in range(def_n_cycle):
        sum_.append(((-0.5) ** i_cycle_sum))
    return sum(sum_)


"""
505 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1.py:25(calculation_cycle_sum)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


"""
for i in range(1, n, 5):
    print(timeit.timeit('calculation_rec(i)', number=10000, globals=globals()))
    print(timeit.timeit('calculation_cycle(i)', number=10000, globals=globals()))
    print(timeit.timeit('calculation_cycle_sum(i)', number=10000, globals=globals()))
"""
"""
cProfile.run('calculation_rec(n)')
cProfile.run('calculation_cycle(n)')
cProfile.run('calculation_cycle_sum(n)')
"""

