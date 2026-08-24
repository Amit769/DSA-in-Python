rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

print("Diagonal elements:")

for i in range(min(rows, cols)):
    print(matrix[i][i])