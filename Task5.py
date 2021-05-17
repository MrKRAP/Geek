from functools import reduce
def generator():
    list_1 = [
        el
        for el in range(99,1001)
        if el % 2 == 0
    ]
    return list_1

result = reduce(lambda x,y : x*y ,generator())

print(result)