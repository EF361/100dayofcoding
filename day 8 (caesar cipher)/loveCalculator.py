print("The Love Calculator is calculating your score...")
name1 = input("What is your name? : ") # What is your name?
name2 = input("What is their name? : ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#combine both of the names
name3 = name1.lower() + name2.lower()

#calculate the total number of true love
calcTrue = name3.count("t") + name3.count("r") + name3.count("u") + name3.count("e")
calcLove = name3.count("l") + name3.count("o") + name3.count("v") + name3.count("e")
totalNumber = int(str(calcTrue) + str(calcLove))

#display output
if totalNumber < 10 or totalNumber>90:
  print(f"Your score is {totalNumber}, you go together like coke and mentos.")
elif totalNumber < 50 and totalNumber > 40: 
  print(f"Your score is {totalNumber}, you are alright together.")
else: 
  print(f"Your score is {totalNumber}.")
