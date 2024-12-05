input_text = open("input.txt", "r").readlines()
reports = [line.split() for line in input_text]
matrix = [list(row[0]) for row in reports]

word = "XMAS"
counter = 0

rows, columns = len(matrix), len(matrix[0])

for row in range(rows):
    for column in range(columns):
        if column + 3 < columns:
            hor = "".join(matrix[row][column : column + len(word)])
            if hor == word or hor[::-1] == word:
                counter += 1

        if row + 3 < rows:
            vert = "".join(matrix[row + i][column] for i in range(len(word)))
            if vert == word or vert[::-1] == word:
                counter += 1

        if column - 3 >= 0 and row + 3 < rows:
            diag2 = "".join(matrix[row + i][column - i] for i in range(len(word)))
            if diag2 == word or diag2[::-1] == word:
                counter += 1

        if column + 3 < columns and row + 3 < rows:
            diag = "".join(matrix[row + i][column + i] for i in range(len(word)))
            if diag == word or diag[::-1] == word:
                counter += 1

print(counter)
