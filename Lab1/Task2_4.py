from re import sub, findall


def sum_of_ru_symbols(s: str) -> int:
    ru_string = sub(r"[^а-яА-Я]", "", s)
    return len(ru_string)


def is_latin_palindrome(s: str) -> bool:
    string = sub(r"[^a-z]", "", s)
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True


def find_date(s: str) -> list[str]:
    return findall(r"\d{1,2}\.\d{1,2}\.\d{4}", s)
