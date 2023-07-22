from collections import defaultdict


def checkInclusion(self, s1: str, s2: str) -> bool:
    s1_freq, s2_freq = defaultdict(int), defaultdict(int)
    for c in s1:
        s1_freq[c] += 1
    have, need = 0, len(s1_freq)
    left = 0
    for right, c in enumerate(s2):
        #check if character are part of characters in s1
        if c in s1_freq:
            #increment the count for that
            s2_freq[c] += 1
            #check whether for that particular character contains all the count of characters
            if s2_freq[c] == s1_freq[c]:
                have += 1
        # violating condition: if window is bigger than the permutation string
        if right - left + 1 > len(s1):
            # decrease have if the left ptr contains a value in s1
            if s2[left] in s1_freq and s2_freq[s2[left]] == s1_freq[s2[left]]:
                have -= 1
            # decrease frequency in s2
            s2_freq[s2[left]] -= 1
            # decrease window
            left += 1
        #check whether or not we have reached to point of have == need
        if have == need:
            return True
    return False

checkInclusion("ab", "eidboaoo")