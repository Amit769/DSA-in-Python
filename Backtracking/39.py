class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start, path, total):

            # Base case: target reached
            if total == target:
                result.append(path[:])
                return

            # Stop if total becomes greater than target
            if total > target:
                return

            for i in range(start, len(candidates)):

                path.append(candidates[i])       # Choose

                backtrack(
                    i,                           # Same number can be reused
                    path,
                    total + candidates[i]
                )

                path.pop()                       # Undo

        backtrack(0, [], 0)

        return result