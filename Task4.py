import os

with open('task4_ru.txt','w') as data_ru:
    with open('task4.txt','r') as data:
        list_1 = [el.split() for el in data]
        print(list_1)
        for el in list_1:
            print(el[0])
            if el[0] == 'One':
                data_ru.write('Один - 1\n')
            if el[0] == 'Two':
                data_ru.write('Два - 2\n')
            if el[0] == 'Three':
                data_ru.write('Три - 3\n')
            if el[0] == 'Four':
                data_ru.write('Четыре - 4\n')

# os.remove('task4_ru.txt')

