class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
    
candies = list(map(int, input("enter candies: ").split()))
extraCandies = int(input("enter extra candies: "))   
solution = Solution()
result = solution.kidsWithCandies(candies, extraCandies)
print("output: ", result) 