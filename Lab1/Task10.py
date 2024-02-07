def task10(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda s: len(s.split(" ")))
