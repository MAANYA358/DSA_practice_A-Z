class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        nums=[]
        for row in grid:
            for num in row:
                nums.append(num)
        for num in nums:
            if num % x!=nums[0]%x:
                return -1
        nums.sort()
        median=nums[len(nums)//2]
        moves=0
        for num in nums:
            moves+=abs(num-median)//x
        return moves
                