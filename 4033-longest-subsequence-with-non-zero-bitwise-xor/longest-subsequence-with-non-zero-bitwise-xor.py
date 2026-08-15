class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        # If all elements are 0, no non-zero XOR subsequence can be formed
        if not any(nums):
            return 0

        total_xor = 0
        for x in nums:
            total_xor ^= x

        # If the whole array has non-zero XOR, return len(nums)
        # Otherwise, remove any non-zero element to get a valid subsequence of length len(nums) - 1
        return len(nums) if total_xor != 0 else len(nums) - 1
        