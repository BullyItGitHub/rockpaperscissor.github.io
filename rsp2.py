import random

L = ["rock", "scissor", "paper"]

def get_user_choice():
    while True:
        try:
            user_input = int(input('''
                1 Rock 
                2 Scissor
                3 Paper
                Choose your option (1/2/3): '''))
            if user_input in [1, 2, 3]:
                return ["rock", "scissor", "paper"][user_input - 1]
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

while True:
    ucount = 0
    ccount = 0
    
    uc = int(input('''
    Game Start.....
    1 Yes
    2 No | Exit
    Choose an option (1/2): '''))
    
    if uc == 2:
        print("Exiting the game...")
        break
    
    if uc == 1:
        for a in range(5):
            uchoice = get_user_choice()
            Cchoice = random.choice(L)
            print(f"User choice: {uchoice}")
            print(f"Computer choice: {Cchoice}")
            
            if Cchoice == uchoice:
                print("Game Draw")
            elif (uchoice == "rock" and Cchoice == "scissor") or \
                 (uchoice == "paper" and Cchoice == "rock") or \
                 (uchoice == "scissor" and Cchoice == "paper"):
                print("You win")
                ucount += 1
            else:
                print("Computer wins")
                ccount += 1
        
        if ucount == ccount:
            print("Final game draw....")
        elif ucount > ccount:
            print("Final you win the game....")
        else:
            print("Final computer wins the game....")
        
        print(f"User score: {ucount}")
        print(f"Computer score: {ccount}")

    else:
        print("Invalid choice. Please choose 1 to start the game or 2 to exit.")