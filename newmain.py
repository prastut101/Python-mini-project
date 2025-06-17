import random

mydict = {
    "1": "ROCK",
    "2": "PAPER",
    "3": "SCISSORS",
    "4": "EXIT"
}

print("HELLO, WELCOME TO ROCK PAPER SCISSORS GAME")
print("------------------------------------------")
for key, value in mydict.items():
    print(f"{key}: {value}")

while True:
    choice = input("Enter between (1-4): ")

    # Validate user input first
    if choice not in mydict:
        print("INVALID CHOICE")
        continue

    if choice == "4":
        print("THANKS, kheldeko ma solti")
        break

    computer_chooses = random.choice(list(mydict.values())[:3])
    print(f"Computer chosed: {computer_chooses}")

    myChoice = mydict[choice]

    # Check for draw
    if computer_chooses == myChoice:
        print("DRAW VAYO LA")
        continue  # Continue the game

    # Win conditions for user
    if (
        (computer_chooses == "ROCK" and myChoice == "PAPER") or
        (computer_chooses == "PAPER" and myChoice == "SCISSORS") or
        (computer_chooses == "SCISSORS" and myChoice == "ROCK")
    ):
        print("You WIN 🎉")
    else:
        print("You LOSE 😭")
import random

mydict = {
    "1": "ROCK",
    "2": "PAPER",
    "3": "SCISSORS",
    "4": "EXIT"
}

print("HELLO, WELCOME TO ROCK PAPER SCISSORS GAME")
print("------------------------------------------")
for key, value in mydict.items():
    print(f"{key}: {value}")

while True:
    choice = input("Enter between (1-4): ")

    # Validate user input first
    if choice not in mydict:
        print("INVALID CHOICE")
        continue

    if choice == "4":
        print("THANKS, kheldeko ma solti")
        break

    computer_chooses = random.choice(list(mydict.values())[:3])
    print(f"Computer chosed: {computer_chooses}")

    myChoice = mydict[choice]

    # Check for draw
    if computer_chooses == myChoice:
        print("DRAW VAYO LA")
        continue  

    # Win conditions for user
    if (
        (computer_chooses == "ROCK" and myChoice == "PAPER") or
        (computer_chooses == "PAPER" and myChoice == "SCISSORS") or
        (computer_chooses == "SCISSORS" and myChoice == "ROCK")
    ):
        print("You WIN 🎉")
    else:
        print("You LOSE 😭")


