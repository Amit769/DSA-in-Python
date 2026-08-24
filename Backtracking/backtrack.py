def find_subset(s):
    result = []
    
    def backtrack(start, path):
        result.append(path)
        
        for i in range(start, len(s)):
            backtrack(i+1, path+ s[i])
            
            
    backtrack(0, "")
    
    return result
s = input("enter a string: ")

subsets = find_subset(s)

print("subsets: ")
for subset in subsets:
    print(subset)
               
        