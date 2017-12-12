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

def place_symbol(grid, player, token_map):
    input_square = int(input(player + ', select from 1-9 the spot you would like to choose.'))
    # do checks - come back to this
    grid[input_square-1] = token_map[player]
    return grid

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

        grid = place_symbol(grid, current_player, token_map)
        display_game_board(grid)

if __name__ == '__main__':
    run()
