from typing import Union


def calculate_fizzbuzz(number: int) -> Union[str, int]:
    """
    Determines the output of the FizzBuzz method for a given number
    Parameters
    ----------
    number : int
        The number input for calculating FizzBuzz method.
    Returns
    -------
    result : Union[str, int]
        FizzBuzz output number or string.
    Raises
    ------
    ValueError
        If the input is not a number number.
    """
    if type(number) != int:
        raise ValueError(f'The input value ({number}) should should be a number, but it is a {type(number).__name__}!')
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


def calculate_fizzbuzz_range(start: int, end: int) -> tuple:
    """
        Determines the output of the FizzBuzz method for a given number range (including both ends).
        Parameters
        ----------
        start : int
            The number for starting the sequence.
        end : int
            The number for ending the sequence.

        Returns
        -------
        result : tuple
            Tuple containing all FizzBuzz numbers of the desired sequence.
        Raises
        ------
        ValueError
            If one of the inputs is not a number or if start number is greater than end number.
        """
    if start > end:
        raise ValueError(f'The start number ({start}) should not be greater than the end number ({end})!')
    if type(start) != int or type(start) != int:
        raise ValueError(f'Both inputs should be numbers!')
    return tuple(calculate_fizzbuzz(i) for i in range(start, end + 1))
