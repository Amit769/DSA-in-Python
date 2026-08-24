matrix = []
rows = int(input("enter row"))
col = int(input("enter col"))

for i in range(rows):
    rows = list(map(int, input("enter row").split()))
    matrix.append(rows)
    
for j in range(col):
    col = list(map(int, input("enter col").split()))
    matrix.append(col)
    
print(matrxi)            

    