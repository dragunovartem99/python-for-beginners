import random

first_player_name = "Human"
second_player_name = "Computer"

options = ["rock", "paper", "scissors"]

def get_choices():
	first_player_choice = input("[Rock, paper, scissors] Enter a choice => ")

	second_player_choice = random.choice(options) # it is a computer

	choices = {
		first_player_name: first_player_choice,
		second_player_name: second_player_choice
	}

	return choices


def get_result(first_option, second_option):
	if first_option.lower() not in options:
		return f'"{first_option}" is not an option! You can choose rock, paper or scissors. Try again!'

	first_option = first_option.lower()

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
