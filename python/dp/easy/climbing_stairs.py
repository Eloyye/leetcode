def climbStairs(n: int) -> int:
    if n < 4:
        return n
    n1, n2 = 2, 3
    for i in range(4, n + 1):
        n1, n2 = n2, n1 + n2
    return n2

inp = 55
res = climbStairs(inp)
print(f'The result of climbStairs({inp}): {res}')