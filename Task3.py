class Worker:
    _dict_1 = {
        'economist': {
            'wage': 50000,
            'bonus': 12000
        },
        'SMM': {
            'wage': 30000,
            'bonus': 10000
        }
    }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        try:
            self.income = sum([el for el in self._dict_1[position].values()])
        except KeyError:
            print("Такой позиции нет")
            self.income = "Такой позиции нет"


# w= Worker("m",'d','SMM')

class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя {self.name} {self.surname}")

    def get_full_income(self):
        print(self.income)


econ = Position('M','A','econ')
econ.get_full_name()
econ.get_full_income()
