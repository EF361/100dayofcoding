# Which year do you want to check?
year = int(input("Enter a year: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
isLeapYear = False
if year % 4 == 0: 
  isLeapYear = True
  if year % 100 == 0:
    isLeapYear = False
if year % 400 == 0: 
    isLeapYear = True

if isLeapYear == True:
  print("Leap year")
else: 
  print("Not leap year")