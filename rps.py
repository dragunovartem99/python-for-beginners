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
        "lose": "You lose. 😢"
    }

    if first_option == second_option:
        result = result_messages["draw"]

    elif first_option == "rock":
        if second_option == "paper":
            result = result_messages["lose"]
        else:
            result = result_messages["win"]

    return info + result

get_choices()