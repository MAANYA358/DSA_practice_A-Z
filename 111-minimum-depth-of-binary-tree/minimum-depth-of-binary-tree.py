from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Base case: Leaf node
        if not root.left and not root.right:
            return 1
        
        # If left child is missing, must go down right subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If right child is missing, must go down left subtree
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Both children exist: take the minimum of both subtrees
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))