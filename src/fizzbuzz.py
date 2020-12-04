from typing import Union


def calculate_fizzbuzz(number: int) -> Union[str, int]:
    """ Determines the output of the FizzBuzz method for a given number """
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


def calculate_fizzbuzz_range(start: int, end: int) -> list:
    return []
