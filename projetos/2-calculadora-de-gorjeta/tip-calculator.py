# Day 2 Project – Tip calculator

print("### Tip Calculator ###")

bill = float(input("What was the total bill?\n-> $"))
tip = int(input("What percentage tip would you like to give? (Answer with numbers only)\n-> "))
bill_splitters = int(input("And how many people are splitting the bill?\n-> "))

# total = (bill * ((tip / 100) + 1))
total = (((tip / 100) * bill) + bill)
# print(total)
share = round((total / bill_splitters), 2)

# print(f"Each person should pay ${share}")
print("Each person should pay $%.2f" %(share))
