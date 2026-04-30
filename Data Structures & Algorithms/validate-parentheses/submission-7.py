class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in check.values():
                stack.append(c)

            if c in check.keys():
                if not stack:
                    return False
                if check[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False