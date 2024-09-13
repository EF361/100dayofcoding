print("Welcome to the Tip Calculator!\n")

#ask for the total bill
bill = float(input("What was the total bill?\n$"))

#ask for the tip
tip = float(input("How much percentage of tips would you like to give? 10, 12, or 15?\n"))

#ask for the total number of people 
people = int(input("How many people to split the bill?\n"))

#break a line for easy to read
print("\n")

#calculation
tip = bill * (tip/100)
payPerPerson = round((bill + tip) / people,2)

#print the output
print(f"Each person should pay: ${payPerPerson}")
