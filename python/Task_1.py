# 1 Task
print("----------------------Task-1-----------------")
var = 1
var_2  = 2
print("Первая переменная {} \nВторая переменная {}".format(var, var_2))

name = input("В терминале напишите свое имя:")
print("Вы уверены что это ваше имя?",name)
ans = input("Введите Да , если это ваше имя")

if ans == "Да":
    print("Отлично",name)
else:
    print("Повтори попытку ввода")
    name = input("В терминале напишите свое имя:")
# Я ЗАЛИНИЛСЯ ПИСАТЬ ФУНКЦИЮ ТАК ЧТО КАК ЕСТЬ))))