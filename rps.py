import random

def get_choices():
    player_choice = input("[Rock, paper, scissors] Enter a choice => ")

    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    print(get_result(player_choice, computer_choice))

    return choices

def get_result(first_option, second_option):
    info = f"You chose {first_option}, computer chose {second_option}. "

    result_messages = {
        "draw": "It's a draw! 😐",
        "win": "You win! 😀",
        "lost": "You lose. 😢"
    }

    # Who beats who, where the key is the winner
    win_condition = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if first_option == second_option:
        result = result_messages["draw"]

    else:
        if win_condition[first_option] == second_option:
            result = result_messages["win"]
        else:
            result = result_messages["lost"]

    return info + result

get_choices()