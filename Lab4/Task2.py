import random


def main():
    numbers = [random.randint(0, 50) for _ in range(100)]
    with open("f.txt", mode="w") as file:
        file.writelines(map(lambda x: f"{x}\n", numbers))

    with open("g.txt", mode="w") as file:
        file.writelines(map(lambda x: f"{x}\n", set(numbers)))


if __name__ == '__main__':
    main()
