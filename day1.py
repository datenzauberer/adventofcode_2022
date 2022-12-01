'''
https://adventofcode.com/2022/day/1
'''

import re


def elves_calories(str_input):
    return [sum([int(i) for i in elf.splitlines()])
            for elf in re.split(r"(?m)^\s*$\s*", str_input)]


def calories_of_elf_with_most_energy(str_input):
    return max(elves_calories(str_input))


def calories_of_top_three_elves(str_input):
    _elves_calories = elves_calories(str_input)
    _elves_calories.sort(reverse=True)
    return sum(_elves_calories[0:3])


TEST_INPUT = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

assert calories_of_elf_with_most_energy(TEST_INPUT) == 24000

day1_input = open("day1-input.txt", "r").read()
print(f'{calories_of_elf_with_most_energy(day1_input)=}')

assert calories_of_top_three_elves(TEST_INPUT) == 45000
print(f'{calories_of_top_three_elves(day1_input)=}')
