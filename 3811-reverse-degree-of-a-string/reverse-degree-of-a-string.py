class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i, char in enumerate(s):
            position=i+1
            
        
            rev=26-(ord(char)-ord('a'))

            res+=position*rev
           
        return res