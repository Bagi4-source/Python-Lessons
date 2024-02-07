from re import finditer, sub


def task6(s: str):
    numbers = [float(x.group()) for x in finditer(r"\d+(\.\d+)?", s)]
    if not numbers:
        return None

    result = numbers[0]
    for i in numbers:
        result = max(result, i)
    return result


def task7(s: str):
    def f(x):
        a, b = map(int, x.split("/"))
        return a / b

    numbers = [f(x.group()) for x in finditer(r"\d+/\d+", s)]
    if not numbers:
        return None
    result = numbers[0]
    for i in numbers:
        result = min(result, i)
    return result


def task8(s: str):
    lengths = [len(x.group()) for x in finditer(r"\d+", s)]
    return max(lengths)
