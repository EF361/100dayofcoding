line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? : ") # Where do you want to put the treasure?

# 🚨 Don't change the code above 👆
# Write your code below this row 👇
locationCol = position[0].lower()
locationRow = int(position[1]) - 1

if locationCol == "a":
  locationCol = 0
elif locationCol == "b":
  locationCol = 1
elif locationCol == "c":
  locationCol = 2

map[locationRow][locationCol] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")