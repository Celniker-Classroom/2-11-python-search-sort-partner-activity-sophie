from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


random_nums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    random_nums.append(randint(1,51)) #this adds a random number between 1-50 to the list


print(random_nums) #print the list!