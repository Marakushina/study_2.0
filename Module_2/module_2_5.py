def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix.append(columns := [])
        for j in range (m):
            if value > 1:
                columns.append(value)
            else: break


    return matrix


result1 = get_matrix(4, 0, 2)
print(result1)