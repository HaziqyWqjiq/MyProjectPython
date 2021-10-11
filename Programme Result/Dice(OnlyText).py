from random import randint

# Variables
die = 6
trigger = 1
run = True
points = 0

while run:
    # Ask user if he wants to roll
    inp = input("Do you want to roll? y/n: ")
    # If user enters "y" or "Y"
    if inp == "y" or inp == "Y":
        # Roll the dice from 1 to our die variable (6)
        roll = randint(1, die)
        # Check if the roll isn't the same as our trigger
        if roll != trigger:
            # Add points to score
            points = points + roll
            # Show points and new score.
            print(roll.__str__() + " points added to your score.")
            print("Your score is: " + points.__str__())
            
        else:
            # If the roll hits the trigger, end the game
            run = False
            # Print final score before terminating
            print("You rolled 1! Your score was: " + points.__str__())
    else: 
        # If the user wants to stop the game
        run = False
        # Print final score before terminating
        print("Your score is: " + points.__str__())
    