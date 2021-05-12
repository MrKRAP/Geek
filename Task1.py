def delen(num_1, num_2):
    if num_1 and num_2 != 0:
        return num_1 / num_2
    else:
        return "Делить на ноль нельзя"


print(delen(int(input("Введите первое число:")), int(input("\nВведите второе число:"))))
