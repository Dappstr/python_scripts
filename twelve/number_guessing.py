import random
NUM = random.randint(0, 100)

print("Welcome to the number guessing game!")

num_guesses = 0
diff_choice = input("Choose a difficulty. Type \'easy\' or \'hard\': ")

if diff_choice == "easy":
    num_guesses = 10
elif diff_choice == "hard":
    num_guesses = 5

while num_guesses > 0:
    guess = int(input("Enter a number: "))
    if guess == NUM:
        print("You win!")
    else:
        if guess > NUM:
            print("Too high")
        else:
            print("Too low")
        num_guesses -= 1

if num_guesses < 1:
    print(f"You lose! The number was {NUM}")
