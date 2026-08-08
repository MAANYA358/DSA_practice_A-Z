import bisect
from collections import defaultdict

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # Pre-store indices for each character in word1
        pos = defaultdict(list)
        for idx, ch in enumerate(word1):
            pos[ch].append(idx)

        def get_prev_occ(ch: str, limit: int) -> int:
            """Returns the largest index in word1 < limit where word1[index] == ch, or -1."""
            lst = pos[ch]
            idx = bisect.bisect_left(lst, limit)
            return lst[idx - 1] if idx > 0 else -1

        # last0[j]: max index in word1 for word2[j] matching word2[j:] with 0 mismatches
        last0 = [-1] * m
        p1 = n
        for j in range(m - 1, -1, -1):
            p1 = get_prev_occ(word2[j], p1)
            last0[j] = p1
            if p1 == -1:
                break

        # last1[j]: max index in word1 for word2[j] matching word2[j:] with <= 1 mismatch
        last1 = [-1] * m
        last1[m - 1] = n - 1

        for j in range(m - 2, -1, -1):
            best = -1
            # Option 1: Mismatch used at j -> word2[j+1:] matched with 0 mismatches
            if last0[j + 1] > 0:
                best = max(best, last0[j + 1] - 1)
            
            # Option 2: Exact match at j -> word2[j+1:] matched with <= 1 mismatch
            if last1[j + 1] > -1:
                p = get_prev_occ(word2[j], last1[j + 1])
                best = max(best, p)

            last1[j] = best

        # Forward greedy construction
        ans = []
        changed = False
        i = 0

        for j in range(m):
            found = False
            while i < n:
                is_equal = (word1[i] == word2[j])

                if changed:
                    # Must be an exact match and remaining suffix matched with 0 mismatches
                    is_valid = is_equal and (j == m - 1 or i < last0[j + 1])
                else:
                    if is_equal:
                        # Exact match: remaining suffix needs <= 1 mismatch
                        is_valid = (j == m - 1 or i < last1[j + 1])
                    else:
                        # Mismatch used here: remaining suffix needs 0 mismatches
                        is_valid = (j == m - 1 or i < last0[j + 1])

                if is_valid:
                    ans.append(i)
                    if not is_equal:
                        changed = True
                    i += 1
                    found = True
                    break

                i += 1

            if not found:
                return []

        return ans
        