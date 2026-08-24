
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len(nums)

        left = -1
        right = -1

        max_seen = nums[0]
        min_seen = nums[-1]

        for i in range(n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]

        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]

        if left == -1:
            return 0

        return right - left + 1
