count = int(input("Введите максимальное количество значений которые будут введены"))
a = input("Введите любые значения:\n Для завершения ввода напишите exit")
a = list(a)
while len(a) < count:
    a.append(input("Введите любые значения:\n Для завершения ввода напишите exit\n"))
    if a[-1] == "exit":
        a.remove('exit')
        break
new_list = []
num = 0
# print(len(a))
for el in a:
    # print(num)
    if num+1 == len(a):
        new_list.append(a[num])
        break
    elif num == len(a):
        break
    else:
        new_list.append(a[num + 1])
        new_list.append((a[num]))
        num += 2
print(new_list)
print(a)

# for num,el in enumerate(a):
#     while num < len(a):
#         a.insert(num,a[num+1])
# print("----------------")
# print(a)