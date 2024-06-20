#split() will split a string into a list where each word is an item
#heights = input("Enter heights: ").split()
#total_heights = 0
#for n in range(0, len(heights)):
#    total_heights += int(heights[n])

#print("Total height: " + str(total_heights))

scores = input("Enter scores: ").split()
for n in range(len(scores)):
    scores[n] = int(scores[n])
print("Max score: " + str(max(scores)))

#Like in many other languages, you can modify the step with a third argument
#for number in range(1, 11, 3): #Will start with 1, then go up by 3 each iteration
#    print(number)

#FizzBuzz
target = int(input("Enter a number to fizzbuzz: "))
for i in range(1, target):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)