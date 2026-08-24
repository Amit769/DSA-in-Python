class Solution:
    def sortArray(self, nums):
        nums.sort()
        return nums

nums = list(map(int, input("enter the array").split()))    
sorted_nums = Solution().sortArray(nums)
print(sorted_nums)
        

