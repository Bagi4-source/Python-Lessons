from re import finditer


def find_date(s: str):
    result = finditer(r"\d{1,2} (декабря|января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября) \d{4}", s)
    return [x.group() for x in result]
