matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
largest = matrix[0][0]
 
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            
print(largest)                   
        