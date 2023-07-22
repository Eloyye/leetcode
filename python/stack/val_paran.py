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
