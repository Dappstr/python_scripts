import random
#def add(a, b):
#    return a + b
#print(add(5, 10))

def get_guess(num):
    guess = int(input("Enter a guess: "))
    if guess > num:
        print("Number was too high.")
    elif guess < num:
        print("Number was too low.")
    return guess

num = random.randint(1, 10)
guess = int(0)
while guess != num:
    guess = get_guess(num)