season_dict = {
    "Февраль": "зима",
    "Декабрь": "зима",
    "Январь": "зима",
    "Сентябрь": "осень",
    "Октябрь": "осень",
    "Ноябрь": "осень",
    'Июнь': "лето",
    "Июль": "лето",
    "Август": "лето",
    "Март": "весна",
    "Апрель": "весна",
    "Май": "весна"
}

user_input = input("Введите месяц на русском и с Большой буквы!\n")

for el in season_dict.keys():
    if user_input == el:
        print(season_dict.get(el,"Такого месяца нет"))

season_list = ["Декабрь", "Январь", "Февраль",
               "Март", "Апрель", "Май",
               "Июнь", "Июль", "Август",
               "Сентябрь", 'Октябрь', 'Ноябрь']
for num, el in enumerate(season_list):
    if num < 3 and el == user_input:
        print("Зима")
    if 2 < num < 6 and el == user_input:
        print("Весна")
    if 5 < num < 9 and el == user_input:
        print("Лето")
    if 8 < num < 12 and el == user_input:
        print("Осень")

