class Data:

    @classmethod
    def data(cls, date):
        int_date = [int(el) for el in date.split('-')]

        return print(cls.validate(int_date))

    @staticmethod
    def validate(date):
        if 0 < date[0] <= 31 and ((0 < date[1] <= 7 and date[1] % 2 == 1) or (7 < date[1] <= 12 and date[1] % 2 == 0 )):
            return date
        elif date[1] % 2 == 0 and 0 < date[0] <= 30:
            return date
        elif date[1] == 2 and date[0] >= 28:
            return "В феврале не может быть больше 28 дней (проверку на весокосный лень)))))"
        else:
            return "Ошибка при вводе даты"


Data.data("31-12-2000")

