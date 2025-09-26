# Simple text-based adventure game
# name is the first variable that stores the user's name
# answer is the second variable that stores the user's input for the first scenario
# elden is the third variable that stores the user's input for the demon scenario
# pudding is the fourth variable that stores the user's input for the traveller scenario
# choice is the fifth variable that stores the user's input for the dragon scenario
# SEKIRO is the sixth variable that stores the user's input for the SEKIRO scenario
# The game uses if, elif, and else statements to handle different scenarios based on user input.

# variable
# if, elif, else statements
# print thank you message

print("Welcome to the adventure game!")
name = input("Enter your name: ")

print(f"Welcome, {name}, to the adventure game!")   

answer = input("You find yourself at a crossroads. Do you want to go left or right? (left/right): ").lower()

# here "answer" is the variable that stores the user's input for the first scenario

if answer == "left":
    # first scenario
    elden = input("You fall into a pit of demons. want to fight them or run away? (fight/run): ")
    
    # here "elden" is the variable that stores the user's input for the demon scenario

    if elden == "fight":
        print("You bravely fight the demons and emerge victorious! You find a treasure chest filled with gold.")
    elif elden == "run":
        print("You run away safely but miss out on the treasure. But you meet a traveller who tells you about dragons! (should we make him an alley/ walk away).")

        #here "pudding" is the variable that stores the user's input for the traveller scenario

        pudding = input("choose (make him an alley/walk away): ")
        if pudding == "make him an alley":
            print("The traveller becomes your ally and helps you on your journey. Together, you find a hidden path to a dragon's lair!")
        elif pudding == "walk away":
            print("You decide to walk away and continue your journey alone.")   
        else:
            print("Invalid choice. Please choose 'make him an alley' or 'walk away'. Game over!")

    
    else:
        print("Invalid choice. Please choose 'fight' or 'run'. Game over!")

elif answer == "right":
    # second scenario
    choice= input("You encounter a friendly dragon who shares his treasure with you. do you want to ride the dragon and go on an adventure? (ride the dragon/walk away): ")
    
    # here "choice" is the variable that stores the user's input for the dragon scenario
    
    if choice == "ride the dragon":
        print("You and the dragon fly off into the sunset, embarking on a grand adventure! ")
    elif choice == "walk away":
        print("You decide to stay on the ground and walk away through the forest their you find a village terrorized by a Warrior name SEKIRO.(Should we fight him?/ walk away) ")
        
        # here "SEKIRO" is the variable that stores the user's input for the SEKIRO scenario

        SEKIRO = input("choose (fight him/walk away): ")
        if SEKIRO == "fight him":
            print("You bravely fight SEKIRO and save the village! The villagers celebrate your victory and you become a hero.")
        elif SEKIRO == "walk away": 
            print("You decide to walk away and continue your journey alone.")
    else:
        print("Invalid choice. Please choose 'ride the dragon' or 'walk away'. Game over!")

else:
    print("Invalid choice. Please choose 'left' or 'right'. Game over!")

print(f"Thank you for playing the adventure game!, {name}.")


# elif and else statements are used to handle different scenarios based on user input.
# Variables are used to store user inputs for different scenarios.
# We can add if and elif statements in elif statements.