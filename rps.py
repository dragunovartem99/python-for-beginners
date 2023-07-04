import random

first_player_name = "Human"
second_player_name = "Computer"


def get_choices():
    player_choice = input("[Rock, paper, scissors] Enter a choice => ")

    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    choices = {
        first_player_name: player_choice,
        second_player_name: computer_choice
    }

    return choices


def get_result(first_option, second_option):
    info = f"{first_player_name} chose {first_option}, {second_player_name} chose {second_option}. "

    # It's kinda first-player-oriented
    result_messages = {
        "draw": "It's a draw! 😐",
        "win": f"{first_player_name} wins! 🥰",
        "lost": f"{first_player_name} loses. 😱"
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


choices = get_choices()
game_termination = get_result(choices[first_player_name], choices[second_player_name])

print(game_termination)
