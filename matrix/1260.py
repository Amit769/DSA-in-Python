class Solution:
    def shiftGrid(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])

        for _ in range(k):
            last = grid[-1][-1]

            for i in range(rows):
                for j in range(cols - 1, 0, -1):
                    grid[i][j] = grid[i][j - 1]

            for i in range(rows - 1, 0, -1):
                grid[i][0] = grid[i - 1][-1]

            grid[0][0] = last

        return grid