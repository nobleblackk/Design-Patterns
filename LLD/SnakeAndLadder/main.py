from GameBoard import GameBoard
from Player import Player 
from Jumper import Jumper 
from Dice import Dice

snake_1 = Jumper(34, 10)
snake_2 = Jumper(44, 2)

ladder_1 = Jumper(5, 70)
ladder_2 = Jumper(39, 79)

dice = Dice() 

player_1 = Player(1)
player_2 = Player(2)
player_3 = Player(3)



gameboard = GameBoard(players=[player_1, player_2, player_3], snakes=[snake_1, snake_2], ladders=[ladder_1, ladder_2], dice=dice)
gameboard.play_game()