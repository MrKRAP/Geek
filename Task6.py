count = int(input("Количество товаров:\n"))
list_all = []
list_name = []
list_price = []
list_q = []
list_ed = []
id_num = 1
while count != 0:
    dict_id = {"название": input("Введите название"),
               "цена": int(input("Введите цену")),
               "количество": int(input("Введите количество")),
               "eд": input("Введите eд")
               }
    no_list = (id_num, dict_id)
    list_all.append(no_list)
    id_num += 1
    count -= 1

print(list_all[0][1]["название"])
for num, el in enumerate(list_all):
    list_name.append(list_all[num][1]["название"])
    list_price.append(list_all[num][1]["цена"])
    list_q.append(list_all[num][1]["количество"])
    list_ed.append(list_all[num][1]["eд"])

dict_stat = {
    'название': list_name,
    'цена': list_price,
    'количестов': list_q,
    'ед': list_ed
}

print(dict_stat)
