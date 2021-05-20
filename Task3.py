from statistics import  mean


with open('task3.txt','r') as data:
    # print(data.read().split())
    who_min = [el.split()[0] for el in data.read().split('\n') if int(el.split()[1]) < 20000 ]
    data.seek(0)
    mean_1 = mean([int(el.split()[1]) for el in data.read().split('\n')])

print('Зарплата меньше 20000 :', *who_min)
print(mean_1)