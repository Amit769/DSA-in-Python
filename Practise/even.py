class Solution:
    def isEven (self, n):
        # code here 
        
        for i in range(1, n):
            if n % 2 == 0:
                return True
            else:
                return False
        
        