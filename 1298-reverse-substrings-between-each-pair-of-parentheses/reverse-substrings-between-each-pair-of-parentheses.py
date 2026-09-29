class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Initialize the stack to track characters and brackets
        stack = []
        
        # Process each character in the string sequentially
        for char in s:
            if char == ')':
                # Temporary list to hold the characters inside the current brackets
                temp = []
                
                # Pop characters until the most recent open bracket is found
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                    
                # Pop and discard the '(' itself
                stack.pop()
                
                # Push the automatically reversed characters back onto the stack
                # extend() adds each character individually, maintaining the new order
                stack.extend(temp)
            else:
                # Standard characters and open brackets are simply pushed
                stack.append(char)
                
        # Join the remaining characters in the stack to form the final string
        return "".join(stack)