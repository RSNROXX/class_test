"""
A module for printing out stuff
"""


def print_inputs_out(x: int | float | str | list) -> int | float | str | list:
    """Print and return the input.

    Args:
        x: An integer, float, string, or list

    Returns:
        The input value
    """
    return x


def double_it(x: int | float | str | list) -> int | float | str | list:
    """Double a numeric value.

    Args:
        x: An integer or float to double

    Returns:
        The value doubled
    """
    return x * 2


if __name__ == "__main__":
    print(double_it(2))
    print(print_inputs_out(2))
