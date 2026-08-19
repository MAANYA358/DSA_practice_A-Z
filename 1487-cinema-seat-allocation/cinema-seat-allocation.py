from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Map each row to a bitmask of occupied seats between 2 and 9
        row_mask = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                row_mask[r] |= (1 << c)
                
        # Bitmasks for the three valid 4-person blocks
        # Left:   seats 2, 3, 4, 5 -> (1<<2)|(1<<3)|(1<<4)|(1<<5)
        # Right:  seats 6, 7, 8, 9 -> (1<<6)|(1<<7)|(1<<8)|(1<<9)
        # Middle: seats 4, 5, 6, 7 -> (1<<4)|(1<<5)|(1<<6)|(1<<7)
        LEFT   = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        RIGHT  = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
        MIDDLE = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        
        # Rows without any reservations in seats 2-9 can fit 2 groups each
        ans = (n - len(row_mask)) * 2
        
        for mask in row_mask.values():
            left_valid = (mask & LEFT) == 0
            right_valid = (mask & RIGHT) == 0
            mid_valid = (mask & MIDDLE) == 0
            
            if left_valid and right_valid:
                ans += 2
            elif left_valid or right_valid or mid_valid:
                ans += 1
                
        return ans
        