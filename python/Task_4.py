# 4 Task
print("----------------------Task-4-----------------")
num = input("Число:")
i = 0
max_st = 0

while i != len(num):
    max_new = int(num[i])
    if max_new >= max_st:
        max_st = max_new
        i += 1
    else:
        i += 1
print(max_st)