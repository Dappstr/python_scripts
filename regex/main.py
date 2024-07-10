import re

#Without regular expressions
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(is_phone_number("503-333,3333"))

message = "Call me 123-456-7890 tomorrow, or at 098-765-4321 for my office line"
phone_num_regex = re.compile(r'''
                             \d\d\d     # Area code
                             -          # First dash
                             \d\d\d     # Middle part of phone number
                             -          # Second dash
                             \d\d\d\d   # Last part of phone number'''
                             , re.VERBOSE) # Raw string, looking for 3 digits then a dash, then 3 more digits, then dash, then last 4 digits
print(phone_num_regex.findall(message))

phone_num_formatted_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_formatted_regex.search(message)
print(mo.group(1)) # Will print the first group within the parentheses

# You can use the pipe operator to match one of several patterns
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
print(bat_regex.findall("Batman lost a wheel in his Batmobile"))

bat_regex2 = re.compile(r'Bat(wo)?man') # '?' tells the interpreter that `wo` may appear 1 or 0 times
bwm = bat_regex2.search("The adventures of Batwoman")
print(bwm.group())

ha_regex = re.compile(r"ha")
ha = ha_regex.findall("He went hahahaha")
print(len(ha)) # Will print the amount of times `ha` occurs

# \D is for any character that is not a numeric digit from 0 to 9
# \w is for any letter, numeric digit, or underscore character

other = re.compile(r'[^aeiou]') # The carrot symbol means any character that is NOT within the group
print(other.findall("This is a very long string that is being searched"))

names_regex = re.compile(r'Agent \w+')
names_regex.findall("Agent Mulder gave the secret documents to Agent Scully")
print(names_regex.sub('REDACTED', "Agent Mulder gave the secret documents to Agent Scully"))