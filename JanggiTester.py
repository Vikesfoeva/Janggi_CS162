# Tests for Janggi

import unittest
import JanggiGame


class TestJanggi(unittest.TestCase):
    """
    Contains unit tests for Janggi Game
    """

    def setUp(self):
        self.game = JanggiGame.JanggiGame()

    def test_Solider_Capture(self):
        self.assertTrue(self.game.make_move("a7", "a6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("i4", "i5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("a6", "a5"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("i5", "i6"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("a5", "a4"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_Horse_capture(self):
        self.assertTrue(self.game.make_move("c10", "d8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c1", "d3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("e7", "e6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e4", "e5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c4", "c5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("c6", "c5"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e5", "e6"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("d8", "e6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("d3", "c5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("h10", "g8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("h1", "i3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("g7", "h7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("g4", "f4"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("h7", "h6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("i4", "i5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue( self.game.make_move("h6", "h5"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("i5", "i6"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("g8", "g8"))
        self.assertTrue(self.game.make_move("i3", "h5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("g8", "g8"))
        self.assertTrue(self.game.make_move("i6", "h6"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("g8", "h6"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_horse_cannot_jump_own_piece(self):
        self.assertTrue(self.game.make_move("c10", "d8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c1", "d3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("c7", "d7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c4", "d4"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.make_move("d8", "c6"))
        self.assertTrue(self.game.make_move("d8", "d8"))
        self.assertFalse(self.game.make_move("d3", "d6"))
        self.assertTrue(self.game.make_move("d3", "d3"))
        self.assertTrue(self.game.make_move("h10", "g8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertFalse(self.game.make_move("h2", "g3"))
        self.assertFalse(self.game.make_move("g8", "h6"))
        self.assertTrue(self.game.make_move("g8", "g8"))
        self.assertFalse(self.game.make_move("g3", "g5"))

    def test_cannon_no_diag(self):
        self.assertFalse(self.game.make_move("b8", "d6"))

    def test_no_forward_no_screen(self):
        self.assertFalse(self.game.make_move("b8", "b7"))

    def test_horse_l_too_big(self):
        self.assertFalse(self.game.make_move("h10", "f8"))

    def test_horse_l_too_big_2(self):
        self.assertFalse(self.game.make_move("c10", "d7"))

    def test_elephant_bad_moves(self):
        self.assertTrue(self.game.make_move("e9", "f8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e2", "f3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.make_move("f8", "g8"))
        self.assertTrue(self.game.make_move("f8", "f8"))
        self.assertFalse(self.game.make_move("f3", "f4"))
        self.assertTrue(self.game.make_move("f3", "f3"))
        self.assertTrue(self.game.make_move("f10", "e10"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("f1", "e1"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.make_move("f8", "f10"))
        self.assertTrue(self.game.make_move("f8", "f8"))
        self.assertFalse(self.game.make_move("f3", "f1"))
        self.assertTrue(self.game.make_move("f3", "f3"))
        self.assertTrue(self.game.make_move("e10", "e9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e1", "e2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.make_move("f8", "e9"))
        self.assertTrue(self.game.make_move("f8", "f8"))
        self.assertFalse(self.game.make_move("f3", "e2"))

    def test_check_one(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c1", "d3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("b10", "d7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("b3", "e3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("c10", "d8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("h1", "g3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("e7", "e6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e3", "e6"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("h8", "c8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("d3", "e5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("c8", "c4"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e5", "c4"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("i10", "i8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("g4", "f4"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("i8", "f8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("g3", "h5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("h10", "g8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e6", "e3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e9", "d9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_turn_pass(self):
        self.assertTrue(self.game.make_move("a7", "b7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a4", "a4"))
        self.assertTrue(self.game.make_move("b7", "b6"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_blue_start(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_turn_takes(self):
        self.assertFalse(self.game.make_move("a1", "a3"))
        self.assertTrue(self.game.make_move("a7", "a6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a1", "a2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("d10", "d9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c4", "c5"))
        self.assertFalse(self.game.is_in_check('red'))

    def test_state(self):
        self.assertTrue(self.game.make_move("e7", "f7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e4", "e5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertEqual(self.game.get_game_state(), "UNFINISHED")

    def test_blue_chariot_move(self):
        self.assertTrue(self.game.make_move("a10", "a8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a1", "a2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("a8", "a9"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_chariot_horizonatal(self):
        self.assertTrue(self.game.make_move("a10", "a9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a1", "a2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("a9", "c9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a2", "a3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("c9", "b9"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_blue_cannon(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a4", "a5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("a7", "b7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a5", "a6"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("b8", "b6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a6", "a7"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("b6", "e6"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_char_forward(self):
        self.assertTrue(self.game.make_move("a10", "a8"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_horse_for(self):
        self.assertTrue(self.game.make_move("h10", "g8"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_other_horse_for(self):
        self.assertTrue(self.game.make_move("c10", "d8"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_soldier_for(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_chariot_red_for(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a1", "a3"))
        self.assertFalse(self.game.is_in_check('red'))

    def red_solider_for(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c4", "c5"))
        self.assertFalse(self.game.is_in_check('red'))

    def test_more_elephant_moves(self):
        self.assertTrue(self.game.make_move("b10", "d7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("b1", "d4"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("e7", "e6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e4", "e5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("g10", "e7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("g1", "e4"))
        self.assertFalse(self.game.is_in_check('red'))

    def test_guard_moves(self):
        self.assertTrue(self.game.make_move("d10", "d9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("d1", "d2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("f10", "f9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("f1", "f2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("d9", "d8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("d2", "d3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("f9", "f8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("f2", "f3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("e9", "e10"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e2", "e1"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("d8", "e9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("d3", "e2"))
        self.assertFalse(self.game.is_in_check('red'))

    def test_general_moves(self):
        self.assertTrue(self.game.make_move("e9", "f8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e2", "f3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("f8", "e8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("f3", "e3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("e8", "d8"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e3", "d3"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("d8", "d9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("d3", "d2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("d9", "e9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("d2", "e2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("e9", "e10"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("e2", "e1"))
        self.assertFalse(self.game.is_in_check('red'))

    def test_cannon_moves(self):
        self.assertTrue(self.game.make_move("a7", "b7"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a4", "a5"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("b8", "b4"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_blue_char_side(self):
        self.assertTrue(self.game.make_move("a10", "a9"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a1", "a2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("a9", "c9"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_soldier_sideways(self):
        self.assertTrue(self.game.make_move("c7", "b7"))
        self.assertFalse(self.game.is_in_check('blue'))

    def test_char_side_way(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a1", "a2"))
        self.assertFalse(self.game.is_in_check('red'))
        self.assertTrue(self.game.make_move("g7", "g6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("a2", "c2"))
        self.assertFalse(self.game.is_in_check('red'))

    def test_soldier_side(self):
        self.assertTrue(self.game.make_move("c7", "c6"))
        self.assertFalse(self.game.is_in_check('blue'))
        self.assertTrue(self.game.make_move("c4", "d4"))
        self.assertFalse(self.game.is_in_check('red'))


if __name__ == "__main__":
    unittest.main()