import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Append original indices to keep track of them after sorting
        arr = [(*interval, i) for i, interval in enumerate(intervals)]
        
        # Sort intervals by start time to process from left to right in our suffix DP
        arr.sort(key=lambda x: x[0])
        starts = [x[0] for x in arr]
        
        # dp[i][k] stores a tuple: (maximum_weight, lexicographically_smallest_indices_list)
        # i represents the suffix starting at index i
        # k represents the maximum number of intervals we can still pick (up to 4)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        # Traverse backwards to build the DP table
        for i in range(n - 1, -1, -1):
            start, end, weight, orig_idx = arr[i]
            
            # Find the next valid interval that does not overlap
            # The problem defines overlapping as sharing any points, so we strictly need next_start > end
            j = bisect.bisect_right(starts, end)
            
            for k in range(1, 5):
                # Option 1: Do not pick the current interval
                skip_weight, skip_indices = dp[i + 1][k]
                
                # Option 2: Pick the current interval
                take_weight, take_indices = dp[j][k - 1]
                take_weight += weight
                
                # The final chosen indices must be sorted to be compared lexicographically
                new_indices = sorted([orig_idx] + take_indices)
                
                # Compare both options to maximize weight
                if take_weight > skip_weight:
                    dp[i][k] = (take_weight, new_indices)
                elif take_weight < skip_weight:
                    dp[i][k] = (skip_weight, skip_indices)
                else:
                    # If weights tie, strictly pick the lexicographically smaller array of indices
                    if new_indices < skip_indices:
                        dp[i][k] = (take_weight, new_indices)
                    else:
                        dp[i][k] = (skip_weight, skip_indices)
                        
        # Return the strictly optimal indices array for exactly 4 available picks from index 0
        return dp[0][4][1]
        