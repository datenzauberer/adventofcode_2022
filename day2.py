'''
https://adventofcode.com/2022/day/2

Summary:
Rock     1 A X
Paper    2 B Y
Scissors 3 C Z

Rules for Winning
R1 Rock defeats Scissors
R2 Scissors defeats Paper, and
R3 Paper defeats Rock
'''

TEST_INPUT = '''A Y
B X
C Z
'''

DRAW_SCORE = 3
WIN_SCORE = 6

SHAPE2SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3,
}

WINNING_RULES = [(1, 3), (3, 2), (2, 1)]  # x wins agains y


def sum_game_with(calc_one_round):
    '''can be configured with the algo for one round'''

    def process_input(str_input):
        return sum(calc_one_round(line) for line in str_input.splitlines())

    return process_input


def calc_result_round(str_input):
    my_shape = determine_points_for_my_shape(str_input)
    opponent_shape = determine_points_for_opponent_shape(str_input)
    return my_shape + determine_points_for_result(my_shape, opponent_shape)


def determine_points_for_my_shape(str_input):
    return SHAPE2SCORE[str_input[2]]


def determine_points_for_opponent_shape(str_input):
    return SHAPE2SCORE[str_input[0]]


def determine_points_for_result(my_shape, opponent_shape):
    if my_shape == opponent_shape:
        return DRAW_SCORE
    if (my_shape, opponent_shape) in WINNING_RULES:
        return WIN_SCORE
    return 0


sum_game = sum_game_with(calc_result_round)
assert sum_game(TEST_INPUT) == 15
day2_input = open("day2-input.txt", "r").read()
print(f'{sum_game(day2_input)=}')

# part B

map_column2points = {
    'X': 0,
    'Y': DRAW_SCORE,
    'Z': WIN_SCORE,
}

resultpoints_and_opponentshapes2myshape = {
    (0, 1): 3,
    (0, 3): 2,
    (0, 2): 1,
    (6, 3): 1,
    (6, 2): 3,
    (6, 1): 2
}


def calc_result_indicated_round(str_input):
    opponent_shape = determine_points_for_opponent_shape(str_input)
    result_points = map_column2points[str_input[2]]
    my_shape = opponent_shape
    if result_points != DRAW_SCORE:
        my_shape = resultpoints_and_opponentshapes2myshape[
            result_points, opponent_shape]
    return result_points + my_shape

sum_indicated = sum_game_with(calc_result_indicated_round)
assert sum_indicated(TEST_INPUT) == 12
print(f'{sum_indicated(day2_input)=}')
