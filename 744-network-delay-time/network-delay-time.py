import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build the adjacency list
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # 2. Initialize min-heap: (current_time, current_node)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0
        
        # 3. BFS with Priority Queue (Dijkstra's)
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            # Skip if we've already found a shorter path to this node
            if node in visited:
                continue
                
            # Mark as visited and record the time
            visited.add(node)
            max_time = max(max_time, time)
            
            # Add neighbors to the heap
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        # 4. Check if the signal reached all 'n' nodes
        return max_time if len(visited) == n else -1
        