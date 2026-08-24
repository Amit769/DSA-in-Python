class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1

nums = list(map(int, input("enter array: ").split()))
print(Solution().pivotIndex(nums))   