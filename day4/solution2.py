input_text = open("input.txt", "r").readlines()
reports = [line.split() for line in input_text]
matrix = [list(row[0]) for row in reports]

word = "MAS"
diag_list = []
diag2_list = []

rows, columns = len(matrix), len(matrix[0])

for row in range(rows):
    for column in range(columns):
        if column + 2 < columns and row + 2 < rows:
            diag = "".join(matrix[row + i][column + i] for i in range(3))
            if diag == word or diag[::-1] == word:
                diag_list.append((row + 1, column + 1))

        if column - 2 >= 0 and row + 2 < rows:
            diag2 = "".join(matrix[row + i][column - i] for i in range(3))
            if diag2 == word or diag2[::-1] == word:
                diag2_list.append((row + 1, column - 1))

print(len(set(diag_list) & set(diag2_list)))
