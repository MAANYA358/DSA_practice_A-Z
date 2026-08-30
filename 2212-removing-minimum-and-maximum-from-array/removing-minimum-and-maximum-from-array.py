class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n= len(nums)
        if n<= 2:
            return n
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        
        # 1. Delete both from the front: elements 0 through j
        cost_front = j + 1
        
        # 2. Delete both from the back: elements i through n - 1
        cost_back = n - i
        
        # 3. Delete from both ends: (0 through i) + (j through n - 1)
        cost_both = (i + 1) + (n - j)
        
        return min(cost_front, cost_back, cost_both)

        