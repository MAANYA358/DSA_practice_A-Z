from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Every land cell adds 4 to the perimeter
                    perimeter += 4
                    
                    # If there is land directly above, subtract 2 for the shared horizontal edge
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                        
                    # If there is land directly to the left, subtract 2 for the shared vertical edge
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
                        
        return perimeter