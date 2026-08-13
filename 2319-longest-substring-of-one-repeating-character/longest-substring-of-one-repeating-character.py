class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        
        # Segment tree nodes store: (max_len, pref_len, suff_len, left_char, right_char)
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.left_char = [''] * (4 * self.n)
        self.right_char = [''] * (4 * self.n)
        
        self._build(1, 0, self.n - 1)

    def _push_up(self, node: int, l: int, r: int, mid: int):
        left_child = 2 * node
        right_child = 2 * node + 1
        left_size = mid - l + 1
        right_size = r - mid

        self.left_char[node] = self.left_char[left_child]
        self.right_char[node] = self.right_char[right_child]

        # Combine maximums from both halves
        self.max_len[node] = max(self.max_len[left_child], self.max_len[right_child])
        self.pref_len[node] = self.pref_len[left_child]
        self.suff_len[node] = self.suff_len[right_child]

        # Check boundary merge
        if self.right_char[left_child] == self.left_char[right_child]:
            cross_len = self.suff_len[left_child] + self.pref_len[right_child]
            self.max_len[node] = max(self.max_len[node], cross_len)

            if self.pref_len[left_child] == left_size:
                self.pref_len[node] = left_size + self.pref_len[right_child]
            if self.suff_len[right_child] == right_size:
                self.suff_len[node] = right_size + self.suff_len[left_child]

    def _build(self, node: int, l: int, r: int):
        if l == r:
            ch = self.s[l]
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.left_char[node] = ch
            self.right_char[node] = ch
            return

        mid = (l + r) // 2
        self._build(2 * node, l, mid)
        self._build(2 * node + 1, mid + 1, r)
        self._push_up(node, l, r, mid)

    def update(self, node: int, l: int, r: int, idx: int, ch: str):
        if l == r:
            self.left_char[node] = ch
            self.right_char[node] = ch
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, ch)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, ch)

        self._push_up(node, l, r, mid)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        
        for idx, ch in zip(queryIndices, queryCharacters):
            st.update(1, 0, len(s) - 1, idx, ch)
            ans.append(st.max_len[1])
            
        return ans
        