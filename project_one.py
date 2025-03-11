import random

# Options dictionary
opt_dic = {"Snake": 1, "Water": -1, "Gun": 0}

# Random choice for the computer
computer_choice = random.choice(list(opt_dic.keys()))
computer = opt_dic[computer_choice]

# User input with validation
you = input("Enter your choice (Snake, Water, Gun): ").capitalize()

if you not in opt_dic:
    print("Invalid choice! Please enter Snake, Water, or Gun.")
else:
    you_check = opt_dic[you]
    
    print(f"Computer chose: {computer_choice}")
    
    # Game logic
    if computer == you_check:
        print("Game Draw!")
    elif (you_check == 1 and computer == -1) or (you_check == -1 and computer == 0) or (you_check == 0 and computer == 1):
        print(f"{you} beats {computer_choice}, You Win! 🎉")
    else:
        print(f"{computer_choice} beats {you}, Computer Wins! 😢")
