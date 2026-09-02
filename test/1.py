# Product of Array Except Self
# O(n) time, O(1) extra space (excluding output array)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        
