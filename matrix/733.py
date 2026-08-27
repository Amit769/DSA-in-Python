from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        
        if original == color:
            return image 
        
        def dfs(r, c ):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            if image[r][c] != original:
                return
            image[r][c] = color
            
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        dfs(sr, sc)

        return image

        