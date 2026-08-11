class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Find the length of the longest sequential prefix starting at index 0
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
            
        # Step 2: Calculate the sum of the longest sequential prefix
        prefix_sum = sum(nums[:i])
        
        # Step 3: Find the smallest integer >= prefix_sum not in nums
        num_set = set(nums)
        while prefix_sum in num_set:
            prefix_sum += 1
            
        return prefix_sum
        