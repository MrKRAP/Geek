# a = "ffffff"
# print(a[0].upper()+a[1:])
list_1 = []
def int_func(str_1):
    if len(str_1.split()) == 1:
        print(str_1[0].upper()+str_1[1:])
    else:
        for el in str_1.split():
            # print(el[0].upper()+el[1:])
            list_1.append(el[0].upper()+el[1:])
        print(*list_1)

int_func("fffff")
int_func('wfwefwe wefweffe wefwefe ddd22222ddd')