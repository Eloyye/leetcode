class Solution:
    def is_valid(self, str_in : str) -> bool:
        stack = []
        get_open = {'}' : '{', ']': '[', ')' : '('}
        for c in str_in:
            # check if closing
            if c in get_open:
                if stack and get_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                # open paran appends to stack
                stack.append(c)
        return not stack

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    closeToOpen = {'}': '{', ')': '(', ']':'['}
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                #you would have a mismatched opening paran and closing paran
                return False
        else:
            stack.append(c)
    return True if not stack else False
