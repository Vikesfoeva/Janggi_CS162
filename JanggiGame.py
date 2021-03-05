#  Name: Brandon Lenz
#  Date: 2/19/2021
#  Description: The ancient game of Janggi!  This project outlines the logic to get started playing Janggi.
#  https://docs.google.com/spreadsheets/d/1Lfl4IaSGqQaBYZmoD2wOrTVkXS2E7BP9v6N4p5sDPgM/edit#gid=0
#  Additional planning - https://docs.google.com/spreadsheets/d/13MTVMrmjhH53qYzgSoDzK7Y_Y0INGk79RlSjAaf7e8o/edit#gid=0
#  https://www.pychess.org/

#######
# "DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"

# Initializing the board
# The board will be initialized upon the creation of an instance of the JanggiGame class.  Nested dictionarys will be
# used to hold the game board.  The first layer of the dictionary is the columns of the board 'a', 'b', etc.  Then,
# nested within letter is a dictionary that holds rows 1-10.  The value at each key is the 'thing' currently at that
# square.  That would be a piece or None.

# Determining how to represent pieces  at a given location on the board
# Each piece is created with a class.  Each of their classes is a child of the parent GamePiece class.  A boolean
# is used to determine the player.  False represents red and True represents blue.  True or False is passed in each
# creation of an instance of these classes as the board is being laid out.

# Determining how to validate a given move according to the rules for each piece, turn taking and other game rules.
# Each child class of GamePiece has a method titled check_valid_moves.  This method is redefined for each child class
# as the logic is different for every game piece.  Depending on the piece the logic is a little bit different for red
# pieces vs blue pieces, this is handled by an if statement in the aforementioned method.  For example, this takes place
# with soldiers as they can only move forward (forward of of course has different meaning for red vs blue).

# Modifying the board state after each move.
# I'm not entirely sure what state is meant to refer to here since state was referred to in the README as 'UNFINSISHED'
# or 'RED_WON', etc.  That state does not need to be modified after every single move, and should only change once
# during the course of the game.  Pieces are moved across the board by passing several logical checks.  Is the right
# piece being moved for who's turn it is, is the move valid for the chosen piece, were proper coordinates passed, etc.
# The first step here is to set the destination square equal to the source square.  From there the source square can
# be set to None.  There is not a scenario where the source is not none after a successful completion of a move.

# Determining how to track which player's turn it is to play right now.
# Similarly to how the game pieces have their ownership defined via a boolean, the turn structure is also defined
# using a boolean.  If the boolean is set to True, it is blue's turn.  If False, then it is red's.  After the successful
# completion of a turn, the boolean is flipped in value indicating it is now the other's turn.

# Determining how to detect the checkmate scenario.
# First we need to check if a general is in check.  We do this by checking to see if the opponent's pieces have any
# valid moves that place them capturing the general next turn.  If yes, than that general is in check.  We can optimize
# this part of the function by ensuring we diligently check this so that we only need to perform this check on the most
# recently moved piece.  From there, once the General is in check, we need to determine what are the legal moves to have
# the general evade check by moving in the palace, maneuvering a piece to block the check, or capturing the enemy piece
# to prevent the check.  If none of these three can be done, then it is indeed checkmate.  To perform that check, we
# will need to iterate overall all of the pieces for the 'checked'  general to see if they have any means of saving
# themselves.

# Determining which player has won and also figuring out when to check that.
# If a player was checkmated in the previous step, then the non-checkmated player will be declared the victor.

#########


def print_error(message):
    """A function to print out error messages to the console.  We use this function so that only 1 line needs
    to be commented away to prevent console output"""
    #print(message)


