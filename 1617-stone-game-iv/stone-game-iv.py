class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] represents whether the current player can win with 'i' stones remaining
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                # If removing k*k stones leaves the opponent in a losing state,
                # the current player can force a win.
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
                
        return dp[n]
        