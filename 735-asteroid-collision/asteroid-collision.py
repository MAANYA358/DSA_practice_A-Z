class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for a in asteroids:
            alive = True
            
            # Collision happens only if stack has a right-moving asteroid (> 0) and current is left-moving (< 0)
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()  # Top asteroid explodes; current asteroid continues
                elif stack[-1] == -a:
                    stack.pop()  # Both asteroids explode
                    alive = False
                else:
                    alive = False  # Current asteroid explodes
            
            if alive:
                stack.append(a)
                
        return stack