from re import sub, findall


def task2(s: str) -> int:
    ru_string = sub(r"[^а-яА-Я]", "", s)
    return len(ru_string)


def task3(s: str) -> bool:
    string = sub(r"[^a-z]", "", s)
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True


def task4(s: str) -> list[str]:
    return findall(r"\d{1,2}\.\d{1,2}\.\d{4}", s)
