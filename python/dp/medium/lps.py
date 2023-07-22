def longestPalindrome(self, s: str) -> str:
    LPS = ""
    LPS_size = 0
    string_len = len(s)
    def isPalindrome(l, r):
        nonlocal LPS, LPS_size
        while 0 <= l and r < string_len and s[l] == s[r]:
            if (r - l + 1) > LPS_size:
                LPS = s[l: r + 1]
                LPS_size = r - l + 1
            l -= 1
            r += 1
    for i in range(string_len):
        #odd case
        isPalindrome(i, i)
        #even case
        isPalindrome(i, i + 1)
    return LPS