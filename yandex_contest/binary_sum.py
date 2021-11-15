def convert_to_list(string):
    return [int(i) for i in string]


def main():
    num_1 = input()
    list_1 = convert_to_list(num_1)

    num_2 = input()
    list_2 = convert_to_list(num_2)

    list_1 = list(reversed(list_1))
    list_2 = list(reversed(list_2))

    if len(list_1) > len(list_2):
        list_1, list_2 = list_2, list_1

    for _ in range(len(list_2) - len(list_1)):
        list_1.append(0)

    result = []
    summa = 0
    rest = 0

    for i in range(len(list_1)):
        summa = list_1[i] + list_2[i] + rest
        rest = summa // 2
        summa %= 2
        result.append(summa)

    if rest > 0:
        result.append(rest)

    res = list(reversed(result))

    binary_num = ''.join(str(n) for n in res)
    print(binary_num)


if __name__ == "__main__":
    main()
