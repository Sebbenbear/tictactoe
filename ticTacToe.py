"""
TIC TAC TOE
"""

def store_names():
    player_0 = input('Who will be naughts? ')
    player_X = input('Who will be crosses? ')
    return player_0, player_X

def display_game_board():
    i = 1
    while i < 10:
        print('-------------')
        row_count = 0
        while row_count < 3:
            print('| ' + str(i) + ' ', end='')
            row_count = row_count + 1
            i = i + 1
        print('|')
    print('-------------')

def display_game_board(grid):
    print('-' * 13)
    print('| ' + grid[0] + ' | ' + grid[1] + ' | ' + grid[2] + ' |')
    print('-' * 13)
    print('| ' + grid[3] + ' | ' + grid[4] + ' | ' + grid[5] + ' |')
    print('-' * 13)
    print('| ' + grid[6] + ' | ' + grid[7] + ' | ' + grid[8] + ' |')
    print('-' * 13)

def display_welcome(player_0, player_X):
    print('Welcome ' + player_0 + ' and ' + player_X + '!')

def create_game_grid():
    numbers = []
    for i in range(1, 10):
        numbers.append(str(i))
    return numbers

def place_symbol(grid, player, token):
    input_square = int(input(player + ', select from 1-9 the spot you would like to choose.'))
    # do checks - come back to this
    grid[input_square-1] = token
    return grid

def is_row(grid, token, first, second, third):
    return grid[first] == token and grid[second] == token and grid[third] == token

def check_win(grid, token):
    player_won = False

    if (is_row(grid, token, 0, 1, 2) or is_row(grid, token, 3, 4, 5) or is_row(grid, token, 6, 7, 8)):
        # add checks for diagonals
        player_won = True

    return player_won

def run():
    grid = create_game_grid()
    player_0, player_X = store_names()

    token_map = {player_0:'O', player_X:'X'}

    display_welcome(player_0, player_X)
    display_game_board(grid)

    for turn in range(9):
        if turn % 2 == 0:
            current_player = player_0
        else:
            current_player = player_X

        current_token = token_map[current_player]
        grid = place_symbol(grid, current_player, current_token)
        display_game_board(grid)
        

        player_won = check_win(grid, current_token)
        if player_won:
            print(current_player + ' won the game!')
            return
        

if __name__ == '__main__':
    run()
