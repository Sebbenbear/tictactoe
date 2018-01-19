"""
TicTacToe

This is a small Tic Tac Toe game between 2 players.
"""

def store_names():
    """
    Stores the players names to use in the game.
    """
    player_nought = input('Who will be naughts? ')
    player_cross = input('Who will be crosses? ')
    return player_nought, player_cross

def display_game_board(grid):
    """
    Displays the game board on the screen for the players.
    """
    print('-' * 13)
    print('| ' + grid[0] + ' | ' + grid[1] + ' | ' + grid[2] + ' |')
    print('-' * 13)
    print('| ' + grid[3] + ' | ' + grid[4] + ' | ' + grid[5] + ' |')
    print('-' * 13)
    print('| ' + grid[6] + ' | ' + grid[7] + ' | ' + grid[8] + ' |')
    print('-' * 13)

def display_welcome(player_nought, player_cross):
    """
    Displays the welcome message for the players.
    """
    print('Welcome ' + player_nought + ' and ' + player_cross + '!')

def create_game_grid():
    """
    Creates the game grid for the players to put tokens on.
    """
    numbers = []
    for i in range(1, 10):
        numbers.append(str(i))
    return numbers

def is_valid_number(input_square):
    """
    Checks if the player's chosen square is a valid place on the board.
    """
    return input_square >= 0 and input_square <= 8

def is_valid_move(input_square, grid):
    """
    Checks if the player's chosen square doesn't already contain a token.
    """
    return grid[input_square] != 'X' and grid[input_square] != 'O'

def get_user_input(player, token, grid):
    """
    Get user input from the player, and ensure it is both a valid number, and
    can be put on a valid place on the board.
    """
    is_valid = False
    while not is_valid:
        try:
            input_square = int(input(player + " (" + token + ")" + ', select from 1-9 the spot you would like to choose: ')) - 1
            if not is_valid_number(input_square):
                print("That's not a valid number on the game board. Try again.")
                continue
            if not is_valid_move(input_square, grid):
                print("Someone's already placed a move here. Try again.")
                continue

            # If we've got this far, the input is valid and can be used.
            is_valid = True

        except ValueError:
            print("That's not a number! Try again.")

    return input_square

def place_symbol(grid, player, token):
    """
    Places the player's symbol on the board.
    """
    input_square = get_user_input(player, token, grid)
    grid[input_square] = token
    return grid

def token_matches(grid, token, first, second, third):
    """
    Checks if the tokens match the correct squares
    """
    return grid[first] == token and grid[second] == token and grid[third] == token

def check_win(grid, token):
    """
    Check if a player has won the game.
    """
    player_won = False

    if token_matches(grid, token, 0, 1, 2) or \
        token_matches(grid, token, 3, 4, 5) or \
        token_matches(grid, token, 6, 7, 8) or \
        token_matches(grid, token, 0, 3, 6) or \
        token_matches(grid, token, 1, 4, 7) or \
        token_matches(grid, token, 2, 5, 8) or \
        token_matches(grid, token, 0, 4, 8) or \
        token_matches(grid, token, 6, 4, 2):
        player_won = True

    return player_won

def run():
    """
    The main game loop
    """
    grid = create_game_grid()
    player_nought, player_cross = store_names()

    token_map = {player_nought:'O', player_cross:'X'}

    display_welcome(player_nought, player_cross)
    display_game_board(grid)

    for turn in range(9):
        if turn % 2 == 0:
            current_player = player_nought
        else:
            current_player = player_cross

        current_token = token_map[current_player]
        grid = place_symbol(grid, current_player, current_token)
        display_game_board(grid)

        player_won = check_win(grid, current_token)
        if player_won:
            print(current_player + ' won the game!')
            return

    print('Nobody won this time!')

if __name__ == '__main__':
    run()
