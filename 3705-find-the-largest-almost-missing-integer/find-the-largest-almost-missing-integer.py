from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        cnt = Counter(nums)
        
        # Case 1: k == 1 -> Find the largest unique element
        if k == 1:
            uniques = [x for x, c in cnt.items() if c == 1]
            return max(uniques) if uniques else -1
        
        # Case 2: k == n -> Only one subarray exists; return the max element
        if k == n:
            return max(nums)
        
        # Case 3: 1 < k < n -> Only endpoints can appear in exactly one subarray
        ans = -1
        if cnt[nums[0]] == 1:
            ans = max(ans, nums[0])
        if cnt[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
        