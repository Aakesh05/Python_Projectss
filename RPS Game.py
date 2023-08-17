import random
while True:
    userChoice = input("Hey rookie, Rock, Paper, or Scissors? ").lower()

    moveOptions = ['rock', 'paper', 'scissors']

    while (userChoice not in moveOptions):
        userChoice = input("Invailid choice, the choice must be Rock, Paper or scissors").lower()

    print("")
    print(f"You chose {userChoice}. ")

    computerChoice = random.choice(moveOptions)
    print(f"The computer chose {computerChoice}.")

    moves = {
        'rock': { 'beats': 'scissors', 'losesTo': 'paper' },
        'scissors': { 'beats': 'paper', 'losesTo': 'rock' },
        'paper': { 'beats': 'rock', 'losesTo': 'scissors' },
    }

    if userChoice == computerChoice:
        print(f"Both you and the computer chose {userChoice}. It's a tie!")
    else:
        if (moves[userChoice]['beats'] == computerChoice):
            print(f"{userChoice} beats {computerChoice}. You win!")
    
        if (moves[userChoice]['losesTo'] == computerChoice):
            print(f"{userChoice} loses to {computerChoice}. The computer wins!")

    quitGame = input("Do you want to Continue? Y or N: ")
    if quitGame.lower() != "y":
        break 
