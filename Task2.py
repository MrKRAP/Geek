import re
user = []

def user_information(name,surname,year,city,email,phone):
    user.append(name)
    user.append(surname)
    user.append(year)
    user.append(city)
    user.append(email)
    user.append(phone)
    return user

print(*user_information(
    input("Введите имя:"),
    input("Введите фамилию:"),
    input("Введите год рождения:"),
    input("Введите город постоянного проживания:"),
    input("Введите адрес электронной почты:"),
    input("Введите номер телефона:")
))


# # Validation
# def validTel(text):
#     if not re.findall(r"\+7", text):
#         msg = 'Нужно указать телефон'
#         return msg
#
#     if len(text) > 20:
#         msg = 'Слишком много символов!'
#         return msg
#
#     else:
#         msg = 'Всё отлично!'
#         return msg
#
#
# def validMail(text):
#     if not re.findall(r"\@", text):
#         msg = 'Нужно указать почту с @'
#         return msg
#
#     else:
#         msg = 'Всё отлично!'
#         return msg

