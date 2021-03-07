#  Name: Brandon Lenz
#  Date: 2/19/2021
#  Description: The ancient game of Janggi!  This project outlines the logic to get started playing Janggi via the
#  console.  Most rules have been built in, but your Generals are allowed to see each other & you cannot customize
#  your start.

# Other documents
#  Additional planning - https://docs.google.com/spreadsheets/d/13MTVMrmjhH53qYzgSoDzK7Y_Y0INGk79RlSjAaf7e8o/edit#gid=0
#  https://www.pychess.org/\
#  FEN - rbna1abnr/4k4/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/4K4/RBNA1ABNR w - - 0 1

# Ways to improve this for performance
# 1) Keep a list of all player pieces that are not captured, one for each player
# 2) Add the row and column concept to each piece and store it on the piece, this will help the checkmate search

#######
# "DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"

# Initializing the board
# The board will be initialized upon the creation of an instance of the JanggiGame class.  Nested dictionary will be
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
# I'm not entirely sure what state is meant to refer to here since state was referred to in the README as 'UNFINISHED'
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


# noinspection SpellCheckingInspection
class JanggiGame:
    """Builds the board and contains the methods that help the board to function"""

    def __init__(self):
        """Creates the board and the game.  The board is defined by nested dictionaries.  The first level is an entry
        for each row (a, b, c etc) and then within each row the columns for that one.  This board is prebuilt in the
        class so that it is built consistently.  We are passing False to the various game piece child classes to create
        a red piece and True to create a blue piece.  We also are storing the game_state here & also whose turn it
        currently is."""
        self._game_state = None
        self._blue_turn = True
        self._red_check = False
        self._blue_check = False
        self._blue_gen = 'e9'
        self._red_gen = 'e2'
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

    def get_blue_gen(self):
        """Returns the location of the blue general"""
        return self._blue_gen

    def get_red_gen(self):
        """Returns the location the red general"""
        return self._red_gen

    def set_blue_gen(self, square):
        """Updates the location of the blue general"""
        self._blue_gen = square

    def set_red_gen(self, square):
        """Updates the location of the red general"""
        self._red_gen = square

    def get_game_state(self):
        """Returns the state of the game as UNFINISHED or shows the victor.  None is used to old the unfinished state
        for ease of referencing in the program.  If none though, we will return UNFINISHED"""
        if self._game_state is None:
            return "UNFINISHED"
        return self._game_state

    def is_in_check(self, player):
        """Intakes a player as either red or blue and returns if that player is n check.  To perform this, we need need
        to iterate through a player's game pieces and see if any of them have valid moves that would place them on the
        opponent's general.  For example, if there is a solider being checked, we would want to check all of the
        potential moves for that soldier and see if any of them wind up placing them on the square as the general.  If
        that is true and the general also then does not have any moves that put them in a spot where they are not in
        check, then the game is now checkmate."""
        # print('Starting the check now', player)
        if type(player) != str:
            return False

        player = player.lower()
        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        # Start as checking red
        is_blue = False
        general_col = self._red_gen[0].lower()
        general_row = int(self._red_gen[1:])

        # Flip to blue if needed
        if player == 'blue':
            is_blue = not is_blue
            general_col = self._blue_gen[0].lower()
            general_row = int(self._blue_gen[1:])

        # iterate through the board
        for col in layout:
            for row in range(1, 11):
                square = self._board[col][row]
                # Check if blue is in check
                if is_blue and square is not None and not square.get_owner():
                    # We have now determined this is a red piece, check if it has a valid move to the general
                    if square.check_valid_moves(col, row, general_col, general_row, self):
                        return True

                # Check if red is in check
                elif not is_blue and square is not None and square.get_owner():
                    # We have now determined this is a blue piece, check if it has a valid move to the general
                    if square.check_valid_moves(col, row, general_col, general_row, self):
                        return True

        return False

    def make_move(self, source, destination):
        """
        Allows a move to occur and outlines the logic to ensure that said move is valid.  This function performs several
        checks to ensure that players are moving valid pieces on their turn, ensures they are not trying to capture
        their own pieces, calls appropriate methods to ensure they are making the proper move for the piece they selected
        """
        # print("Attempting", source, "==>", destination)

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
            return False
        elif not self._blue_turn and source_square.get_owner():
            # Can't move a blue piece on red's turn
            return False

        if destination_square is not None:
            if source_square.get_owner() == destination_square.get_owner():
                # The pieces on the source and destination squares are owned by the same player
                # You can't capture your own piece, it's poor battle tactics!
                return False

        if source_square.check_valid_moves(source_col, source_row, destination_col, destination_row, self):
            self._board[destination_col][destination_row] = source_square
            self._board[source_col][source_row] = None

            # Ensure this move does not place the user in check.  If it did, restore the board state
            # and then return False
            if (self._blue_turn and self.is_in_check('blue')) or (not self._blue_turn and self.is_in_check('red')):
                self._board[source_col][source_row] = source_square
                self._board[destination_col][destination_row] = destination_square

                if type(source_square).__name__ == "General" and self._blue_turn:
                    general_source = source_col + str(source_row)
                    self.set_blue_gen(general_source)
                elif type(source_square).__name__ == "General" and not self._blue_turn:
                    general_source = source_col + str(source_row)
                    self.set_red_gen(general_source)

                return False

            # Check if this move left the opponent in check
            if self._blue_turn:
                self._red_check = self.is_in_check('red')
            else:
                self._blue_check = self.is_in_check('blue')

            # Check if checkmate.  We look only need to check for mate, if they were already in check.  To perform this
            # check, we need to find all valid moves for a player's pieces and see if that places them not in check.
            if self._red_check and self.is_checkmate(False):
                self._game_state = 'BLUE_WON'
            elif self._blue_check and self.is_checkmate(True):
                self._game_state = 'RED_WON'

            self._blue_turn = not self._blue_turn

            return True

        return False

    def is_checkmate(self, is_blue):
        """This method is called at the completion of a move when a player is in check.  We will check all valid moves
        for a player to determine if they have been checkmated.

        is_blue will be True if we are checking checkmate on blue
        is_blue will be False if we are checking checkmate on red

        This is horribly inefficient O^4  :(  """

        # This first set of loops is used to locate the pieces for the player
        for col_piece in self._board.keys():
            for row_piece in self._board[col_piece]:
                # Store this square if it should be checked
                source_square = self._board[col_piece][row_piece]
                if source_square is not None and source_square.get_owner() == is_blue:

                    # Iterates across the board to check for valid moves for this above piece
                    for col_move in self._board.keys():
                        for row_move in self._board[col_move]:

                            # If this is a valid move for this piece we move to our next step
                            if source_square.check_valid_moves(col_piece, row_piece, col_move, row_move, self):
                                destination_square = self._board[col_move][row_move]

                                self._board[col_piece][row_piece] = None
                                self._board[col_move][row_move] = source_square

                                # If the move was valid, temporarily make the move and see if in still in check
                                # If we are still in check, we will undo the move and the check the next valid move
                                # If we are not still in check, we undo the move and return out of the method

                                if is_blue and not self.is_in_check('blue'):

                                    # Reset the general location if we are checking the general
                                    if type(source_square).__name__ == "General" and is_blue:
                                        general_source = col_piece + str(row_piece)
                                        self.set_blue_gen(general_source)
                                    elif type(source_square).__name__ == "General" and not is_blue:
                                        general_source = col_piece + str(row_piece)
                                        self.set_red_gen(general_source)

                                    self._board[col_piece][row_piece] = source_square
                                    self._board[col_move][row_move] = destination_square
                                    return False
                                elif not is_blue and not self.is_in_check('red'):

                                    # Reset the general location if we are checking the general
                                    if type(source_square).__name__ == "General" and is_blue:
                                        general_source = col_piece + str(row_piece)
                                        self.set_blue_gen(general_source)
                                    elif type(source_square).__name__ == "General" and not is_blue:
                                        general_source = col_piece + str(row_piece)
                                        self.set_red_gen(general_source)

                                    self._board[col_piece][row_piece] = source_square
                                    self._board[col_move][row_move] = destination_square
                                    return False

                                # This move did not clear checkmate, so we reset and try again

                                # Reset the general location if we are checking the general
                                if type(source_square).__name__ == "General" and is_blue:
                                    general_source = col_piece + str(row_piece)
                                    self.set_blue_gen(general_source)
                                elif type(source_square).__name__ == "General" and not is_blue:
                                    general_source = col_piece + str(row_piece)
                                    self.set_red_gen(general_source)

                                self._board[col_piece][row_piece] = source_square
                                self._board[col_move][row_move] = destination_square
        return True

    def space_open(self, col, row):
        """Checks an input coordinator to determine if a space is open.  This method is called by the make_move method
        and relies on the coordinate breakdown that is performed in the make_move method."""
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

    def get_square(self, col, row):
        """Returns the contents of a square"""
        return self._board[col][row]


