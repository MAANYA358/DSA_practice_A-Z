from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the number of rows in the grid
        rows = len(grid)
        # Get the number of columns in the grid
        cols = len(grid[0])
        
        # Initialize a queue to facilitate multi-source BFS
        queue = deque()
        # Initialize a counter to track the number of fresh oranges
        fresh_count = 0
        
        # Iterate through every cell in the grid to initialize the queue and fresh count
        for r in range(rows):
            for c in range(cols):
                # If the cell contains a rotten orange (2)
                if grid[r][c] == 2:
                    # Add its coordinates to the initial BFS queue
                    queue.append((r, c))
                # If the cell contains a fresh orange (1)
                elif grid[r][c] == 1:
                    # Increment the fresh orange counter
                    fresh_count += 1
                    
        # Initialize minutes elapsed to 0
        minutes = 0
        # Define the 4 adjacent directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Continue BFS as long as there are rotting oranges to process AND fresh oranges left
        while queue and fresh_count > 0:
            # Increment the minute tracker for the current BFS level
            minutes += 1
            
            # Process all oranges that became rotten in the previous minute strictly
            for _ in range(len(queue)):
                # Pop the coordinates of a rotten orange from the front of the queue
                r, c = queue.popleft()
                
                # Explore all 4 adjacent cells
                for dr, dc in directions:
                    # Calculate the row index of the adjacent cell
                    nr = r + dr
                    # Calculate the column index of the adjacent cell
                    nc = c + dc
                    
                    # Check if the adjacent cell is within grid bounds AND contains a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # Mutate the fresh orange into a rotten one in the grid
                        grid[nr][nc] = 2
                        # Decrement the fresh orange counter
                        fresh_count -= 1
                        # Add the newly rotten orange's coordinates to the queue for the next minute
                        queue.append((nr, nc))
                        
        # If no fresh oranges remain, return the elapsed minutes; otherwise, return -1
        return minutes if fresh_count == 0 else -1
        