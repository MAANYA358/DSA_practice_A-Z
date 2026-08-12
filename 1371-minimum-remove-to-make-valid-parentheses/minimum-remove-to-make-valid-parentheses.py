class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        remove = set()

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            elif s[i] == ')':

                if stack:
                    stack.pop()

                else:
                    remove.add(i)

        while stack:
            remove.add(stack.pop())

        ans = []

        for i in range(len(s)):
            if i not in remove:
                ans.append(s[i])

        return "".join(ans)
        