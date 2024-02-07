from re import finditer, sub


def task6(s: str) -> int | None:
    numbers = [float(x.group()) for x in finditer(r"\d+(\.\d+)?", s)]
    if not numbers:
        return None

    result = numbers[0]
    for i in numbers:
        result = max(result, i)
    return result


def task7(s: str) -> float | None:
    def f(x) -> float:
        a, b = map(int, x.split("/"))
        return a / b

    numbers = [f(x.group()) for x in finditer(r"\d+/\d+", s)]
    if not numbers:
        return None
    result = numbers[0]
    for i in numbers:
        result = min(result, i)
    return result


def task8(s: str) -> int:
    lengths = [len(x.group()) for x in finditer(r"\d+", s)]
    return max(lengths)
