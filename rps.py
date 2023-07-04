def get_choices():
    player_choice = input("[Rock, paper, scissors] Enter a choice => ")
    choices = {
        "player": player_choice,
        "computer": "paper"
    }

    return choices

choices = get_choices()
print(choices)