import json
from pcpartpicker import API

api = API()

# f = open('file.txt','r')
# content = f.read()
# print(content)
# f.close()

# gpu_data = api.retrieve('video-card')
# gpu_data.to_json()
# with open('gpu_data.json','w') as gpu_json:
#     json.dump(gpu_data.to_json(),gpu_json)

with open('task1.txt','w') as file_in:
    while True:
        a = input("Для окончания записи отправьте пустую строку:")
        if a != '':
            file_in.write(a)
        else:
            break


