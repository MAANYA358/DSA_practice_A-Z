class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set=set(nums)
        curr=k
        while curr in num_set:
            curr+=k
        return curr