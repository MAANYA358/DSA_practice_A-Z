from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Step 1: Record the first and last occurrence index of every character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        intervals = []
        
        # Step 2: Validate and expand intervals
        for i, char in enumerate(s):
            # Only attempt to build an interval starting at the first occurrence of a character
            if i == first[char]:
                new_right = self._get_right_bound(s, i, first, last)
                
                # If the interval is valid, store its start and end indices
                if new_right != -1:
                    intervals.append((i, new_right))
                    
        # Step 3: Greedy selection
        # Sort intervals by their rightmost boundary to maximize non-overlapping picks
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_right = -1
        
        # Iterate through the sorted intervals and select non-overlapping ones
        for left, right in intervals:
            if left > prev_right:
                res.append(s[left : right + 1])
                prev_right = right
                
        return res

    def _get_right_bound(self, s: str, start: int, first: dict, last: dict) -> int:
        """
        Expands the substring boundary to include all occurrences of characters within it.
        Returns the expanded right index, or -1 if the substring becomes invalid.
        """
        right = last[s[start]]
        curr = start
        
        # Scan through the interval
        while curr <= right:
            char = s[curr]
            
            # If a character's first occurrence is before our starting point, 
            # this entire substring is invalid (a better superset exists starting earlier)
            if first[char] < start:
                return -1
                
            # Expand the right boundary if the current character extends beyond it
            right = max(right, last[char])
            curr += 1
            
        return right
        