class JanggiGame():
    """Builds the board and contains the methods that help the board to function"""

    def __init__(self):
        """Creates the board and the game.  The board is defined by nested dictionaries.  The first level is an entry
        for each row (a, b, c etc) and then within each row the columns for that one.  This board is prebuilt in the class
        so that it is built consistently.  We are passing False to the various game piece child classes to create a red
          piece and True to create a blue piece.  We also are storing the game_state here & also whose turn it
          currently is."""
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
        """Returns the state of the game as UNFINISHED or shows the victor.  None is used to old the unfished state
        for ease of referencing in the program.  If none though, we will return UNFINISHED"""
        if self._game_state is None:
            return "UNFINISHED"
        return self._game_state

    def is_in_check(self, player):
        """Intakes a player as either red or blue and returns if that player is n check.  To perform this, we need need
        to iterate through a player's game pieces and see if any of them have valid moves that would place them on the
        opponent's general.  For example, if there is a solidrer being checked, we would want to check all of the potential
        moves for that soldier and see if any of them wind up placing them on the square as the general.  If that is true
        and the general also then does not have any moves that put them in a spot where they are not in check, then the
        game is now checkmate."""

        if type(player) != str:
            return False

        player = player.lower()

        if player == 'red':
            pass
        elif player == 'blue':
            pass

        return False

    def make_move(self, source, destination):
        """
        Allows a move to occur and outlines the logic to ensure that said move is valid.  This function performs several
        checks to ensure that players are moving valid pieces on their turn, ensures they are not trying to capture their
        own pieces, calls appropiate methods to ensure they are making the proper move for the piece they selected.
        """
        print("Attempting", source, "==>", destination)

        if source == destination:
            self._blue_turn = not self._blue_turn
            return True

        # Break down the source square algebraic notation into coordinates
        source_col = source[0].lower()
        source_row = int(source[1:])

        if self.space_open(source_col, source_row):
            # if the source is a free space, this is not a valid move
            return False

        if self._game_state is not None:
            # The game has ended, no more valid moves!
            return False

        # Break down the destination square algebraic notation into coordinates
        destination_col = destination[0].lower()
        destination_row = int(destination[1:])

        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        if source_col not in layout or destination_col not in layout:
            return False

        if destination_row > 10 or source_row > 10:
            return False

        source_square = self._board[source_col][source_row]
        destination_square = self._board[destination_col][destination_row]

        if self._blue_turn and not source_square.get_owner():
            # Can't move a red piece on blue's turn
            print_error("Can't move a red piece on blue's turn")
            return False
        elif not self._blue_turn and source_square.get_owner():
            # Can't move a blue piece on red's turn
            print_error("Can't move a blue piece on red's turn")
            return False

        if destination_square is not None:
            if source_square.get_owner() == destination_square.get_owner():
                # The pieces on the source and destination squares are owned by the same player
                # You can't capture your own piece, it's poor battle tactics!
                return False

        if source_square.check_valid_moves(source_col, source_row, destination_col, destination_row, self):
            self._board[destination_col][destination_row] = source_square
            self._board[source_col][source_row] = None
            self._blue_turn = not self._blue_turn

        return True

    def space_open(self, col, row):
        """Checks an input coordinator to determine if a space is open.  This method is called by the make_move method
        and relies on the coordiaate breakdown that is performed in the make_move method."""
        if self._board[col][row] is None:
            return True
        return False

    def print_board(self):
        """Prints out the board into the terminal.  This is designed to help the user visualize board after a a set of
        moves has taken place.  This method relies on the get_name() method of each piece's class to print out what
        that particular piece is.  That method on those pieces is just used to help track this board visualization."""
        print()
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
        print()


