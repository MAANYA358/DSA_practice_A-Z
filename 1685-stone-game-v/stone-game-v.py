from functools import cache
from itertools import accumulate
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        s = [0] + list(accumulate(stoneValue))
        
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= j:
                return 0
            
            ans = 0
            for k in range(i, j):
                l = s[k + 1] - s[i]
                r = s[j + 1] - s[k + 1]
                
                if l < r:
                    if ans >= l * 2:
                        continue
                    ans = max(ans, l + dfs(i, k))
                elif l > r:
                    if ans >= r * 2:
                        break
                    ans = max(ans, r + dfs(k + 1, j))
                else:
                    ans = max(ans, l + max(dfs(i, k), dfs(k + 1, j)))
            return ans

        return dfs(0, len(stoneValue) - 1)
        