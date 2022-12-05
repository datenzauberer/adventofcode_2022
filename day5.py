'''
https://adventofcode.com/2022/day/5

requires python >= 3.8
PEP 572 introduces Assignment Expressions
'''
import re
from dataclasses import dataclass


def process_moves_with_move_function(str_input, move_function):
    (str_stack, str_moves) = split_input_string_to_stack_and_moves(str_input)
    stacks = build_stacks_from_lines(str_stack)
    moves = [Move.parse(line) for line in str_moves]
    for move in moves:
        move_function(stacks, move)
    return "".join([x[-1] for x in stacks])


def split_input_string_to_stack_and_moves(str_input):
    str = re.split(r"(?m)^\s*$\s*", str_input)
    starting_stack = str[0].splitlines()
    moves = str[1].splitlines()
    return (starting_stack, moves)


def build_stacks_from_lines(str_stack):
    chars_per_stack = 4
    len_line = len(str_stack[0])
    num_of_stacks = (len_line + 1) // chars_per_stack
    stacks = [[] for __ in range(num_of_stacks)]
    for line in reversed(str_stack[0:-1]):
        crates = [line[i] for i in range(1, len(line), chars_per_stack)]
        for i in range(num_of_stacks):
            if (crate := crates[i]) != ' ':
                stacks[i].append(crate)
    return stacks


def move_one_by_one(stacks, move):
    for __ in range(move.quantity):
        stacks[move.to_crate - 1].append(stacks[move.from_crate - 1].pop())
    return


def move_multiple_crates_at_once(stacks, move):
    crates = stacks[move.from_crate - 1][-move.quantity:]
    stacks[move.from_crate - 1] = stacks[move.from_crate - 1][:-move.quantity]
    stacks[move.to_crate - 1] += crates
    return


@dataclass
class Move:
    quantity: int
    from_crate: int
    to_crate: int

    @classmethod
    def parse(cls, str_input):
        pattern = re.compile('move (.*) from (.*) to (.*)')
        groups = list(map(int, pattern.match(str_input).groups()))
        return cls(groups[0], groups[1], groups[2])


def test_it():
    str_input = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
    _move = Move.parse("move 1 from 2 to 3")
    assert _move.quantity == 1
    assert _move.from_crate == 2
    assert _move.to_crate == 3
    assert process_moves_with_move_function(
        str_input, move_one_by_one) == "CMZ"
    assert process_moves_with_move_function(
        str_input, move_multiple_crates_at_once) == "MCD"


test_it()
str_input = open("day5-input.txt", "r").read()
result = process_moves_with_move_function(str_input, move_one_by_one)
print("part a: head of stacks move one by one: {}", result)
result = process_moves_with_move_function(str_input,
                                          move_multiple_crates_at_once)
print("part b: head of stacks move multiple crates at once: {}", result)