class GamePiece():
    """A parent class to create game pieces.  This class initializes the information that is consistent across all
    types of game poieces"""
    def __init__(self, owner_blue):
        """Defines the parent class and attributes used across all pieces."""
        self._is_blue = owner_blue
        self._captured = False

    def set_captured(self):
        """Marks this piece as captured"""
        self._captured = True

    def get_captured(self):
        """Returns whether this piece is captured or not"""
        return self._captured

    def get_owner(self):
        """Returns the boolean of whether or not this is a blue game piece"""
        return self._is_blue

    def col_difference(self, col1, col2):
        """Accepts two different columns listed by letter and returns how many columns are moved to traverse.  This
        method is used when determining if moves are valid"""
        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        col1 = layout.index(col1)
        col2 = layout.index(col2)
        return abs(col1 - col2)

    def invalid_diagonal_check(self, source_col, source_row, destination_col, destination_row):
        """Disallowed Diagonals in the Palace (note all others are invalid).  Note that we need to block both D9==E10
        and also E10 ==> D9
        D9  <=> E10,
        E10 <=> F9,
        F9  <=> E8,
        E8  <=> D9,
        E1 <=> F2,
        F2 <=> E3,
        E3 <=> D2,
        D2 <=> E1

        Returns True if the diagonal was invalid
        """

        # D9 ==> E10 and E10 ==> D9
        if source_col == 'd' and source_row == 9 and destination_col == 'e' and destination_row == 10:
            return True
        elif source_col == 'e' and source_row == 10 and destination_col == 'd' and destination_row == 9:
            return True

        # E10 ==> F9 and F9 ==> E10
        elif source_col == 'e' and source_row == 10 and destination_col == 'f' and destination_row == 9:
            return True
        elif source_col == 'f' and source_row == 9 and destination_col == 'e' and destination_row == 10:
            return True

        # F9 ==> E8 and E8 ==> F9
        elif source_col == 'f' and source_row == 9 and destination_col == 'e' and destination_row == 8:
            return True
        elif source_col == 'e' and source_row == 8 and destination_col == 'f' and destination_row == 9:
            return True

        # E8 ==> D9 and D9 ==> E8
        elif source_col == 'e' and source_row == 8 and destination_col == 'd' and destination_row == 9:
            return True
        elif source_col == 'd' and source_row == 9 and destination_col == 'e' and destination_row == 8:
            return True

        # D2 ==> E1 and E1 ==> D2
        if source_col == 'd' and source_row == 2 and destination_col == 'e' and destination_row == 1:
            return True
        elif source_col == 'e' and source_row == 1 and destination_col == 'd' and destination_row == 2:
            return True

        # E1 ==> F2 and F2 ==> E1
        elif source_col == 'e' and source_row == 1 and destination_col == 'f' and destination_row == 2:
            return True
        elif source_col == 'f' and source_row == 2 and destination_col == 'e' and destination_row == 1:
            return True

        # F2 ==> E3 and E3 ==> F2
        elif source_col == 'f' and source_row == 2 and destination_col == 'e' and destination_row == 3:
            return True
        elif source_col == 'e' and source_row == 3 and destination_col == 'f' and destination_row == 2:
            return True

        # E3 ==> D2 and D2 ==> E3
        elif source_col == 'e' and source_row == 3 and destination_col == 'd' and destination_row == 2:
            return True
        elif source_col == 'd' and source_row == 2 and destination_col == 'e' and destination_row == 3:
            return True

        return False

    def inside_palace(self, source_col, source_row, destination_col, destination_row):
        """Returns true if a piece is contained within the palace and false if is not"""

        source_col_palace = source_col == 'd' or source_col == 'e' or source_col == 'f'
        source_row_palace = source_row < 4 or source_row > 7

        destination_col_palace = destination_col == 'd' or destination_col == 'e' or destination_col == 'f'
        destination_row_palace = destination_row < 4 or destination_row > 7

        if source_col_palace and source_row_palace and destination_col_palace and destination_row_palace:
            return True

        return False

class Chariot(GamePiece):
    """Outlines the Chariot Game Piece"""
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """Checks if the input move is valid and returns True / False based on that."""
        in_palace = False
        if self.inside_palace(source_col, source_row, destination_col, destination_row):
            in_palace = not in_palace

        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        col1 = layout.index(source_col)
        col2 = layout.index(destination_col)
        col_move = col2 - col1

        row_move = destination_row - source_row

        if in_palace and abs(row_move) > 0 and abs(col_move) > 0:
            if abs(row_move) > 2 or abs(col_move) > 2:
                return False
            if self.invalid_diagonal_check(source_col, source_row, destination_col, destination_row):
                return False
            if abs(row_move) == 2 and abs(col_move) != 2 and row_move != 0:
                return False
            if abs(col_move) == 2 and abs(row_move) != 2 and col_move != 0:
                return False

        if (not in_palace and source_col != destination_col) and (not in_palace and source_row != destination_row):
            # Can only move diagonally while in the palace
            return False

        if not in_palace and col_move == 0:
            # Column is being held constant
            if 0 > row_move:
                increment = -1
            else:
                increment = 1

            for path in range(increment, row_move, increment):
                if not game_board.space_open(source_col, source_row + path):
                    return False

        elif not in_palace and row_move == 0:
            # Row is being held constant
            if 0 > col_move:
                increment = -1
            else:
                increment = 1

            for path in range(increment, col_move, increment):
                if not game_board.space_open(layout[col1 + path], source_row):
                    return False

        elif in_palace and abs(row_move) == 2 and abs(col_move) == 2:
            # Check for valid palace diagonals
            # If we are trying to move two diagonal spaces, the middle must be empty
            if source_row > 5 and not game_board.space_open('e', 9):
                return False
            elif source_row < 5 and not game_board.space_open('e', 2):
                return False

        return True

    def get_name(self):
        """Prints out the game piece based on who the owner is"""
        if self.get_owner():
            return "Blue Chariot"
        return "Red Chariot"


