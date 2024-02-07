def task9():
    string = input("Enter string: ")
    result = list()
    while string:
        result.append(string)
        string = input("Enter string: ")

    return sorted(result)
