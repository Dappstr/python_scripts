from hangman_words import word_list
import random

word = random.choice(word_list)
lives = 6
display = []

for char in range(len(word)):
    display += '_'

print(display)

game_over = False

while game_over != True:
    print("Lives: " + str(lives))
    if lives == 0:
        print(f"Game over. The word was \"{word}\"")
        game_over = True
    else:
        guess = input("Enter a character: ").lower()
        
        if len(guess) > 1:
            print("You must enter only one character")
        else:
            if guess in display:
                print("You've already guessed that")
            else:
                if guess in word:
                    for i in range(0, len(word)):
                        if word[i] == guess:
                            display[i] = guess
                    print(display)
                    if '_' not in display:
                        print("You win!")
                        game_over = True
                else:
                    lives -= 1

