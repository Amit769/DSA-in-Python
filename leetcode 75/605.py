def PlaceFlower(flowerbed, n):
    
    for i in range(len(flowerbed)):
        left_empty = (i == 0 or flowerbed[i - 1] == 0)
        right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            
        
        if flowerbed[i] == 0 and left_empty and right_empty:
          flowerbed[i] = 1
          n -= 1
         
    
    return n <= 0  

flowerbed = list(map(int, input("enter array: ").split()))
n = int(input("enter n: "))
print(PlaceFlower(flowerbed, n))


        
        
        
      