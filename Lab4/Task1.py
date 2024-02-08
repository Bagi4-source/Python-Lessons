def main():
    with open("27-170b.txt", mode="r") as file:
        lines = file.readlines()
        numbers = list(map(int, lines[1:]))

    n, k = map(int, lines[0].split(" "))
    numbers.sort()
    result = sum(numbers[n - k - 1:n])
    print(result)


if __name__ == '__main__':
    main()
