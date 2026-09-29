class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)

        target = total - x

        # Impossible case
        if target < 0:
            return -1

        left = 0
        current_sum = 0
        max_len = -1

        for right in range(len(nums)):

            current_sum += nums[right]

            # Shrink window if sum becomes greater than target
            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1

            # Found a subarray with required sum
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        # No valid subarray found
        if max_len == -1:
            return -1

        return len(nums) - max_len