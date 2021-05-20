dict_1 ={}
with open('Task6.txt','r') as data:
    for el in data.read().split("\n"):
        # Проверка 2-го
        if el.split()[2][-4:] == "(пр)":
            num_1 = int(el.split()[2].replace('(пр)',''))
        else:
            num_1 = 0
        # Проверка 1-го
        if el.split()[1][-3:] == "(л)":
            num_2 = int(el.split()[1].replace('(л)',''))
        else:
            num_2 = 0
        # Проверка 3-го
        if el.split()[3][-4:] == "(лаб)":
            num_3 = int(el.split()[2].replace('(лаб)',''))
        else:
            num_3 = 0

        sum_hour = num_3+num_2+num_1

        dict_1['{}'.format(el.split()[0])] = sum_hour

print(dict_1)
