# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: 'Optional[TreeNode]') -> int:
        # Initialize a counter to track how many nodes meet the average condition
        matching_nodes = 0
        
        # Helper function for bottom-up Post-Order traversal
        def post_order(node: 'Optional[TreeNode]') -> tuple[int, int]:
            # Allow modification of the outer scope's counter variable
            nonlocal matching_nodes
            
            # Base case: If the node is null, it contributes 0 to the sum and 0 to the count
            if not node:
                return 0, 0
                
            # Step 1: Recursively get the sum and count from the left subtree
            left_sum, left_count = post_order(node.left)
            
            # Step 2: Recursively get the sum and count from the right subtree
            right_sum, right_count = post_order(node.right)
            
            # Step 3: Calculate the total sum for the current node's entire subtree
            current_sum = left_sum + right_sum + node.val
            
            # Step 4: Calculate the total node count for the current node's entire subtree
            current_count = left_count + right_count + 1
            
            # Step 5: Check if the current node's value equals the integer average of its subtree
            if node.val == current_sum // current_count:
                # Increment the result counter if the condition is met
                matching_nodes += 1
                
            # Return the aggregated sum and count upward to the parent node
            return current_sum, current_count
            
        # Trigger the DFS traversal starting from the root
        post_order(root)
        
        # Return the final count of matching nodes
        return matching_nodes