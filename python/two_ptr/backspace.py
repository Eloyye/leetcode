def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    n, m = len(s), len(t)
    s_ptr, t_ptr = n - 1, m - 1
    s_b, t_b = 0, 0
    while s_ptr >= 0 or t_ptr >= 0:
        while s_ptr >= 0:
            if s[s_ptr] == '#':
                s_b += 1
                s_ptr -= 1
            elif s_b > 0:
                s_b -= 1
                s_ptr -= 1
            else:
                break
        while t_ptr >= 0:
            if t[t_ptr] == '#':
                t_b += 1
                t_ptr -= 1
            elif t_b > 0:
                t_b -= 1
                t_ptr -= 1
            else:
                break
        if s_ptr >= 0 and t_ptr >= 0 and s[s_ptr] != t[t_ptr]:
            return False
        if (s_ptr >= 0) != (t_ptr >= 0):
            return False
        s_ptr -= 1
        t_ptr -= 1
    return True

backspaceCompare("ab#c", "ad#c")