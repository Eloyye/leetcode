import heapq


class Solution:
    def findContentChildren(self, g : list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        child_ptr = cookie_size_ptr = content_children = 0
        while child_ptr < len(g) and cookie_size_ptr < len(s):
            child_demands, cookie_size = g[child_ptr], s[cookie_size_ptr]
            if child_demands <= cookie_size:
                content_children += 1
                cookie_size_ptr += 1
            child_ptr += 1
        return content_children


if __name__ == '__main__':
    pass