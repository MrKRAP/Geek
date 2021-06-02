class MyError(Exception):
    def __init__(self, text):
        self.text = text


while True:

    num_1 = input('Введите первое число:')
    num_2 = input('Введите второе число:')

    try:
        if int(num_2) == 0:
            raise MyError('Вы ввели 0, на него делить нельзя')
    except ValueError:
        print('Вы ввели не число')
    except MyError as err:
        print(err)
    else:
        print(f'Ответ {int(num_1) / int(num_2)}')

    if (num_1 or num_2) == 'q':
        break
