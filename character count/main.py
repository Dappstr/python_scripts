import pprint

# Will count the amount of characters in the message, storing them into a dictionary

message = "It was a bright cold day in April, and the clocks were striking thirteen"
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)