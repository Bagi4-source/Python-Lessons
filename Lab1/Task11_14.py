from re import sub

VOWELS = {'а', 'о', 'у', 'ы', 'э', 'я', 'е', 'ю', 'и', 'ё'}


def task11(strings: list[str]) -> list[str]:
    def f(s: str) -> int:
        s = sub(r"[^a-я]", "", s.lower())
        n = 0
        for char in s:
            if char in VOWELS:
                n += 1
        return abs(len(s) - n - n)

    return sorted(strings, key=f)


def task12(strings: list[str]) -> list[str]:
    if not strings:
        return []

    def avg_weight(s: str) -> float:
        if not s:
            return 0

        n = 0
        for char in s:
            n += ord(char)
        return n / len(s)

    first_avg = avg_weight(strings[0])

    def f(s: str) -> float:
        return (avg_weight(s) - first_avg) ** 2

    return sorted(strings, key=f)


def task13(strings: list[str]) -> list[str]:
    def f(s: str) -> float:
        s = sub(r"[^a-я]", "", s.lower())
        a = 0
        b = 0
        for i in range(len(s) - 1):
            if s[i] in VOWELS and s[i + 1] not in VOWELS:
                a += 1
            if s[i] not in VOWELS and s[i + 1] in VOWELS:
                b += 1

        return abs(a - b)

    return sorted(strings, key=f)


def task14(strings: list[str]) -> list[str]:
    def f(s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                count += 1
        return count

    return sorted(strings, key=f)
