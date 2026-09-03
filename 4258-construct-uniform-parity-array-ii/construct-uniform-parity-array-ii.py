from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_val = min(nums1)
        
        # If the minimum value is even, we cannot have any odd numbers in the array.
        if min_val % 2 == 0:
            for num in nums1:
                if num % 2 != 0:
                        return False
            return True
            
        # If the minimum value is odd, it is always possible.
        return True
            
        # If the minimum value is odd, it is always possible.
        return True