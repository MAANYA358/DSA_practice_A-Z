from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with -infinity because node values can be negative
        max_sum = float('-inf')
        
        def get_max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            
            # Base case: null node contributes 0 to the sum
            if not node:
                return 0
            
            # Recursively compute the maximum branch gain from left and right children
            # If the gain is negative, clamp it to 0 (do not include that branch)
            left_gain = max(0, get_max_gain(node.left))
            right_gain = max(0, get_max_gain(node.right))
            
            # Price of the new path where the current node is the highest point (turning point)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            max_sum = max(max_sum, current_path_sum)
            
            # Return the maximum single branch sum that can be extended to the parent
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return max_sum
