# Enter your height in meters e.g., 1.55
height = float(input("Enter your height: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2

if bmi < 18.5: 
  condition = "you are underweight. "
elif bmi < 25: 
  condition = "you have a normal weight."
elif bmi < 30: 
  condition = "you are slightly overweight."
elif bmi < 35: 
  condition = "you are obese."
else: 
  condition = "you are clinically obese."
  
print(f"Your BMI is {bmi}, {condition}")