class Soldier(GamePiece):
    """Outlines the Soldier Game Piece"""
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """
        Checks if the input move is valid
        Soldiers can only move forward their direction or side to side 1 space
        """
        row_move = abs(source_row - destination_row)
        if row_move > 1:
            # Can only move 1 row
            return False

        col_move = self.col_difference(source_col, destination_col)
        if col_move > 1:
            # Can only move 1 col
            return False

        in_palace = False
        if (source_row == 2 or source_row == 3 or source_row == 8 or source_row == 9) and (source_col == 'd' or source_col == 'e' or source_col == 'f'):
            in_palace = not in_palace

        if not in_palace and row_move == 1 and col_move ==1:
            # Can only move diagonally in the palace
            return False

        if self.get_owner():
            # This section represents blue
            if source_row < destination_row:
                return False
        else:
            # This section represents red
            if destination_row < source_row:
                return False

        # Checks to see if the diagonal we are moving on is valid, not all are
        if self.invalid_diagonal_check(source_col, source_row, destination_col, destination_row):
            return False

        return True

    def get_name(self):
        """Returns the name of the game piece for printing the board"""
        if self.get_owner():
            return "Blue Soldier"
        return "Red Soldier"


class Elephant(GamePiece):
    """Outlines the Elephant Game Piece"""
    def check_valid_moves(self, input_move):
        """Checks if the input move is valid and returns True / False based on that."""
        return True

    def get_name(self):
        """Returns the name of the game piece for printing the board"""
        if self.get_owner():
            return "Blue Elephant"
        return "Red Elephant"


class Cannon(GamePiece):
    """Outlines the Cannon Game Piece"""
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """Checks if the input move is valid and returns True / False based on that."""
        return True

    def get_name(self):
        """Returns the name of the game piece for printing the board"""
        if self.get_owner():
            return "Blue Cannon"
        return "Red Cannon"


class Horse(GamePiece):
    """Outlines the Horse Game Piece"""
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """Checks if the input move is valid and returns True / False based on that.
        This piece moves similarily to the knight in western chess, in an L shape.  It can however be blocked.
        It will first move 1 space vertically or horizontally towards it's destination and then 1 space
        diagonally, if it cannot make the first 1/2 of the move; it is blocked.
        """
        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        col1 = layout.index(source_col)
        col2 = layout.index(destination_col)
        col_move = col2 - col1

        row_move = destination_row - source_row

        # col_move or row_move must be 2 and the other must be 1
        if not (abs(col_move) == 2 and abs(row_move) == 1) and not (abs(col_move) == 1 and abs(row_move == 2)):
            return False

        # Check if the vertical move is blocked
        if abs(row_move) == 2 and not game_board.space_open(source_col, source_row + row_move/2):
            return False
        # Check if the horizontal move is blocked
        elif abs(row_move) == 1 and not game_board.space_open(layout[col1 + col_move/2], source_row):
            return False
        else:
            return False

        return True

    def get_name(self):
        """Returns the name of the game piece for printing the board"""
        if self.get_owner():
            return "Blue Horse"
        return "Red Horse"


class Guard(GamePiece):
    """Outlines the Guard Game Piece"""
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """Checks if the move is valid for a Guard.  Guards can move any direction within their palace"""
        row_move = abs(source_row - destination_row)

        if destination_row == 4 or destination_row ==5 or destination_row ==6 or destination_row == 7:
            # The destination is outside the palace
            return False

        if destination_col != 'd' and destination_col != 'e' and destination_col != 'f':
            # The destination is outside the palace
            return False

        if row_move > 1:
            # Can only move 1 row
            return False

        col_move = self.col_difference(source_col, destination_col)
        if col_move > 1:
            # Can only move 1 col
            return False

        # Checks to see if the diagonal we are moving on is valid, not all are
        if self.invalid_diagonal_check(source_col, source_row, destination_col, destination_row):
            return False

        return True

    def get_name(self):
        """Checks if the input move is valid and returns True / False based on that."""
        if self.get_owner():
            return "Blue Guard"
        return "Red Guard"


