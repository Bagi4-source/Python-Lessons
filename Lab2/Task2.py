from re import split


def task2(string: str) -> list[int]:
    counts = dict()
    result = []
    for word in split(r"\s+", string):
        count = counts.get(word, 0)
        result.append(count)
        counts[word] = count + 1

    return result
