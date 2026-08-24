arr = list(map(int,input("enter arr:", ).split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1
print(freq)                     
