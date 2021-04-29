# 2 Task
print("----------------------Task-2-----------------")
time = input("Enter time in seconds:")
h = int(time)//3600
time_2 = int(time) - h*3600
m =  time_2//60
time_3 = time_2 - m*60

print("{}h:{}m:{}s".format(h,m,time_3))