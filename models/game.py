from models.player import Player

class Game:

    def play(player_1, player_2):
        if player_1.choice == "rock" and player_2.choice == "scissors":
            return f"{player_1.choice} beats {player_2.choice}.. {player_1.name} wins!"
        elif player_1.choice == "scissors" and player_2.choice == "rock":
            return f"{player_2.choice} beats {player_1.choice}.. {player_2.name} wins!"
        elif player_1.choice == "rock" and player_2.choice == "paper":
            return f"{player_2.choice} beats {player_1.choice}.. {player_2.name} wins!"
        elif player_1.choice == "paper" and player_2.choice == "rock":
            return f"{player_1.choice} beats {player_2.choice}.. {player_1.name} wins!"
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return f"{player_1.choice} beats {player_2.choice}.. {player_1.name} wins!"
        elif player_1.choice == "paper" and player_2.choice == "scissors":
            return f"{player_2.choice} beats {player_1.choice}.. {player_2.name} wins!"
        else:
            return None