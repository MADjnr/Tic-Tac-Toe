
from  player import Player
from player import  Player


class Board:

    EMPTY_CELL = 0 ##this is used to denote an empty cell in the board

    def __init__(self):
        self.game_board = [[0, 0, 0],   ###this is the initial representation when we create a board instance
                           [0, 0, 0],
                           [0, 0, 0]]

    ##this is a method that will print the board
    def print_board(self):
        self.print_board_with_positions()

        #print("/nPositions:")
        #self.print_board_with_positions()

        ####to print the current state of the board
        print("\nBoard:")
        for row in self.game_board:  ###In the board attribute, there are three lists nested in a list
                                    ### SO this iterations is interating across three lists in a list
    ###printing the structure of the board
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print() ##for a new line
        print()


    def print_board_with_positions(self):
        print("\nPositions: ")
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

### At this stage i want to implement a method to submit a move to the board

    def submit_move(self, player, move): ## move is a move object(already declared Move class). in order to submit move, we need to know the row and the column
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]        ##to check if the position has been taken by another character

        if value == Board.EMPTY_CELL: ##if the value assigned to the position above is empty, we assign that position to a player marker
            self.game_board[row][col] = player.marker
        else:
            print('This position is already taken. Please enter another one')


    def check_is_game_over(self, player, last_move): #the last move submitted by a player makes the player win the game
    ## when a player submit move to the board, we are going to check if the game is over
    ## take the last_move, check the row, the column, the diagonal and anti-diagonal
        return ((self.check_row(player, last_move))
                or (self.check_column(player, last_move))
                or (self.check_diagonal(player))
                or (self.check_antidiagonal(player))) ##return if either one of the method calls return true

    def check_row(self, player, last_move):
        row_index = last_move.get_row() ## this could be row 1, row 2, or row 3 . this line gets the row index
        board_row = self.game_board[row_index]  ## get the actual list that corresponds to that row ['0','0', 'x']

        return board_row.count(player.marker) == 3 ## count how many times a player's marker appears on the row.
                                                   ##example: if the count is 'x' it returns that the player marker is one
                                                    ## so it is compared with the value 3, if the value is three, it returns true.

    def check_column(self, player, last_move):
        markers_count = 0
        column_index = last_move.get_column()

        for i in range(3): # 3 because we have three rows
            if self.game_board[i][column_index] == player.marker:
                markers_count += 1

        return markers_count == 3 ## return True if the markers_count is equals to 3

    def check_diagonal(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1

        return markers_count == 3 ## return True if the markers_count is equal to 3

    def check_antidiagonal(self, player):
        markers_count = 0

        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_is_tie(self):
        empty_counter = 0  # this is to check if the game is a tie. If there is a tie then, the board is full
                           ## But they are not full with the same marker
                            ## We have to check how many empty set we have and if they are 0 then, there is a tie

        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)  ## this is to add how many zeros in a row, which is a list

        return empty_counter == 0 ##return true if the counter is zero and false otherwise

    def reset_board(self):  ## this is a method to reset the board. ie is the initial state of the board
        self.game_board =  [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]




'''
###i will test the game right now

board = Board()
player = Player()

board.print_board()

move1 = player.get_move()
move2 = player.get_move()
move3 = player.get_move()

board.print_board()

board.submit_move(player, move1)
board.submit_move(player, move2)
board.submit_move(player, move3)

board.print_board()

print(board.check_is_game_over(player, move3))
'''

