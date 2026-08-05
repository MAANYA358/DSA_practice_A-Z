from typing import List
from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        # Build adjacency list
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        # Step 1: Find all suspicious methods using BFS
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    queue.append(nei)

        # Step 2: Check if any outside method invokes a suspicious method
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        # Step 3: Return remaining methods
        ans = []
        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans
        