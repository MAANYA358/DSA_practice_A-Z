class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # The problem requires the answer modulo 10^9 + 7
        MOD = 10**9 + 7
        
        # Array to store the number of distinct subsequences ending with each letter (a-z)
        last_count = [0] * 26
        
        # Variable to keep track of the total distinct subsequences formed so far
        total = 0
        
        # Iterate through every character in the string
        for char in s:
            # Get the 0-25 index for the current character (e.g., 'a' -> 0, 'b' -> 1)
            idx = ord(char) - ord('a')
            
            # Subsequences ending with this char = (all existing subsequences + the char itself)
            new_count = (total + 1) % MOD
            
            # Calculate how many truly *new* subsequences this character added
            # Subtracting the old 'last_count[idx]' removes the duplicates we counted previously
            added = (new_count - last_count[idx]) % MOD
            
            # Update the count of subsequences ending with this character
            last_count[idx] = new_count
            
            # Add the newly formed distinct subsequences to our overall total
            total = (total + added) % MOD
            
        return total
        