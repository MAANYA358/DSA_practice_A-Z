from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Pair each value with its original index and sort by value
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        n = len(nums)
        ans = [0] * n
        
        # Group elements where adjacent values differ by <= limit
        i = 0
        while i < n:
            group_vals = deque([sorted_pairs[i][0]])
            group_indices = [sorted_pairs[i][1]]
            
            j = i + 1
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                group_vals.append(sorted_pairs[j][0])
                group_indices.append(sorted_pairs[j][1])
                j += 1
                
            # Sort the indices in this group so smaller indices get smaller values
            group_indices.sort()
            
            # Place values into the result array
            for idx in group_indices:
                ans[idx] = group_vals.popleft()
                
            i = j
            
        return ans