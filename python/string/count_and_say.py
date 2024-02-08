class Solution:
    def countAndSay(self, n: int) -> str:
        def cas(n: int) -> str:
            def count_digits(prev):
                cur_char = prev[0]
                count = 0
                res = ''
                for digit_char in prev:
                    if digit_char == cur_char:
                        count += 1
                    else:
                        res += str(count) + cur_char
                        count = 1
                        cur_char = digit_char
                res += str(count) + cur_char
                return res
            if n == 1:
                return "1"
            return count_digits(cas(n - 1))


        return cas(n)


if __name__ == '__main__':
    countAndSay = Solution().countAndSay
    n = 4
    print(countAndSay(n))
