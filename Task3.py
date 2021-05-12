import heapq




def sum(nums):
    if len(nums) < 3:
        return "Нужно больше 3-х чисел!"
    else:
        return heapq.nlargest(2, nums)[0] + heapq.nlargest(2, nums)[1]


print(sum([
    int(input("Введите число 1:")),
    int(input("Введите число 2:")),
    int(input("Введите число 3:")),
]))


def my_func(num_1, num_2, num_3):
    if num_1 >= num_3 >= num_2 or num_3 >= num_1 >= num_2:
        return num_1 + num_3
    elif num_2 >= num_1 >= num_3 or num_1 >= num_2 >= num_3:
        return num_2 + num_1
    elif num_3 >= num_2 >= num_1 or num_2 >= num_3 >= num_1:
        return num_3 + num_2


print("--"*40)
print("Вариант как в дз")
print("--"*40)

print(my_func(
    int(input("Введите число 1:")),
    int(input("Введите число 2:")),
    int(input("Введите число 3:")),
))

