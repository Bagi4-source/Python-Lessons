def sum_of_digits(x: int, f=lambda x: True) -> int:
    s = 0
    while x:
        digit = x % 10
        if f(digit):
            s += digit
        x //= 10
    return s


def is_simple(x: int) -> bool:
    if x < 1:
        return False
    if x < 3:
        return True
    if x % 2 == 0:
        return False
    return len(get_divs(x)) == 2


def get_divs(x: int) -> list:
    result = []
    for i in range(1, x + 1):
        if x % i == 0:
            result.append(i)
    return result
