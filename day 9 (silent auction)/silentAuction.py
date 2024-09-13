#import modules
import art
import clear
import random
import items

#declare variables
cont = True
dictionary = {}
highest = 0
items_to_bid = random.choice(items.items_to_bid)

while cont == True:   
    #welcome user
    print(art.logo)
    print("Welcome to the Secret Auction Program.")
    print(f"Item to Bid: {items_to_bid}")

    #input variables
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dictionary[name] = bid
    winner = ""
    
    #loop the dictionary 
    for things in dictionary: 
        if dictionary[things] > highest: 
            highest = dictionary[things]
            winner = name

    #check whether should continue the loop 
    to_continue = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()
    if to_continue == "yes":
        clear.clear()
    elif to_continue == "no": 
        cont = False
        print(f"The highest bidder is : {name} with the bid of ${highest}")

