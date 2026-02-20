from random import randint

random_list = [randint(1,51) for i in range(10)]
print(random_list)

max = random_list[0] #start with the first element
for num in random_list:
    if num > max:
        max = num
print("Maximum:",max)
