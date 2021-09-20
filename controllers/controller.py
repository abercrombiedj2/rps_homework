from flask import render_template
from models.game import *
from models.player import Player
from app import app

@app.route("/<player_1_choice>/<player_2_choice>")
def play_game(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    result = Game.play(player_1, player_2)
    return render_template("result.html", result=result)