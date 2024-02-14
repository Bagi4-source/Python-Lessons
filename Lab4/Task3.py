def ip_to_int(ip_address):
    parts = ip_address.split('.')
    ip_int = 0
    for part in parts:
        ip_int = (ip_int << 8) + int(part)
    return ip_int


def int_to_ip(ip_int):
    parts = []
    for _ in range(4):
        parts.insert(0, str(ip_int & 255))
        ip_int >>= 8
    return '.'.join(parts)


def print_ip(begin, end):
    # print(f"{begin:b}")
    # print(f"{end:b}")
    mask = end ^ begin
    n = 0
    while mask:
        n += 1
        mask >>= 1
    return f"{int_to_ip(begin)}/{32 - n}"


def task3():
    blacklist = set()
    whitelist = set()
    with open("task3_1.txt", mode="r") as file:
        n = int(file.readline())

        for line in file.readlines():
            line = line.strip()
            command = line[0]
            line = line[1:]
            if "/" not in line:
                line += "/32"
            ip, mask = line.split("/")
            begin = ip_to_int(ip) & (2 ** 32 - 2 ** (32 - int(mask)))
            end = begin + 2 ** (32 - int(mask)) - 1
            for i in range(begin, end + 1):
                if command == '-':
                    if i in whitelist:
                        print(-1)
                        return
                    blacklist.add(i)
                else:
                    if i in blacklist:
                        print(-1)
                        return
                    whitelist.add(i)
    print(blacklist)
    print(whitelist)
    begin = blacklist.pop()
    oldItem = begin
    result = []
    while blacklist:
        item = blacklist.pop()
        if item != oldItem + 1:
            result.append((begin, oldItem))
            begin = item
        oldItem = item
    result.append((begin, 2 ** 32 - 1))

    for (begin, end) in result:
        print(print_ip(begin, end))


def main():
    task3()


if __name__ == '__main__':
    main()
