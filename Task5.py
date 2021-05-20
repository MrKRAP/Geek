
with open('task5.txt','w+') as data:
    data.write((input("Введите числа через пробел:")))
    data.seek(0)
    all_sum = sum(
        [int(el) for el in data.read().split()]
    )

print(all_sum)