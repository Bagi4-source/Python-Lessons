from shared.util import get_divs, sum_of_digits, is_simple

def f1(*args):
    result = 0
    for x in get_divs(*args):
        if is_simple(x):
            result += x
    return result


def f2(*args):
    return sum_of_digits(*args, f=lambda x: x % 2 and x > 3)


def f3(*args):
    result = 1
    sum_of_digits_x = sum_of_digits(*args)
    for x in get_divs(*args):
        if sum_of_digits_x > sum_of_digits(x):
            result *= x
    return result
