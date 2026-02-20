from random import randint

random_list = [randint(1,51) for i in range(10)]
print(random_list)

max_cnt = 0
mode = None
for number in random_list:
    count = random_list.count(number)
    if count > max_cnt:
        max_cnt = count
        mode = number

# check if a mode exist
if max_cnt > 1:
    print("Mode", mode)

else: 
    print("There is no mode")
