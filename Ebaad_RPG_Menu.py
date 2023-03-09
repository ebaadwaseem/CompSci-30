# Ebaad Waseem
# CS 30 Period 1
# March 9, 2023,
# This is a very simple RPG Game Menu

# Defined actions that the user can take
actions = ["1. Attack", "2. Defend", "3. Look Around", "4. Quit"]
# Printing all items inside the array
for items in actions:
    print(items)
# Runs indefinitely until it breaks
while True:
    # Handles user inputs, a number between 1 and 4
    choice = input("Choose a number between 1 - 4: ")
    # Checks the user input, handles if not a number and breaks when needed
    if not choice.isnumeric() :
        print("Incorrect input, chose a number between 1 and 4")
    else:
        if int(choice) == 1:
            print("You have chosen to Attack!")
        elif int(choice) == 2:
            print("You have chosen to Defend!")
        elif int(choice) == 3:
            print("You have chosen to Look Around!")
        elif int(choice) == 4:
            print("Exiting game, thank you for playing!")
            break
        else:
            print("Incorrect input, chose a number between 1 and 4")