class GamePiece:
    """A parent class to create game pieces.  This class initializes the information that is consistent across all
    types of game pieces"""
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
        """Returns the boolean of whether or not this is a blue game piece.  True is blue"""
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

        if (destination_row < 4 or source_row < 4) and (destination_row > 7 or source_row > 7):
            return False

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

        if not in_palace and row_move == 1 and col_move == 1:
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
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """Checks if the input move is valid and returns True / False based on that.
        This piece moves similar to the knight in western chess, in an L shape.  It can however be blocked.
        It will first move 1 space vertically or horizontally towards it's destination and then 2 space
        diagonally, if it cannot make the first 1/2 of the move; it is blocked.

        It's like a mega knight since it has a larger L
        """
        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        col1 = layout.index(source_col)
        col2 = layout.index(destination_col)
        col_move = col2 - col1

        row_move = destination_row - source_row

        # col_move or row_move must be 2 and the other must be 1
        criteria1 = abs(col_move) == 3 and abs(row_move) == 2
        criteria2 = abs(col_move) == 2 and abs(row_move) == 3
        if not (criteria1 or criteria2):
            return False

        # Check if the vertical move is blocked and the diagonal spot that is crossed
        if abs(row_move) == 3 and (not game_board.space_open(source_col, source_row + row_move/3) or not game_board.space_open(layout[int(col1 + col_move/2)], source_row + row_move/3*2)):
            return False
        # Check if the horizontal move is blocked and the diagonal spot that is crossed
        elif abs(row_move) == 2 and (not game_board.space_open(layout[int(col1 + col_move/3)], source_row) or not game_board.space_open(layout[int(col1 + col_move/3*2)], source_row + row_move/2)):
            return False

        return True

    def get_name(self):
        """Returns the name of the game piece for printing the board"""
        if self.get_owner():
            return "Blue Elephant"
        return "Red Elephant"


