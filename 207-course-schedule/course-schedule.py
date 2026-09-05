from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list where adj[i] contains all courses that require course 'i'
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            
        # State tracking array for each course: 
        # 0 = Unvisited, 1 = Currently Visiting (in the current path), 2 = Fully Visited (safe)
        state = [0] * numCourses
        
        # DFS helper function to detect cycles
        def has_cycle(node: int) -> bool:
            # If we see a node that is currently in our active path, we found a cycle!
            if state[node] == 1:
                return True
                
            # If we see a node we've already completely cleared, no need to check it again
            if state[node] == 2:
                return False
                
            # Mark the current node as "Currently Visiting"
            state[node] = 1
            
            # Recursively check all courses that depend on this node
            for neighbor in adj[node]:
                # If any of the downstream paths have a cycle, bubble up the True result
                if has_cycle(neighbor):
                    return True
                    
            # Once all dependencies are cleared, mark this node as "Fully Visited" (safe)
            state[node] = 2
            
            # Return False because no cycle was found from this node
            return False

        # Check every course in the graph (handles disconnected graph components)
        for i in range(numCourses):
            # If the course is unvisited, launch a DFS from it
            if state[i] == 0:
                # If a cycle is detected anywhere, we cannot finish the courses
                if has_cycle(i):
                    return False
                    
        # If we checked all nodes and found no cycles, it is possible to finish
        return True
        