list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [list_1[num] for num, el in enumerate(list_1) if el > list_1[num-1]]

print(new_list)
