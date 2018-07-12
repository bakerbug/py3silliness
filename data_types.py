def int_square(x: int) -> int:
    return x**2


def str_square(x: int) -> str:
    # format converts the int into a str.
    return 'The square of {} is {}.'.format(x, int_square(x))


def print_square(x: int) -> None:
    print(str_square(x))


if __name__ == '__main__':
    print_square(9)
