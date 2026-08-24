
    
rows = int(input("enter rows: "))
cols = int(input("enter col: "))   
     
matrix = []
        

for i in range(rows):
         row = list(map(int, input().split()))
         matrix.append(row)
     
total = 0    
    
for i in range(rows):
        for j in range(cols):
            total = total + matrix[i][j]
        
            
        
print("sum: ", total)    
        
          
        
