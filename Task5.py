my_list = [7, 5, 3, 3, 2]
user_input = int(input("Введите число"))

for num, el in enumerate(my_list):
    if user_input > el:
        my_list.insert(num, user_input)
        break
    elif user_input == el:
        my_list.insert(num, user_input)
        break
    elif my_list[len(my_list)-1] > user_input:
        my_list.append(user_input)
        break
print(my_list)