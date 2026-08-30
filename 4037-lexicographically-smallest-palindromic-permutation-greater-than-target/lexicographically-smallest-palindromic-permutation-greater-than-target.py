from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_cnt = Counter(s)
        
        # 1. Palindrome feasibility check
        odd_chars = [ch for ch, cnt in total_cnt.items() if cnt % 2 != 0]
        if len(odd_chars) > 1 or (n % 2 == 0 and len(odd_chars) > 0):
            return ""
            
        mid_char = odd_chars[0] if odd_chars else ""
        m = n // 2
        half_cnt = {ch: total_cnt[ch] // 2 for ch in total_cnt}
        
        candidates = []
        
        def make_palindrome(first_half: str) -> str:
            return first_half + mid_char + first_half[::-1]

        # 2. Check if identical first half produces a valid palindrome > target
        prefix_cnt = Counter()
        can_match_all = True
        for ch in target[:m]:
            if prefix_cnt[ch] + 1 <= half_cnt.get(ch, 0):
                prefix_cnt[ch] += 1
            else:
                can_match_all = False
                break
                
        if can_match_all:
            pal = make_palindrome(target[:m])
            if pal > target:
                candidates.append(pal)
                
        # 3. Find candidate by placing a strictly larger character in the first half
        curr_prefix = Counter()
        max_pref = 0
        for ch in target[:m]:
            if curr_prefix[ch] + 1 <= half_cnt.get(ch, 0):
                curr_prefix[ch] += 1
                max_pref += 1
            else:
                break
                
        for i in range(max_pref, -1, -1):
            if i < m:
                rem_cnt = Counter(half_cnt) - curr_prefix
                target_char = target[i]
                
                # Pick the smallest available character strictly greater than target[i]
                for code in range(ord(target_char) + 1, ord('z') + 1):
                    ch = chr(code)
                    if rem_cnt[ch] > 0:
                        rem_cnt[ch] -= 1
                        
                        suffix = []
                        for code_c in range(ord('a'), ord('z') + 1):
                            c_char = chr(code_c)
                            if rem_cnt[c_char] > 0:
                                suffix.append(c_char * rem_cnt[c_char])
                                
                        first_half = target[:i] + ch + "".join(suffix)
                        candidates.append(make_palindrome(first_half))
                        rem_cnt[ch] += 1
                        break
                        
            if i > 0:
                curr_prefix[target[i - 1]] -= 1
                
        return min(candidates) if candidates else ""