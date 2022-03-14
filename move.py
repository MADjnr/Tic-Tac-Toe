#### This is the first class created for the tic-tac-toe game

class Move:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


    def is_valid(self): ## return true if it is valid and false otherwise, when we take user inputs and it falls within the range of values that we can accept
        return 1 <= self._value <= 9 ##implement a code if the move is valid and if it is not valid

    def get_row(self):
## i want to get a corresponding row based on the value
        if self._value in (1,2,3):
            return 0  #first row
        elif self._value in (4,5,6):
            return 1   #second row
        else:
            return 2   #third row

    def get_column(self):
        if self._value in (1,4,7):
            return 0  #first column
        elif self._value in (2,5,8):
            return 1  #second column
        else:
            return 2  ## third column
      #col0#col2#col2
#row 0: | 1 | 2 | 3 |
#row 1: |4  | 5 | 6 |
#row 2: |7  | 8 | 9 |


#### to test the Move class
#move = Move(4)
#print(move.get_column())



