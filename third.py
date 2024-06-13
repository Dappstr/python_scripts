print("Your mission is to find the treasure.")
first_choice = input("left (l) or right (r)? ")
if first_choice == "r":
    print("Game over.")
else:
    second_choice = input("Swim (s) or wait (w)? ")
    if second_choice == "s":
        print("Game over.")
    else:
        third_choice = input("Which door? Red (r), Blue (b), or Yellow (y)? ")
        if third_choice == "r":
            print("Game over.")
        elif third_choice == "b":
            print("Game over.")
        else:
            print("You win! You found the treasure.")