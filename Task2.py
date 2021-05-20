nums_str = 0
with open("task2.txt",'r') as task:
    print(task.read())
    print("-------------------"*10)
    task.seek(0)
    for el in task:
        print(el)
        nums_str += 1
        list_1 = el.split()
        print(len(list_1))

print('Количество строк:',nums_str)