actions = ["1. Attack", "2. Defend", "3. Look Around", "4. Quit"]

for items in actions:
    print(items)
while True:

    choice = input("Choose a number between 1-4: ")

    if not choice.isnumeric():
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
