# 5 task
print("----------------------Task-5-----------------")
income = int(input("Income:"))
costs = int(input("Costs:"))

results = income - costs

if results < 0:
    print("Издержки больше прибыли")
else:
    print("Выручка больше чем издержки")
    emp = int(input("Enter quantity of employee:"))
    rent = results / income
    print("Рентабельность фирмы:", rent)
    print("Выручка на сотрудника:", results / emp)