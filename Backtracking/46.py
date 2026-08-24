class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):

            # Base case
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:

                # Skip already used numbers
                if num in path:
                    continue

                # Choose
                path.append(num)

                # Explore
                backtrack(path)

                # Undo
                path.pop()

        backtrack([])
        return res