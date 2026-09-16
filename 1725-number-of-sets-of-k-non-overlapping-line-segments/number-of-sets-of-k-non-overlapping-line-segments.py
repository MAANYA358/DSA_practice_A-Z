import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # Define the modulo constant as required by the problem constraints
        MOD = 10**9 + 7
        
        # Calculate the expanded number of points to account for shared endpoints
        # n points + (k - 1) virtual points inserted between potential touching segments
        total_points = n + k - 1
        
        # Every segment requires exactly 2 points (a start and an end)
        points_to_choose = 2 * k
        
        # If the number of points to choose is greater than available points, 0 sets can be formed
        if points_to_choose > total_points:
            return 0
            
        # Calculate the mathematical combination: (total_points) Choose (points_to_choose)
        # Python's math.comb is highly optimized and written in C
        ways = math.comb(total_points, points_to_choose)
        
        # Return the final count of valid sets, modulo 10^9 + 7
        return ways % MOD
        