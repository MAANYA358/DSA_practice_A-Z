from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        
        # Initialize prefix sum arrays (1-indexed to elegantly handle out-of-bounds checks)
        # s[i] stores the accumulated profit up to day i using the original strategy
        s = [0] * (n + 1)
        # t[i] stores the accumulated raw prices up to day i
        t = [0] * (n + 1)
        
        # Populate the prefix sum arrays in a single O(N) pass
        for i in range(1, n + 1):
            price = prices[i - 1]
            action = strategy[i - 1]
            
            s[i] = s[i - 1] + (price * action)
            t[i] = t[i - 1] + price
            
        # The baseline maximum profit is the total profit with zero modifications
        max_profit = s[n]
        
        # Slide a window of size k from left to right across the arrays
        for i in range(k, n + 1):
            # Calculate what the window [i-k to i-1] originally contributed to the total profit
            original_window_profit = s[i] - s[i - k]
            
            # Calculate what the window will contribute after the strategy modification
            # First k/2 days are strictly '0' (hold), so they add 0 profit.
            # Last k/2 days are strictly '1' (sell), so they add the exact stock prices.
            new_window_profit = t[i] - t[i - k // 2]
            
            # The net profit if we modify this specific window
            current_modified_profit = s[n] - original_window_profit + new_window_profit
            
            # Update the global maximum if this modification is strictly better
            max_profit = max(max_profit, current_modified_profit)
            
        return max_profit
        