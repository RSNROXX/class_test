"""
This module contains basic mathematical operations.
Functions for multiplying and adding two numbers.
"""


def prod_number(num1: int, num2: int) -> int:   # type hints
    """Return the product of 2 numbers"""
    return num1 * num2


def add_number(num1: int, num2: int) -> int:    # type hints
    """Return the addition of 2 numbers"""
    return num1 + num2


def divide_number(num1: int, num2: int) -> float:    # type hints
    """Return the division of 2 numbers"""
    return num1 / num2


def addition_example(num1: float, num2: float) -> float:
    """Return the addition of 2 numbers with an additional constant value.

    Args:
        num1 (float): get the first number from the user
        num2 (float): get the secont number from the user

    Returns:
        float: result in float type with a constant added to the user
            defined numbers.
    """
    x: float = 1.1
    return num1 + num2 + x


print(prod_number(3, 4))
print(add_number(1, 2))
print(divide_number(1, 2))
print(addition_example(1.5, 2.8))
