from board import Board
from player import Player

class TicTacToeGame:

    ##there is no constructor in this implementation ## it means that the class would inherit all the methods from the previous classes

    ##before the game start, the first we have to do is to welcome the user
    def start(self):
    ## When the game starts, the first thing we do is to welcome the user
        print("*****************************")
        print(" Welcome to Tic-Tac-Toe  ")
        print("*****************************")

        board = Board()
        human_player = Player()
        computer = Player(False)

        #1111board.print_board() #this line of code is to show the board


        ##This while loop will ask the user if he/she would like to play another round
        while True:
            ###i commented out the 111board so that i can implement it here instantly before another round begins

            ###This second while loop is the logic of the game
            ## here i will check the tie, check game over and other functionalities
            while True:
                player_move = human_player.get_move() # this is the fer move method
                board.submit_move(human_player, player_move)
                board.print_board()

                if board.check_is_tie(): #if there was a tie, then this will be true
                    print("It is a tie! Try again.")
                    break
                elif board.check_is_game_over(human_player, player_move):## we have to check it with the last move
                    print("Awesome. You won the game!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    ##the else condition above shows that the computer won, so if that is true, then the following condition follows
                    if board.check_is_game_over(computer, computer_move):
                        print("ooops!... The computer won. Try again.")
                        break

            play_again = input("would you like to play again? Enter X for YES or O for NO: ").upper()

            if play_again == 'O':
                print("Bye! come back soon")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print('Your input was not valid but i will assume that you want to play again.')

        ##HInt: the first loop in charge of the Game, while the second loop should be in charge of the ROund


    def start_new_round(self, board):
            #print(**************)
            print("  New Round     ")
            board.reset_board()
            board.print_board()  ##print the board, before player_move in the nested while loop

game = TicTacToeGame()

game.start()
