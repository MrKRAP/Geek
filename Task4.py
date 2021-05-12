def my_func(x, y):
    xy = x
    if y == 0:
        return "Нужно ввести число меньше нуля"
    if y == -1:
        return 1 / x
    else:
        while y != -1:
            xy *= x
            y += 1
        return 1 / xy


print(my_func(int(input("Введите первое число:")), int(input("Введите второе число:"))))
