'''
https://adventofcode.com/2022/day/4
'''

TEST_INPUT = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


def determine_num_of_fully_contained_assignments(str_input):
    return apply_filter_on_assignments(
        str_input,
        does_one_range_fully_contain_the_other)


def determine_num_of_partially_contained_assignments(str_input):
    return apply_filter_on_assignments(
        str_input,
        does_one_range_partially_contain_the_other)


def apply_filter_on_assignments(str_input, filtercondition):
    return len(list(filter(filtercondition, determins_assignments(str_input))))


def determins_assignments(str_input):
    return map(convert_line2elve_assignment, str_input.splitlines())


def convert_line2elve_assignment(str_input):
    return list(map(convert_str2range, str_input.split(",")))


def convert_str2range(str_input):
    r = list(map(int, str_input.split('-')))
    return range(r[0]-1, r[1])


def does_one_range_partially_contain_the_other(a):
    return is_range_partially_contained_in(a[0], a[1]) or \
        is_range_partially_contained_in(a[1], a[0])


def does_one_range_fully_contain_the_other(a):
    return is_range_fully_contained_in(a[0], a[1]) \
        or is_range_fully_contained_in(a[1], a[0])


def is_range_fully_contained_in(a, b):
    if b.start <= a.start:
        if b.stop >= a.stop:
            return True
    return False


def is_range_partially_contained_in(a, b):
    return b.start in a or b.stop-1 in a


def test_it():
    assert is_range_fully_contained_in(range(3, 7), range(2, 8))
    assert not is_range_fully_contained_in(range(3, 7), range(4, 8))
    assert not is_range_fully_contained_in(range(2, 8), range(3, 7))

    assert not is_range_partially_contained_in(range(2, 4), range(6, 8))
    assert is_range_partially_contained_in(range(2, 8), range(3, 7))
    assert is_range_partially_contained_in(range(5, 6), range(4, 6))
    assert is_range_partially_contained_in(range(2, 6), range(4, 8))
    assert determine_num_of_fully_contained_assignments(TEST_INPUT) == 2
    assert determine_num_of_partially_contained_assignments(TEST_INPUT) == 4


test_it()
day_input = open("day4-input.txt", "r").read()
print(f"{determine_num_of_fully_contained_assignments(day_input)=}")
print(f"{determine_num_of_partially_contained_assignments(day_input)=}")