class Cannon(GamePiece):
    """Outlines the Cannon Game Piece"""
    def check_valid_moves(self, source_col, source_row, destination_col, destination_row, game_board):
        """Checks if the input move is valid and returns True / False based on that.
        Cannon cannot capture cannon & cannon cannot jump over cannon
        Must have exactly 1 piece between source and destination from either team
        """
        in_palace = False
        if self.inside_palace(source_col, source_row, destination_col, destination_row):
            in_palace = not in_palace

        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        col1 = layout.index(source_col)
        col2 = layout.index(destination_col)
        col_move = col2 - col1

        # noinspection SpellCheckingInspection
        dest_square = game_board.get_square(destination_col, destination_row)

        if dest_square is not None and type(dest_square).__name__ == 'Cannon':
            return False

        row_move = destination_row - source_row

        # Diagonal rules
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

        pieces_jumped = 0

        if not in_palace and col_move == 0:
            # Column is being held constant
            if 0 > row_move:
                increment = -1
            else:
                increment = 1

            for path in range(increment, row_move, increment):
                square = game_board.get_square(source_col, source_row + path)
                if square is not None and type(square).__name__ != "Cannon":
                    pieces_jumped += 1
                elif type(square).__name__ == "Cannon":
                    return False

            if pieces_jumped != 1:
                return False

        elif not in_palace and row_move == 0:
            # Row is being held constant
            if 0 > col_move:
                increment = -1
            else:
                increment = 1

            for path in range(increment, col_move, increment):
                square = game_board.get_square(layout[col1 + path], source_row)
                if square is not None and type(square).__name__ != "Cannon":
                    pieces_jumped += 1
                elif type(square).__name__ == "Cannon":
                    return False

            if pieces_jumped != 1:
                return False

        elif in_palace and abs(row_move) == 2 and abs(col_move) == 2:
            # Check for valid palace diagonals
            # If we are trying to move two diagonal spaces, the middle must be empty
            square_blue = game_board.get_square('e', 9)
            square_red = game_board.get_square('e', 2)
            if source_row > 5 and square_red is not None and type(square_red).__name__ != "Cannon":
                return False
            elif source_row < 5 and square_blue is not None and type(square_blue).__name__ != "Cannon":
                return False

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
        This piece moves similarly to the knight in western chess, in an L shape.  It can however be blocked.
        It will first move 1 space vertically or horizontally towards it's destination and then 1 space
        diagonally, if it cannot make the first 1/2 of the move; it is blocked.
        """
        layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        col1 = layout.index(source_col)
        col2 = layout.index(destination_col)
        col_move = col2 - col1

        row_move = destination_row - source_row

        # col_move or row_move must be 2 and the other must be 1
        criteria1 = abs(col_move) == 2 and abs(row_move) == 1
        criteria2 = abs(col_move) == 1 and abs(row_move) == 2
        if not criteria1 and not criteria2:
            return False

        # Check if the vertical move is blocked
        if abs(row_move) == 2 and not game_board.space_open(source_col, source_row + row_move/2):
            return False
        # Check if the horizontal move is blocked
        elif abs(row_move) == 1 and not game_board.space_open(layout[int(col1 + col_move/2)], source_row):
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

        if destination_row == 4 or destination_row == 5 or destination_row == 6 or destination_row == 7:
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

        if destination_row == 4 or destination_row == 5 or destination_row == 6 or destination_row == 7:
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

        # Update the stored general coordinates
        general_source = source_col + str(source_row)
        general_destination = destination_col + str(destination_row)

        if game_board.get_blue_gen() == general_source:
            game_board.set_blue_gen(general_destination)
        elif game_board.get_red_gen() == general_source:
            game_board.set_red_gen(general_destination)

        return True

    def get_name(self):
        """Returns the name of the game piece for printing the board"""
        if self.get_owner():
            return "Blue General"
        return "Red General"


def main():
    """The main function that is used for running the script locally and testing"""
    game = JanggiGame()
    game.print_board()


if __name__ == "__main__":
    main()
