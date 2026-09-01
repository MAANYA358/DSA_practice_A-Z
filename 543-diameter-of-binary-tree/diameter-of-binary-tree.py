from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global variable to track the maximum diameter found across all subtrees
        max_diameter = 0
        
        # Helper DFS function that returns the height of the current subtree
        def get_height(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            
            # Base case: an empty subtree has a height of 0
            if not node:
                return 0
            
            # Recursively find the height of the left subtree
            left_height = get_height(node.left)
            
            # Recursively find the height of the right subtree
            right_height = get_height(node.right)
            
            # The longest path through the current node is the sum of left and right heights
            # Update the global maximum diameter if this path is larger
            max_diameter = max(max_diameter, left_height + right_height)
            
            # Return the height of this node to its parent (1 + max branch height)
            return 1 + max(left_height, right_height)
        
        # Start the traversal from the root
        get_height(root)
        
        # Return the overall maximum diameter recorded
        return max_diameter
        