def convert_to_list(string):
    list_x = [int(i) for i in string]
    return list_x


def main():
    num_1 = input()
    list_1 = convert_to_list(num_1)

    num_2 = input()
    list_2 = convert_to_list(num_2)

    reversed_num_1 = list(reversed(list_1))
    reversed_num_2 = list(reversed(list_2))

    if len(reversed_num_1) > len(reversed_num_2):
        temp = reversed_num_1
        reversed_num_1 = reversed_num_2
        reversed_num_2 = temp

    for _ in range(len(reversed_num_2) - len(reversed_num_1)):
        reversed_num_1.append(0)

    result = []
    summa = 0
    rest = 0

    for i in range(len(reversed_num_1)):
        summa = reversed_num_1[i] + reversed_num_2[i] + rest
        rest = summa // 2
        summa = summa % 2
        result.append(summa)

    if rest > 0:
        result.append(rest)

    res = list(reversed(result))

    binary_num = ''.join(str(n) for n in res)
    print(binary_num)


if __name__ == "__main__":
    main()
