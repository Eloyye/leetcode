class Solution2:
    def integer_break(self, n : int) -> int:
        memo = {}
        def dfs(n : int) -> int:
            if n == 1:
                return 1
            elif n in memo:
                return memo[n]
            else:
                for i in range(1, n):
                    new_val = dfs(n - i) * i
                    if n in memo:
                        # I think i missed the crux of the idea of breaking integer (n - i) and NOT breaking (n - i)
                        memo[n] = max(memo[n], new_val, (n - i) * i)
                    else:
                        memo[n] = max(new_val, (n - i) * i)
                return memo[n]
        return dfs(n)

def main():
    pass

if __name__ == '__main__':
    main()