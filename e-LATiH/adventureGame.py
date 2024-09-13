print("""        _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/jgs     `.  / /       `.~-^=-=~=^=.-'      '-._ `._""")
print("Welcome to Albert's Forest.")
print("Your mission is to find Steve.")
choice1 = input("Choose left or right:").lower()
if choice1 =="left":
    choice2 = input("You have reached a river. Enter swim or boat.").lower()
    if choice2 == "boat":
        print("You have reached the other side of the river.")
        choice3 = input("You have reached a fork in the road. Enter left or right.").lower()
        if choice3 == "left":
            print("You have reached a cave.")
            choice4 = input("Enter left or right.").lower()
            if choice4 == "left":
                print("You have found Steve.")
            else: 
                print("You have been eaten by a bear.")
        else: 
            print("You have been attacked by bats.")  
    else: 
        print("You got attacked by a mega shark. ")
else:
    print("A crocodile come out and attacked you. You are dead")
     