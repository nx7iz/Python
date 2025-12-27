# variables exercise
# 1. The Tip Calculator

bill = float(input("Enter the total bill amount: "))
tip = int(input("Enter the percentage of bill you want to give: "))
person = int(input("Total person eating: "))

bill += bill * (tip / 100)
print(bill)
per_head = bill / person

print(F"Each person should pay ${per_head:.2f}")
