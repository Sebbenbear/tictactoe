import unittest
import ticTacToe

class TestTicTacToe(unittest.TestCase):

    # Test creation of the game grid
    def test_create_game_grid(self):
        expected = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        actual = ticTacToe.create_game_grid()
        self.assertEqual(expected, actual)
        
    # Test is_valid_number
    def test_is_valid_number_success_0(self):
        actual = ticTacToe.is_valid_number(0)
        self.assertTrue(actual)

    def test_is_valid_number_fail_0(self):
        actual = ticTacToe.is_valid_number(-1)
        self.assertFalse(actual)

    def test_is_valid_number_fail_1(self):
        actual = ticTacToe.is_valid_number(9)
        self.assertFalse(actual)

    # Tests checking the validity of the player's move
    def test_is_valid_move_success_0(self):
        grid = ticTacToe.create_game_grid()
        input_square = 1
        actual = ticTacToe.is_valid_move(input_square, grid)
        self.assertTrue(actual)

    def test_is_valid_move_fail_0(self):
        grid = ticTacToe.create_game_grid()
        grid[0] = 'O'
        input_square = 0
        actual = ticTacToe.is_valid_move(input_square, grid)
        self.assertFalse(actual)

    def test_is_valid_move_fail_1(self):
        grid = ticTacToe.create_game_grid()
        grid[8] = 'X'
        input_square = 8
        actual = ticTacToe.is_valid_move(input_square, grid)
        self.assertFalse(actual)

    # Check if the token has won the game
    def test_check_win_success_0(self):
        grid = ticTacToe.create_game_grid()
        token = 'X'
        grid[2] = token
        grid[5] = token
        grid[8] = token
        actual = ticTacToe.check_win(grid, token)
        self.assertTrue(actual)

    def test_check_win_fail_0(self):
        grid = ticTacToe.create_game_grid()
        token = 'X'
        grid[2] = token
        grid[5] = token
        grid[1] = token
        actual = ticTacToe.check_win(grid, token)
        self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()
