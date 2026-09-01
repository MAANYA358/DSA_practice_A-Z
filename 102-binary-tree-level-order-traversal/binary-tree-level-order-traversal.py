from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list immediately
        if not root:
            return []
        
        # Initialize the final list to store values level by level
        result = []
        
        # Initialize a double-ended queue with the root node to begin BFS
        queue = deque([root])
        
        # Continue the traversal as long as there are nodes to process in the queue
        while queue:
            # Count the number of nodes present at the current level
            level_size = len(queue)
            
            # Temporary list to store values of all nodes in the current level
            current_level = []
            
            # Process strictly all nodes that belong to the current level
            for _ in range(level_size):
                # Remove and retrieve the frontmost node from the queue (FIFO)
                front = queue.popleft()
                
                # Add the current node's value to the current level's list
                current_level.append(front.val)
                
                # If a left child exists, push it to the back of the queue for the next level
                if front.left:
                    queue.append(front.left)
                    
                # If a right child exists, push it to the back of the queue for the next level
                if front.right:
                    queue.append(front.right)
                    
            # Append the completed level values to the final result list
            result.append(current_level)
            
        # Return the final level-ordered 2D array
        return result

    