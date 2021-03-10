"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict

companies_number = int(input("Сколько компаний вы хотите добавить?: "))
companies = defaultdict(list)
average_profit = 0
max_company = []
min_company = []

for i in range(companies_number):
    companies_name = input(f"Введите название {i + 1} компании: ")
    for j in range(4):
        companies[companies_name].append(int(input(f"Введите прибыль {j + 1} квартал: ")))
    average_profit += sum(companies.get(companies_name)) / companies_number

for key in companies:
    if sum(companies.get(key)) >= average_profit:
        max_company.append(key)
    else:
        min_company.append(key)

print(f"Средняя прибыль предприятий: {average_profit}")
print(f"Предприятия с прибылью выше средней: {', '.join(max_company)}")
print(f"Предприятия с прибылью ниже средней: {', '.join(min_company)}")
