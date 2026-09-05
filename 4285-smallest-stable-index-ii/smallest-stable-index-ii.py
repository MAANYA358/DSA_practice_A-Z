from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        # Get the total number of elements in the array
        n = len(nums)
        
        # Initialize an array to store the minimum values from right to left
        suf_min = [0] * n
        
        # The suffix minimum of the very last element is just the element itself
        suf_min[n - 1] = nums[n - 1]
        
        # Iterate backwards from the second-to-last element down to index 0
        # This takes O(N) time and prevents us from repeatedly scanning the array
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])
            
        # Initialize the maximum value seen so far from left to right
        prefix_max = float('-inf')
        
        # Iterate forward through the array to find the smallest stable index
        for i in range(n):
            # Update the maximum value seen from index 0 up to index 'i' in O(1) time
            prefix_max = max(prefix_max, nums[i])
            
            # Calculate instability score using our O(1) lookups
            instability_score = prefix_max - suf_min[i]
            
            # If the condition is met, return 'i' immediately to guarantee the smallest index
            if instability_score <= k:
                return i
                
        # If the loop finishes without finding any stable index, return -1
        return -1