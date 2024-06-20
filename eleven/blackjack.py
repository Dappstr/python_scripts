#Possible todo: add in removing a card from the deck

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
first_card = cards[random.randint(0, 13)]
second_card = cards[random.randint(0, 13)]

player_cards.append(first_card)
player_cards.append(second_card)

print(f"Your cards: [{first_card}, {second_card}], current score: {first_card + second_card}")

computer_cards.append(cards[random.randint(0, 13)])
print(f"Computer\'s first card: {computer_cards[0]}")
choice = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()

if choice == 'y':
    computer_cards.append(cards[random.randint(0, 13)])
    player_cards.append(cards[random.randint(0, 13)])
    print(f"Your hand: {player_cards}, total: {sum(player_cards)}")
    print(f"Computer\'s cards: {computer_cards}")
    if sum(player_cards) > 21:
           print("You bust! Game over.")
    else:
        choice = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()
        while choice == 'y':
            player_cards.append(cards[random.randint(0, 13)])
            print(f"Your hand: {player_cards}, total: {sum(player_cards)}")
            if(sum(player_cards) > 21):
                 print("You bust! Game over!")
                 break
            else:
                choice = input("Type \'y\' to get another card, type \'n\' to pass: ").lower()

else:
     print("Game over.")
if sum(player_cards) <= 21:
     print("You win!")