def main():
    rows_count = int(input())
    colums_count = int(input())
    if rows_count == 0 or colums_count == 0:
        return
    matrix = [input().split() for _ in range(rows_count)]

    new_matrix = []
    for j in range(colums_count):
        for i in range(rows_count):
            new_matrix.append(matrix[i][j])

    sliced_new_matrix = [new_matrix[i:i+rows_count] for i in range(0, len(new_matrix), rows_count)]
    for slice in sliced_new_matrix:
        result = ' '.join(str(k) for k in slice)
        print(result)

if __name__ == "__main__":
    main()
