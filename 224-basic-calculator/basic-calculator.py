class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        curr_num = 0
        sign = 1  # 1 represents '+', -1 represents '-'

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '+':
                res += sign * curr_num
                curr_num = 0
                sign = 1
            elif ch == '-':
                res += sign * curr_num
                curr_num = 0
                sign = -1
            elif ch == '(':
                # Push the result and sign before the parenthesis onto the stack
                stack.append(res)
                stack.append(sign)
                # Reset result and sign for the inner expression
                res = 0
                sign = 1
            elif ch == ')':
                # Complete the inner calculation
                res += sign * curr_num
                curr_num = 0
                # Multiply by sign before '(' and add to previous result before '('
                res *= stack.pop()
                res += stack.pop()

        # Add any trailing operand
        res += sign * curr_num
        return res
        