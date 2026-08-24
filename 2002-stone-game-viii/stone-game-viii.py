from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        pref = list(accumulate(stones))
        n = len(stones)
        
        # Base case: taking all stones gives score pref[n - 1] and ends the game
        dp = pref[-1]
        
        # Work backwards from index n - 2 down to index 1 (since x >= 2, i.e., index >= 1)
        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp