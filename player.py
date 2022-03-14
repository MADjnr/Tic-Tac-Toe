#### This is a file where i implemented the player class
import random

from move import Move


class Player:

    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human: ##this is a code to implement if the player is human or computer
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    ##lets creates a move that the player selects
    def get_move(self):
        if self._is_human: ##check if the player is a human player
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input("please enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter an integer between 1 and 9.")
        return move

    ## since the computer would have to choose randomly i will use the random library

    def get_computer_move(self):
        random_choice = random.choice(list(range(1,10)))
        move = Move(random_choice)
        print("Computer move (1-9): ", move.value)
        return move



### testing the code

#computer_player = Player(False)

#a_move = computer_player.get_move()   ##this is a move object

#print(a_move)