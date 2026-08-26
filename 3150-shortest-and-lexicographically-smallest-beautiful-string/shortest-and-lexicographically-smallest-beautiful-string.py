class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Edge case: not enough '1's in the entire string
        if s.count('1') < k:
            return ""
        
        n = len(s)
        ans = ""
        left = 0
        ones_cnt = 0
        
        for right in range(n):
            if s[right] == '1':
                ones_cnt += 1
                
            # Once we have k ones, minimize the window from the left
            if ones_cnt == k:
                while s[left] == '0':
                    left += 1
                    
                cand = s[left : right + 1]
                
                # Check if cand is shorter or lexicographically smaller
                if ans == "" or len(cand) < len(ans):
                    ans = cand
                elif len(cand) == len(ans):
                    ans = min(ans, cand)
                    
                # Shrink window past the leftmost '1' to search for next valid window
                left += 1
                ones_cnt -= 1
                
        return ans
        