class General(GamePiece):
    """Outlines the Guard Game Piece"""
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """Checks if the move is valid for a General.  Generals can move any direction within their palace"""
        row_move = abs(source_row - destination_row)

        if destination_row == 4 or destination_row ==5 or destination_row ==6 or destination_row == 7:
            # The destination is outside the palace
            return False

        if destination_col != 'd' and destination_col != 'e' and destination_col != 'f':
            # The destination is outside the palace
            return False

        if row_move > 1:
            # Can only move 1 row
            return False

        col_move = self.col_difference(source_col, destination_col)
        if col_move > 1:
            # Can only move 1 col
            return False

        # Checks to see if the diagonal we are moving on is valid, not all are
        if self.invalid_diagonal_check(source_col, source_row, destination_col, destination_row):
            return False

        return True

    def get_name(self):
        """Returns the name of the game piece for printing the board"""
        if self.get_owner():
            return "Blue General"
        return "Red General"

# Basic Tests
# game = JanggiGame()
# #
# game.print_board()
# game.make_move("a7","a6")
# game.print_board()
# game.make_move("i4","i5")
# game.print_board()
# game.make_move("a6","a5")
# game.print_board()
# game.make_move("i5","i6")
# game.print_board()
# game.make_move("a5","a4")
# game.print_board()

# # Move a guard around
# game.make_move("e9", "e8")
# game.make_move('pass', 'pass')
# game.make_move("e8", "f8")
# game.make_move('pass', 'pass')
# game.make_move("f8", "e9")
# game.make_move('pass', 'pass')
# game.make_move("e9", "d8")
# game.make_move('pass', 'pass')
# game.make_move("d8", "d9")
# game.make_move('pass', 'pass')
# game.make_move("d9", 'e8')

# # Move a chariot around
# game.make_move("i7", "h7")
# game.make_move("pass", "pass")
# game.make_move("i10", "i4")
# game.make_move("pass", "pass")
# game.make_move("i4", "i9")
# game.make_move("pass", "pass")
# game.make_move("i9", "f9")
# game.make_move("pass", "pass")
# game.make_move("f9", "e8")
# game.make_move("e9", "e10")
# game.make_move("pass", "pass")
# game.make_move("f9", "e9")
# game.make_move("pass", "pass")
# game.make_move("d10", "d9")
# game.make_move("pass", "pass")
# game.make_move("f10", "f9")
# game.make_move("pass", "pass")
# game.make_move("e9", "f10")
# game.make_move("pass", "pass")
# game.make_move("f10", "d8")
# game.make_move("pass", "pass")
# game.print_board()
# game.make_move("d8", "f8")
# game.make_move("pass", "pass")
# game.make_move("f8", "d10")
# game.print_board()

# # Move a general around
# game.make_move('e9', 'e10')
# game.make_move('pass', 'pass')
# game.make_move('e10', 'e9')
# game.make_move('pass', 'pass')
# game.make_move('e9', 'd8')
# game.make_move('pass', 'pass')
# game.make_move('d8', 'c8')
# # Move a solider around
# # game.make_move('pass', 'pass')
# # game.make_move('c4', 'c5')
# # game.make_move('pass', 'pass')
# # game.make_move('c5', 'c6')
# # game.make_move('pass', 'pass')
# # game.make_move('c6', 'c7')
# # game.make_move('pass', 'pass')
# # game.make_move('c7', 'd7')
# # game.make_move('pass', 'pass')
# # game.make_move('d7', 'd8')
# # game.make_move('pass', 'pass')
# # game.make_move('d8', 'e9')
# # game.make_move('pass', 'pass')
# # game.make_move('e9', 'f10')
# # game.make_move('pass', 'pass')
# # game.make_move('f10', 'g10')
# print()
# game.print_board()
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

