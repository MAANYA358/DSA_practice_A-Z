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
        for i in range(n - 2, -1, -1):
            # The minimum from index 'i' to the end is the smaller of the current element 
            # and the previously calculated minimum to its right
            suf_min[i] = min(nums[i], suf_min[i + 1])
            
        # Initialize the maximum value seen so far from left to right
        prefix_max = float('-inf')
        
        # Iterate forward through the array to find the smallest stable index
        for i in range(n):
            # Update the maximum value seen from index 0 up to index 'i'
            prefix_max = max(prefix_max, nums[i])
            
            # Calculate instability score: max(nums[0..i]) - min(nums[i..n-1])
            instability_score = prefix_max - suf_min[i]
            
            # If the condition is met, we return 'i' immediately because we want the smallest index
            if instability_score <= k:
                return i
                
        # If the loop finishes without finding any stable index, return -1 as specified
        return -1