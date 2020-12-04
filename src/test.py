import pytest

from fizzbuzz import calculate_fizzbuzz, calculate_fizzbuzz_range

TEST_FIZZBUZZ_VALUES = [
    (1, 1),
    (15, 'FizzBuzz'),
    (3, 'Fizz'),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (65, 'Buzz'),
    (60, 'FizzBuzz'),
    (88, 88),
    (90, 'FizzBuzz'),
    (75, 'FizzBuzz'),
    (6, 'Fizz'),
    (17, 17),
    (41, 41),
    (5, 'Buzz'),
    (61, 61),
    (42, 'Fizz'),
    pytest.param(3, 3, marks=pytest.mark.xfail),
]

TEST_FIZZBUZZ_VALUES_RANGE = [
    ((1, 6), (1, 2, 'Fizz', 4, 'Buzz', 'Fizz')),
]

#
@pytest.mark.parametrize("value, expected", TEST_FIZZBUZZ_VALUES)
def test_calculate_fizzbuzz(value, expected):
    print(f'\nTesting calculate_fizzbuzz({expected})')
    assert calculate_fizzbuzz(value) == expected


@pytest.mark.parametrize("value, expected",
                         TEST_FIZZBUZZ_VALUES_RANGE)
def test_calculate_fizzbuzz_range(value, expected):
    print(f'\nTesting calculate_fizzbuzz_range{value}')
    assert calculate_fizzbuzz_range(*value) == expected
