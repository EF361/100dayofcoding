# this is a virtual coin toss program
# it will randomly choose heads or tails
import random

number = random.randint(0,1)

if number == 1: 
  print("Heads")
elif number == 0: 
  print("Tails")