class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []  # Monotonic decreasing stack storing candidates for nums[j]
        third = float('-inf')  # Candidate for nums[k]
        
        # Traverse backwards from right to left
        for num in reversed(nums):
            # If we find a number smaller than 'third', we found nums[i] < nums[k] < nums[j]
            if num < third:
                return True
            
            # Maintain monotonic stack: when num > stack top, num can be nums[j]
            while stack and stack[-1] < num:
                third = stack.pop()
                
            stack.append(num)
            
        return False