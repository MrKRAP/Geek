class MyError(Exception):

    def __init__(self, text):
        self.text = text

list_1 = []
while True:

    user_input = input("Введите число:")

    if user_input == 'q':
        print(list_1)
        break
    try:
        if user_input.isnumeric() is False:
            raise MyError("Вы ввели не число")
        else:
            list_1.append(int(user_input))
    except ValueError:
        pass
    except MyError as err:
        print(err)


