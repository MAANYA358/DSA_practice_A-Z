class Solution:
    def countCommas(self, n: int) -> int:
        # Initialize the total count of commas to 0
        total_commas = 0
        
        # The first comma appears when numbers reach 1,000
        base = 1000
        
        # Keep adding commas as long as 'n' is large enough to hit the current base
        while n >= base:
            # Add all numbers that are greater than or equal to the current base
            # The + 1 ensures the base number itself is included in the count
            total_commas += (n - base + 1)
            
            # Multiply the base by 1,000 to check for the next comma position 
            # (e.g., from 1,000 to 1,000,000)
            base *= 1000
            
        # Return the final calculated count
        return total_commas
        