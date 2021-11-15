def main():
    rows_number = int(input())
    colums_number = int(input())
    if rows_number == 0 or colums_number == 0:
        return None
    matrix = [input().split() for _ in range(rows_number)]

    new_matrix = []
    for j in range(colums_number):
        for i in range(rows_number):
            new_matrix.append(matrix[i][j])

    sliced_new_matrix = [new_matrix[i:i+rows_number] for i in range(0, len(new_matrix), rows_number)]
    for slice in sliced_new_matrix:
        result = ' '.join(str(k) for k in slice)
        print(result)

if __name__ == "__main__":
    main()
