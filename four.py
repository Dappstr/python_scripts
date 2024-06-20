import random

#names = ["Lane, Dappster, John, Timothy, Other"]
#names.extend(["Tester", "Last"])

amount = input("Enter amount of random numbers to generate: ")

random_numbers = []
for i in range(int(amount)):
    num = random.randint(1,10)
    random_numbers.append(num)

#for i in random_numbers:
#    print(i)

print(" ".join(map(str, random_numbers)))

#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
#dirty_dozen = [fruits, vegetables]
# Will print Kale
#print(dirty_dozen[1][1])

animals = ["dog", "cat", "turtle"]

#.index will search for the given parameter in a list and return the index of where it is found
print(animals.index("cat"))

#it can also be restricted to search starting from N_1 to N_2
nums = [1, 3, 4, 2, 0, 5, 0, 3, 6, 8, 3, 7]

#this will print the first occurrence of the number 3 starting from index 2 to the length of the list
print(nums.index(3, 2, len(nums)))

