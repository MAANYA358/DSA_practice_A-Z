class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Get the length of the source string 's'
        m = len(s)
        # Get the length of the target string 't'
        n = len(t)
        
        # Initialize a 1D DP array of size n + 1 with all zeros
        # dp[j] will store the number of ways to form the prefix t[0...j-1]
        dp = [0] * (n + 1)
        
        # Base case: There is exactly 1 way to form an empty string t
        # (by choosing to delete all characters from any prefix of s)
        dp[0] = 1
        
        # Iterate through every character in the source string 's'
        for i in range(1, m + 1):
            # Iterate backwards through the target string 't'
            # Going backwards ensures we don't reuse the current s[i-1] character multiple times
            for j in range(n, 0, -1):
                # If the current character in 's' matches the current character in 't'
                if s[i - 1] == t[j - 1]:
                    # Add the combinations from the previous prefix t[0...j-2]
                    # to the existing combinations for the current prefix t[0...j-1]
                    dp[j] += dp[j - 1]
                    
        # The last element holds the total ways to form the complete string 't'
        return dp[n]
        