def convert(string):
    list_1 = []
    list_1[:0] = string
    list_x = [int(i) for i in list_1]
    return list_x

def main():
    num_1 = input()
    list_1 = convert(num_1)

    num_2 = input()
    list_2 = convert(num_2)

    result = []
    summa = 0
    rest = 0

    number1 = list(reversed(list_1))
    number2 = list(reversed(list_2))

    diff = len(list_1) - len(list_2)
    if diff < 0:
        for _ in range(abs(diff)):
            number1.append(0)
    elif diff > 0:
        for _ in range(abs(diff)):
            number2.append(0)

    for i in range(len(number1)):
        summa = number1[i] + number2[i] + rest
        if summa == 2:
            summa = 0
            rest = 1
            result.append(summa)
        elif summa == 3:
            summa = 1
            rest = 1
            result.append(summa)
        else:
            result.append(summa)
            rest = 0

    if rest > 0:
        result.append(rest)

    res = list(reversed(result))

    binary_num = ''.join(str(n) for n in res)
    print(binary_num)


if __name__ == "__main__":
    main()
