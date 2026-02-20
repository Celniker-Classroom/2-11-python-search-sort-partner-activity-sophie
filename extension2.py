from random import randint

random_list = [randint(1,51) for i in range(13)]
print(random_list)

for i in range(len(random_list)):
    for j in range(len(random_list)-1 - i): # swapping positions
        if random_list[j] > random_list[j+1]:
            random_list[j], random_list[j+1]= random_list[j+1],random_list[j]
print ("sorted list:", random_list)
