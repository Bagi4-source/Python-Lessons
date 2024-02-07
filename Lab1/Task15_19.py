from shared.util import get_divs, is_simple


def task15(arr: list[int]) -> int:
    max_item = arr[0]
    count = 0
    for item in arr:
        count += 1
        if item >= max_item:
            max_item = item
            count = 0

    return count


def task16(arr: list[int]) -> list[int]:
    min_item = arr[0]
    min_index = 0
    result = []
    for index, item in enumerate(arr):
        if item < min_item:
            min_item = item
            min_index = index

    result.extend(arr[min_index:])
    result.extend(arr[:min_index])
    return result


def task17(arr: list[int], interval: tuple) -> int:
    a, b = interval
    return max(arr[a: b])


def task18(arr: list[int]):
    n = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print(i + 1)
            n += 1
    print(f"Count: {n}")


def task19(arr: list[int]):
    result = set()

    for item in arr:
        for i in get_divs(item):
            if is_simple(i):
                result.add(i)
    return result
