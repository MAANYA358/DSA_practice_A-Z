class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        operations = []
        target_idx = 0
        
        for curr in range(1, n + 1):
            if target_idx == len(target):
                break
                
            operations.append("Push")
            
            if curr == target[target_idx]:
                target_idx += 1
            else:
                operations.append("Pop")
                
        return operations