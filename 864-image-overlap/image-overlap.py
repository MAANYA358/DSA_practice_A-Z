from typing import List
import collections

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Lists to store the (row, col) coordinates of all 1s in both images
        ones_img1 = []
        ones_img2 = []
        
        # Single O(N^2) pass to extract all the 1s from the grid
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones_img1.append((r, c))
                if img2[r][c] == 1:
                    ones_img2.append((r, c))
                    
        # Dictionary to track the frequency of each translation vector
        # Keys will be tuples: (row_shift, col_shift), Values will be their count
        vector_counts = collections.defaultdict(int)
        
        # Variable to track the absolute maximum overlaps found
        max_overlaps = 0
        
        # Compare every '1' in img1 against every '1' in img2
        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:
                # Calculate the exact shift needed to align (r1, c1) onto (r2, c2)
                translation_vector = (r2 - r1, c2 - c1)
                
                # Increment the count for this specific shift operation
                vector_counts[translation_vector] += 1
                
                # Update the global maximum if this shift produces a new highest overlap
                max_overlaps = max(max_overlaps, vector_counts[translation_vector])
                
        # Return the highest frequency count found (or 0 if no 1s exist)
        return max_overlaps
        