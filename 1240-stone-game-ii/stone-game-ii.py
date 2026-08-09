from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum: suffix[i] = total stones from i to end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, m):
            # No piles left
            if i >= n:
                return 0

            # Can take all remaining piles
            if 2 * m >= n - i:
                return suffix[i]

            best = 0

            for x in range(1, 2 * m + 1):
                # Opponent gets dp(i+x, max(m,x))
                # Current player gets remaining stones
                best = max(best,
                           suffix[i] - dp(i + x, max(m, x)))

            return best

        return dp(0, 1)
        