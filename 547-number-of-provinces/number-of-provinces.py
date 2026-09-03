from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Get the total number of cities to define the range of our search
        n = len(isConnected)
        
        # Initialize a set to keep track of which cities have already been explored
        # A set provides O(1) lookup time to prevent revisiting cities and infinite loops
        visited = set()
        
        # Initialize a counter to track the number of independent, disconnected provinces found
        provinces = 0
        
        # Helper DFS function to traverse and mark all cities connected to a starting city 'i'
        def dfs(i: int):
            # Iterate through every possible destination city 'j' from city 'i'
            for j in range(n):
                # Check two conditions: 
                # 1. Is there a direct connection between 'i' and 'j' (value is 1)?
                # 2. Has city 'j' NOT been visited yet?
                if isConnected[i][j] == 1 and j not in visited:
                    # Mark city 'j' as visited so it isn't processed again from another path
                    visited.add(j)
                    
                    # Recursively call DFS on 'j' to find all cities connected to 'j'
                    # This explores the graph deeply until the entire component is found
                    dfs(j) 
                    
        # Iterate through every city from 0 to n-1 to ensure no disconnected component is missed
        for i in range(n):
            # If city 'i' is not in the visited set, it belongs to a brand new, unexplored province
            if i not in visited:
                # Increment the province counter since we found a new disconnected group
                provinces += 1
                
                # Mark this starting city as visited
                visited.add(i)
                
                # Launch the DFS traversal to find and mark all other cities in this new province
                dfs(i)
                
        # Return the final count of independent provinces
        return provinces
        