import json


# Я сделал авто добавление по категориям
#

# Класс склад
class Storage:
    all_product = {'category': {}}

    def __init__(self, m):
        self.sqrt_m = m
        # print(f"Помещение {m} квадратных метров")

    @staticmethod
    def count(category):
        count_product = len(Storage.all_product['category'][f'{category}'])
        print(f'{count_product} - количество товаров категории - {category}')


# mother class
class OfficeEq:
    office_eq = {}

    def __init__(self, id_item, price, name, category, date, producer):
        self.office_eq[f'{id_item}'] = {}
        self.office_eq[f'{id_item}']['name'] = name
        self.office_eq[f'{id_item}']['price'] = price
        self.office_eq[f'{id_item}']['category'] = category
        self.office_eq[f'{id_item}']['date'] = date
        self.office_eq[f'{id_item}']['color'] = producer

        Storage.all_product['category'][f'{category}'] = {}
        key = [key for key in Storage.all_product['category']]

        self.addDict()
        # for el in key:
        #
        #     if el == self.office_eq[f'{id_item}']['category']:
        #         Storage.all_product['category'][f'{category}'][f'{id_item}'] = self.office_eq[f'{id_item}']
        #     print("--------"*10)

    def addDict(self):
        key = [key for key in Storage.all_product['category']]
        idItem = [_ for _ in self.office_eq]

        for el in idItem:
            for k in key:
                if k == self.office_eq[f'{el}']['category']:
                    Storage.all_product['category'][f'{k}'][f'{el}'] = self.office_eq[f'{el}']


class Printer(OfficeEq):

    def __init__(self, id_item, price, name, category, date, color, producer, paper):
        OfficeEq.__init__(self, id_item, price, name, category, date, producer)
        self.office_eq[f'{id_item}']['paper'] = paper
        self.office_eq[f'{id_item}']['color'] = color


class PC(OfficeEq):

    def __init__(self, id_item, price, name, category, date, producer, monitor, keyboard, mouse):
        OfficeEq.__init__(self, id_item, price, name, category, date, producer)
        self.office_eq[f'{id_item}']['monitor'] = monitor
        self.office_eq[f'{id_item}']['keyboard'] = keyboard
        self.office_eq[f'{id_item}']['mouse'] = mouse


hp = Printer(1234123332, 10000, 'hp3456', 'printer', '21-12-12', 'black-color-only', 'hp', 'A1-A4')
hp_new = Printer(1123, 3443344, 'hp44556', 'printer', '21-12-12', 'black-color-only', 'hp', 'A1-A4')
pc_1 = PC(4455666, 100000, 'HyperPC-UltraQiwi', 'PC', '21-05-21', 'HyperPC', False, True, True)
pc_2 = PC(4455667, 100000, 'HyperPC-UltraQiwi', 'PC', '21-05-21', 'HyperPC', False, True, True)

print(json.dumps(Storage.all_product, indent=4))
print(Storage.count('printer'))
