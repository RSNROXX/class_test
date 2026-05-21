"""
This module contains basic mathematical operations.
Functions for multiplying and adding two numbers.
"""

import print_out       # first way to import

# from print_out import double_it    # second way to import

X_INIT: int = 1


def prod_number(num1: int,
                num2: int) -> int:   # type hints
    """Return the product of 2 numbers"""
    return num1 * num2


def add_number(num1: int,
               num2: int) -> int:    # type hints
    """Return the addition of 2 numbers"""
    return num1 + num2


def divide_number(num1: int,
                  num2: int) -> float:    # type hints
    """Return the division of 2 numbers"""
    return num1 / num2


def addition_example(old_inventory: int, new_inventory: int) -> int:
    """_summary_

    Args:
        old_inventory (int): _description_
        new_inventory (int): _description_

    Returns:
        int: _description_
    """
    y = old_inventory + new_inventory + X_INIT

    result = print_out.double_it(y)

    return result


# print(prod_number(3, 4))
# print(add_number(1, 2))
# print(divide_number(1, 2))
# print(addition_example(1.5, 2.8))


if __name__ == "__main__":  # dunder method
    print(addition_example(1, 2))
