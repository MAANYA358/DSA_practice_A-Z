from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        
        # best_till[i] stores the minimum length of a valid sub-array ending at or before index i
        best_till = [float('inf')] * n
        
        # Tracks the absolute minimum length of a single valid sub-array seen so far
        min_single_len = float('inf')
        
        # Tracks the minimum sum of the lengths of TWO non-overlapping valid sub-arrays
        min_combined_len = float('inf')
        
        left = 0
        window_sum = 0
        
        # Slide the right pointer across the array
        for right in range(n):
            window_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds the target
            # (Safe to do because all array elements are strictly positive)
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
                
            # If the current window exactly matches the target sum
            if window_sum == target:
                current_len = right - left + 1
                
                # If there is a valid, non-overlapping sub-array before our current 'left' bound
                if left > 0 and best_till[left - 1] != float('inf'):
                    # The combined length is our current length + the best historical length
                    min_combined_len = min(min_combined_len, current_len + best_till[left - 1])
                    
                # Update the running minimum length of a single valid sub-array
                min_single_len = min(min_single_len, current_len)
                
            # Record the best single sub-array length found up to this 'right' index
            best_till[right] = min_single_len
            
        # If min_combined_len was never updated, 2 non-overlapping sub-arrays don't exist
        return min_combined_len if min_combined_len != float('inf') else -1
        