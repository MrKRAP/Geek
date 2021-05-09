user_input = input("Введите слова через пробел")
for num,el in enumerate(user_input.split()):
    if len(el)>11:
        print(num,el[0:11])
    else:
        print(num, el)