from random import randint

random_list = [randint(1,51) for i in range(13)]
print(random_list)

# sort the list first
sorted_list = sorted(random_list)
print("Sorted list:",sorted_list)

# binary search for a number
search_num = randint(1,51)
print("Searching for:",search_num)

left = 0 
right = len (sorted_list) - 1
found = False

while left <= right: 
    mid = (left + right)//2 # finding the middle 
    if sorted_list[mid] == search_num: 
        found = True
        print(search_num + " found at " + mid)
        break
    elif sorted_list[mid]< search_num: # deciding to go right or go left 
        left = mid + 1
    else:
        right = mid - 1
if not found: 
    print(str(search_num) + " not in the list")