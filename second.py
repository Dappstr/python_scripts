#age = input("Enter your age: ")
#years = 90 - int(age)
#There are 52 weeks in a year
#weeks = years * 52
#print(f"You're {age} and you have roughly {weeks} weeks left to live.")

total = float(input("Enter the total bill: $"))
tip = int(input("How much would you like to tip? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))
total_tip = (tip / 100) * total
total_per_person = float((total + total_tip) / people)
print(f"Each person will pay: ${total_per_person}")