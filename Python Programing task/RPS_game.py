#Rock-Paper-Scissors Game
#Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.

import random
words=["Rock","Paper","Scissor"]

print("\t----GAME STARTED----")

while True:
    computer=random.choice(words)

    user=input("Enter your word or quit :- ")

    if ( user == "Quit" ):
        break

    if ( computer == user ):
        print(f"Match tie !")
        print(f"Both computer and user choose {user}")

    elif(computer == "Rock" and user == "Paper"):
        print(f"You win !")
        print(f"Computer choose {computer} and user choose {user}")

    elif(computer == "Rock" and user == "Scissor"):
        print(f"You lose !")
        print(f"Computer choose {computer} and user choose {user}")

    elif(computer == "Paper" and user == "Rock"):
        print(f"You lose !")
        print(f"Computer choose {computer} and user choose {user}")

    elif(computer == "Paper" and user == "Scissor"):
        print(f"You win !")
        print(f"Computer choose {computer} and user choose {user}")

    elif(computer == "Scissor" and user == "Rock"):
        print(f"You win !")
        print(f"Computer choose {computer} and user choose {user}")

    elif(computer == "Scissor" and user == "Paper"):
        print(f"You lose !")
        print(f"Computer choose {computer} and user choose {user}")

    else:
        print("Something went wrong !")
    
    choice=input("Play another round (yes or no) = ")
    if (choice != "yes"):
        print("Thanks for playing")
        break

print("\t----GAME OVER----")