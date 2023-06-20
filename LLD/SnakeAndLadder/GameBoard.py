from collections import deque
class GameBoard:
    def __init__(self, players, snakes, ladders, dice, size=10) -> None:
        self.size = size 
        self.gameboard = [i for i in range(size*size)]

        self.players = deque(players)
        self.jumper = snakes + ladders
        self.dice = dice

    def play_game(self):
        while True:
            # extract current player 
            current_player = self.players.popleft()

            # roll the dice 
            number = self.dice.roll_dice()
            print("dice rolled number is: ", number)

            # check for the new position of user
            new_position = current_player.position + number
            print(f'New Position for Player {current_player.id} is: {new_position}')
            
            # check if new position if going out of bounds
            if new_position >= len(self.gameboard):
                # dont update anything, just add the player back as it is. 
                self.players.append(current_player)
                continue
            
            # check if we have reached the end
            if new_position == len(self.gameboard) - 1:
                print("We have reached the end position")
                print(f'Player {current_player.id} has won')
                break


            # check for snake and ladder 
            for i in range(len(self.jumper)):
                if self.jumper[i].start_position == new_position:
                    # check for snake or ladder
                    if self.jumper[i].start_position > self.jumper[i].end_position: # snake 
                        new_position = self.jumper[i].end_position
                        print(f"Player {current_player.id} has bitten by Snake({self.jumper[i].start_position}, {self.jumper[i].end_position})")
                        print(f'Updated Position is: {new_position}')

                    else: # Ladder :) 
                        new_position = self.jumper[i].end_position
                        print(f"Player {current_player.id} has got ladder({self.jumper[i].start_position}, {self.jumper[i].end_position})")
                        print(f'Updated Position is: {new_position}')

                         # check if we have reached the end
                        if new_position == len(self.gameboard) - 1:
                            print("We have reached the end position")
                            print(f'Player {current_player.id} has won')
                            return
                            
                    break 

            # add the player back to list with updated position
            current_player.position = new_position
            self.players.append(current_player)





    