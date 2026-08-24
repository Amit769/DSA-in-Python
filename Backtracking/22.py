class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def isValid(ans):
            stack = []
            for val in ans:
                if val == '(':
                    stack.append(val)
                else:
                    if stack and stack [-1] == '(' and val == ')':
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
            return True  
                     
        def helperfunction(length, temp):
            if n*2 == length:
                if isValid(temp):
                    result.append(temp)
                return
            if length > n*2:
                return
            
            
            helperfunction(length+1, temp + "(")
            helperfunction(length+1, temp + ")")  
        
        
        helperfunction(0, "")
        
        return result