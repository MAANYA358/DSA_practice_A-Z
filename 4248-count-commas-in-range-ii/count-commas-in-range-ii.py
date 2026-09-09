class Solution:
    def countCommas(self, n: int) -> int:
        # Initialize the total count of commas to 0
        total_commas = 0
        
        # The first comma appears when numbers reach 1,000
        base = 1000
        
        # The loop runs in O(log N) time, effortlessly handling N up to 10^18
        while n >= base:
            # Add all numbers that are greater than or equal to the current base threshold
            total_commas += (n - base + 1)
            
            # Multiply by 1,000 to advance to the next comma boundary 
            # (e.g., 1,000 -> 1,000,000 -> 1,000,000,000)
            base *= 1000
            
        # Return the final aggregated count of commas
        return total_commas