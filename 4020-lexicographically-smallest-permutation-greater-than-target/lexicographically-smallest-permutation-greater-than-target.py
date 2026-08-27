from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_cnt = Counter(s)
        
        # Track character counts of target prefix
        prefix_cnt = Counter()
        max_pref = 0
        for i, ch in enumerate(target):
            if prefix_cnt[ch] + 1 <= total_cnt[ch]:
                prefix_cnt[ch] += 1
                max_pref += 1
            else:
                break
                
        # Try finding the longest matching prefix i from max_pref down to 0
        for i in range(max_pref, -1, -1):
            if i < n:
                # Remaining available characters after placing target[:i]
                rem_cnt = total_cnt - prefix_cnt
                
                # Find the smallest available character strictly greater than target[i]
                target_char = target[i]
                best_char = None
                for code in range(ord(target_char) + 1, ord('z') + 1):
                    ch = chr(code)
                    if rem_cnt[ch] > 0:
                        best_char = ch
                        break
                        
                if best_char:
                    # Use best_char at index i
                    rem_cnt[best_char] -= 1
                    
                    # Sort the remaining characters in ascending order
                    suffix = []
                    for code in range(ord('a'), ord('z') + 1):
                        ch = chr(code)
                        if rem_cnt[ch] > 0:
                            suffix.append(ch * rem_cnt[ch])
                            
                    return target[:i] + best_char + "".join(suffix)
            
            # Backtrack prefix_cnt for the previous position
            if i > 0:
                prefix_cnt[target[i - 1]] -= 1
                
        return ""