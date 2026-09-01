from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_pos = {}
        start = None
        
        # 1. Identify start position and assign a unique bit ID to each litter location
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_pos[(i, j)] = len(litter_pos)
                    
        total_litter = len(litter_pos)
        target_mask = (1 << total_litter) - 1
        
        # Edge case: No litter to collect initially
        if target_mask == 0:
            return 0
            
        # Queue elements: (x, y, current_energy, collected_mask)
        queue = deque([(start[0], start[1], energy, 0)])
        
        # max_energy_seen[x][y][mask] stores the max energy we've had at state (x, y, mask)
        # to aggressively prune sub-optimal or identical paths.
        max_energy_seen = [[[-1] * (1 << total_litter) for _ in range(n)] for _ in range(m)]
        max_energy_seen[start[0]][start[1]][0] = energy
        
        moves = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 2. BFS Traversal
        while queue:
            for _ in range(len(queue)):
                x, y, cur_e, mask = queue.popleft()
                
                # If energy is 0 and we are not on 'R' (which would have reset it), we are stuck
                if cur_e == 0:
                    continue
                    
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    # Check bounds and avoid obstacles
                    if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                        
                        # Calculate new energy (reset if 'R', else consume 1)
                        nxt_e = energy if classroom[nx][ny] == 'R' else cur_e - 1
                        
                        # Calculate new bitmask
                        nxt_mask = mask
                        if classroom[nx][ny] == 'L':
                            nxt_mask |= (1 << litter_pos[(nx, ny)])
                            
                        # Early exit: If we've collected all litter, this is the shortest path
                        if nxt_mask == target_mask:
                            return moves + 1
                            
                        # If this state yields more energy than previously seen, explore it
                        if nxt_e > max_energy_seen[nx][ny][nxt_mask]:
                            max_energy_seen[nx][ny][nxt_mask] = nxt_e
                            queue.append((nx, ny, nxt_e, nxt_mask))
                            
            moves += 1
            
        return -1
        