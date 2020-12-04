import pytest

from fizzbuzz import calculate_fizzbuzz

TEST_FIZZBUZZ_VALUES = [
    (1,1),
    (15,'FizzBuzz'),
    (3,'Fizz'),
    (9,'Fizz'),
    (10,'Buzz'),
    (65,'Buzz'),
    (60,'FizzBuzz'),
    (88,88),
    (90,'FizzBuzz'),
    (75,'FizzBuzz'),
    (6,'Fizz'),
    (17,17),
    (41,41),
    (5,'Buzz'),
    (61,61),
    (42,'Fizz'),
]


@pytest.mark.parametrize("value, expected",
                         TEST_FIZZBUZZ_VALUES)
def test_calculate_fizzbuzz(value, expected):
    print(f'\nTesting calculate_fizzbuzz({expected})')
    assert calculate_fizzbuzz(value) == expected