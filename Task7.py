from statistics import mean
import json

dict_1 ={}
dict_2 = {}
list_1 =[]
with open('Task7.txt','r') as data:
    for el in data.read().split('\n'):
        d = int(el.split()[2]) - int(el.split()[3])
        list_1.append(d)
        if d > 0:
            dict_1['{}'.format(el.split()[0])] = d

dict_2['average_profit'] = mean(list_1)
print(dict_1)
list_3 = [dict_1,dict_2]

with open('Task7_new.json','w') as data:
    json.dump(list_3,data)
