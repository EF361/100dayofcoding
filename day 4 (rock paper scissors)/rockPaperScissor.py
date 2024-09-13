rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. : "))
images = [rock, paper,scissors]
# user output 
print(images[choice])

#computer output
print("Computer choose: ")
computerChoice = random.randint(0,2)
print(images[computerChoice])

#win or lose 
if choice > 2 or choice < 0:
    print("You typed an invalid number, you lose!")
elif computerChoice == 2 and choice == 0: 
    print("You win")
elif computerChoice == 0 and choice == 2: 
    print("You lose")
elif choice == computerChoice: 
    print("It's a draw")
elif choice > computerChoice: 
    print("You win!")
elif choice < computerChoice:
    print("You lose!")