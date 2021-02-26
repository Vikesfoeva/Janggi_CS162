#  Name: Brandon Lenz
#  Date: 2/19/2021
#  Description: The ancient game of Janggi!  This project outlines the logic to get started playing Janggi.
# https://docs.google.com/spreadsheets/d/1Lfl4IaSGqQaBYZmoD2wOrTVkXS2E7BP9v6N4p5sDPgM/edit#gid=0


class JanggiGame():
    """Builds the board and contains the methods that help the board to function"""

    def __init__(self):
        """Creates the board and the game"""
        self._game_state = None
        self._blue_turn = True
        self._board = {
            'a': {
                1: Chariot(False),
                2: None,
                3: None,
                4: Soldier(False),
                5: None,
                6: None,
                7: Soldier(True),
                8: None,
                9: None,
                10: Chariot(True)},
            'b': {
                1: Elephant(False),
                2: None,
                3: Cannon(False),
                4: None,
                5: None,
                6: None,
                7: None,
                8: Cannon(True),
                9: None,
                10: Elephant(True)},
            'c': {
                1: Horse(False),
                2: None,
                3: None,
                4: Soldier(False),
                5: None,
                6: None,
                7: Soldier(True),
                8: None,
                9: None,
                10: Horse(True)},
            'd': {
                1: Guard(False),
                2: None,
                3: None,
                4: None,
                5: None,
                6: None,
                7: None,
                8: None,
                9: None,
                10: Guard(True)},
            'e': {
                1: None,
                2: General(False),
                3: None,
                4: Soldier(False),
                5: None,
                6: None,
                7: Soldier(True),
                8: None,
                9: General(True),
                10: None},
            'f': {
                1: Guard(False),
                2: None,
                3: None,
                4: None,
                5: None,
                6: None,
                7: None,
                8: None,
                9: None,
                10: Guard(True)},
            'g': {
                1: Elephant(False),
                2: None,
                3: None,
                4: Soldier(False),
                5: None,
                6: None,
                7: Soldier(True),
                8: None,
                9: None,
                10: Elephant(True)},
            'h': {
                1: Horse(False),
                2: None,
                3: Cannon(False),
                4: None,
                5: None,
                6: None,
                7: None,
                8: Cannon(True),
                9: None,
                10: Horse(True)},
            'i': {
                1: Chariot(False),
                2: None,
                3: None,
                4: Soldier(False),
                5: None,
                6: None,
                7: Soldier(True),
                8: None,
                9: None,
                10: Chariot(True)}
        }

    def get_game_state(self):
        """Returns the state of the game as UNFINISHED or shows the victor"""
        if self._game_state is None:
            return "UNFINISHED"
        return self._game_state

    def is_in_check(self):
        """
        """
        pass

    def make_move(self, source, destination):
        """
        """
        source_col = source[0]
        source_row = source[1:]

        if self.space_open(source_col, source_row):
            # if the source is a free space, this is not a valid move
            return False

        destination_col = destination[0]
        destination_row = destination[1:]

        source_square = self._board[source_col][source_row]
        destination_square = self._board[destination_col][destination_row]

        # Return False because the source is not

    def space_open(self, col, row):
        """Checks an input coordinator to determine if a space is open"""
        if self._board[col][row] is None:
            return True
        return False

    def print_board(self):
        """Prints out the board into the terminal"""
        for board_row in range(1, 1 + len(self._board['a'])):
            row = []
            for board_col in self._board.keys():

                square = self._board[board_col][board_row]

                if square is not None:
                    square = square.get_name()

                # This logic exists to add padding for clean printing of the board
                if square is None:
                    row.append('             ')
                elif len(square) == 9:
                    row.append(square + '    ')
                elif len(square) == 10:
                    row.append(square + '   ')
                elif len(square) == 11:
                    row.append(square + '  ')
                elif len(square) == 12:
                    row.append(square + ' ')
                elif len(square) == 13:
                    row.append(square)
            print(row)


class GamePiece():
    """A parent class to create game pieces"""
    def __init__(self, owner_blue):
        """Defines the parent class"""
        self._is_blue = owner_blue
        self._captured = False

    def set_captured(self):
        """Marks this piece as captured"""
        self._captured = True

    def get_captured(self):
        """Returns whether this piece is captured or not"""
        return self._captured

    def get_owner(self):
        return self._is_blue


class Chariot(GamePiece):
    """Outlines the Chariot Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid"""
        pass

    def get_name(self):
        if self.get_owner():
            return "Blue Chariot"
        return "Red Chariot"


class Soldier(GamePiece):
    """Outlines the Soldier Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid"""
        pass

    def get_name(self):
        if self.get_owner():
            return "Blue Soldier"
        return "Red Soldier"


class Elephant(GamePiece):
    """Outlines the Elephant Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid"""
        pass

    def get_name(self):
        if self.get_owner():
            return "Blue Elephant"
        return "Red Elephant"


class Cannon(GamePiece):
    """Outlines the Cannon Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid"""
        pass

    def get_name(self):
        if self.get_owner():
            return "Blue Cannon"
        return "Red Cannon"


class Horse(GamePiece):
    """Outlines the Horse Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid"""
        pass

    def get_name(self):
        if self.get_owner():
            return "Blue Horse"
        return "Red Horse"


class Guard(GamePiece):
    """Outlines the Guard Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid"""
        pass

    def get_name(self):
        if self.get_owner():
            return "Blue Guard"
        return "Red Guard"


class General(GamePiece):
    """Outlines the Guard Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid"""
        pass

    def get_name(self):
        if self.get_owner():
            return "Blue General"
        return "Red General"


# Basic Tests
game = JanggiGame()

game.print_board()
game.make_move('c1', 'e10')
print(game.space_open("a", 2))
# move_result = game.make_move('c1', 'e3') #should be False because it's not Red's turn
# move_result = game.make_move('a7,'b7') #should return True
# blue_in_check = game.is_in_check('blue') #should return False
# game.make_move('a4', 'a5') #should return True
# state = game.get_game_state() #should return UNFINISHED
# game.make_move('b7','b6') #should return True
# game.make_move('b3','b6') #should return False because it's an invalid move
# game.make_move('a1','a4') #should return True
# game.make_move('c7','d7') #should return True
# game.make_move('a4','a4') #this will pass the Red's turn and return True

