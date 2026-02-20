from random import randint

random_list = [randint(1,51) for i in range(10)]
print(random_list)
random_search_num = randint(1,20)
print("random number to search for:", random_search_num)

found = False 
for number in random_list:
    if number == random_search_num:
        found = True
        break
if found: 
    print(str(random_search_num)+" is in the list")
else: 
    print(str(random_search_num)+" is not in the list")
comparisons = 0
found = False 
for number in random_list:
    comparisons += 1
    if number == random_search_num:
        found = True
        break
if found: 
    print(str(random_search_num),"is in the list")
else: 
    print(str(random_search_num),"is not in the list")

print("Number of comparisons made:",comparisons)