print("Welcome to the secret auction program.")

bidders = {}

keep_going = True
while keep_going:
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: "))
    bidders[name] = bid
    cont = input("Any other bidders? Type \'yes\' or \'no\: '").lower()
    if cont == "no":
        keep_going = False

highest_bidder = []
highest_bid = int(0)
for bidder in bidders:
    if bidders.get(bidder) > highest_bid:
        highest_bid = bidders.get(bidder)
        highest_bidder = bidder
highest_bidder_str = ''.join(highest_bidder)

print(f"The highest bidder is: {highest_bidder_str} with ${highest_bid}")