"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def input_prompt(text):
    while True:
        user_input = input(f"{text}")
        if user_input.isdigit() != True:
            print("**Error**\nThat's not an integer or it's not a positive number!\n")
            continue
        elif int(user_input) < 1 or int(user_input) > 10:
            print("**Error**\nThat number is out of range!\n")
            continue
        elif user_input.isdigit() == True and (int(user_input) >= 1 and int(user_input) <= 10):
            break
    user_input = int(user_input)
    return(user_input)

def yes_or_no(x):
    x_input = str(input(x))
    while x_input.lower() != "y" and x_input.lower() != "n":
        print("**Error!**\nPlease only enter 'Y' or 'N'\n")
        x_input = str(input(x))
    return(x_input)

def start_game():
    print(f"""
    {"-"*30}
    Welcome to the number guessing game!
    {"-"*30}
    """)
    
    attempt_history = []
    
    while True:
        answer = random.randint(1,10)
        user_guess = input_prompt("Pick a number between 1 and 10.\n> ")
        answer_list = []
        answer_list.append(user_guess)
    
        while user_guess != answer:
            if user_guess < answer:
                user_guess = input_prompt("It's higher!\n> ")
                answer_list.append(user_guess)
            if user_guess > answer:
                user_guess = input_prompt("It's lower!\n> ")
                answer_list.append(user_guess)
        
        attempts = len(answer_list)
        attempt_history.append(attempts)
        
        print(f"You got it! The answer is '{answer}'. You made {attempts} attempts. Thanks for playing.")
        
        play_again = yes_or_no("Would you like to play again? (Y/N):  ")
        
        if play_again == 'y':
            print(f"The current high score is: {min(attempt_history)} attempts")
            continue
        elif play_again == 'n':
            if attempt_history != 0:
                print(f"The best score is: {min(attempt_history)} attempts")
            print("Thanks again for playing the game!")
            break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
