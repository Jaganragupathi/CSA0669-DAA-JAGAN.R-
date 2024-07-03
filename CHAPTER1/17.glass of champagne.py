def t(poured, query_row, query_glass):
    tower = [[0] * k for k in range(1, 102)]
    tower[0][0] = poured
    for row in range(query_row + 1):
        for col in range(row + 1):
            if tower[row][col] > 1:
                overflow = (tower[row][col] - 1) / 2
                tower[row][col] = 1
                tower[row + 1][col] += overflow
                tower[row + 1][col + 1] += overflow
    return min(1, tower[query_row][query_glass])
print(t(1, 1, 1))
print(t(2, 1, 1))
