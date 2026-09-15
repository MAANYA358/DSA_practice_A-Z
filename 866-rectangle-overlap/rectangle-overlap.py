from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # A valid rectangle must have a positive area.
        # If the left edge equals the right edge (x1 == x2) or bottom equals top (y1 == y2),
        # the rectangle is a line or a point, and cannot overlap by definition.
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
            
        # Condition 1: rec1 is completely to the left of rec2
        # (rec1's rightmost edge is less than or equal to rec2's leftmost edge)
        is_left = rec1[2] <= rec2[0]
        
        # Condition 2: rec1 is completely to the right of rec2
        # (rec1's leftmost edge is greater than or equal to rec2's rightmost edge)
        is_right = rec1[0] >= rec2[2]
        
        # Condition 3: rec1 is completely below rec2
        # (rec1's topmost edge is less than or equal to rec2's bottommost edge)
        is_bottom = rec1[3] <= rec2[1]
        
        # Condition 4: rec1 is completely above rec2
        # (rec1's bottommost edge is greater than or equal to rec2's topmost edge)
        is_top = rec1[1] >= rec2[3]
        
        # If any of the 4 separation conditions are True, they do not overlap.
        # We invert the result using 'not' to return True only if they DO overlap.
        return not (is_left or is_right or is_bottom or is_top)
        