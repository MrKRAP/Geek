list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [
    el
    for el in list_1
    if list_1.count(el) == 1
]
print(new_list)