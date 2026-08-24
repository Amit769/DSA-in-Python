class Solution:
    def merge(self, intervals):

        intervals.sort()

        result = []

        for interval in intervals:

            if not result or interval[0] > result[-1][1]:
                result.append(interval)

            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result  
 intervals = list(map(int, input("enter the subarray").arr()))
 merge= Solution().intervals(nums) # pyright: ignore[reportUndefinedVariable]
 return result    