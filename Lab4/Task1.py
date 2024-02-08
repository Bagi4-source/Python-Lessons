def main():
    with open("27-170b.txt", mode="r") as file:
        n, k = map(int, file.readline().split(" "))
        numbers = list(map(int, file.readlines()))

    numbers.sort()
    result = sum(numbers[n - k - 1:n])
    print(result)


if __name__ == '__main__':
    main()
