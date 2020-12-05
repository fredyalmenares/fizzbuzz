import pytest as pt

from fizzbuzz import calculate_fizzbuzz, calculate_fizzbuzz_range

TEST_FIZZBUZZ_VALUES = (
    (1, 1),
    (15, 'FizzBuzz'),
    (3, 'Fizz'),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (65, 'Buzz'),
    (60, 'FizzBuzz'),
    (88, 88),
    (90, 'FizzBuzz'),
    pt.param(61, 'FizzBuzz', marks=pt.mark.xfail),
    (75, 'FizzBuzz'),
    (6, 'Fizz'),
    (17, 17),
    (41, 41),
    (5, 'Buzz'),
    (61, 61),
    (42, 'Fizz'),
    pt.param('Not a number', pt.raises(ValueError), marks=pt.mark.xfail),
    pt.param('90', pt.raises(ValueError), marks=pt.mark.xfail),
    pt.param(-1, -1, marks=pt.mark.xfail),
    pt.param(3, 3, marks=pt.mark.xfail),
    pt.param(5, 5, marks=pt.mark.xfail),
    pt.param(90, 'Buzz', marks=pt.mark.xfail),
    pt.param(3, 'Buzz', marks=pt.mark.xfail),
)

TEST_FIZZBUZZ_VALUES_RANGE = (
    ((1, 6), (1, 2, 'Fizz', 4, 'Buzz', 'Fizz')),
    ((12, 16), ('Fizz', 13, 14, 'FizzBuzz', 16)),
    ((78, 84), ('Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz')),
    pt.param((33, 36), (33, 34, 35, 36), marks=pt.mark.xfail),
    pt.param((49, 81), (1, 2, 8, 29), marks=pt.mark.xfail),
    pt.param((45, 12), pt.raises(ValueError), marks=pt.mark.xfail),
    pt.param((63, 62), pt.raises(ValueError), marks=pt.mark.xfail),
    pt.param((55, 'string'), pt.raises(ValueError), marks=pt.mark.xfail),
)


#
@pt.mark.parametrize("value, expected", TEST_FIZZBUZZ_VALUES)
def test_calculate_fizzbuzz(value, expected):
    print(f'\nTesting calculate_fizzbuzz({expected})')
    assert calculate_fizzbuzz(value) == expected


@pt.mark.parametrize("value, expected",
                     TEST_FIZZBUZZ_VALUES_RANGE)
def test_calculate_fizzbuzz_range(value, expected):
    print(f'\nTesting calculate_fizzbuzz_range{value}')
    assert calculate_fizzbuzz_range(*value) == expected
