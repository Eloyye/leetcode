
#this problem is very similar to the evaluate two string with backspace problem
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while right > left:
        #skip over all the non-alphanumeric values and is valid
        while not s[left].isalnum() and right > left:
            left += 1
        while not s[right].isalnum() and right > left:
            right -= 1
        #lower case and check if they match
        if right > left and s[left].lower() != s[right].lower():
            return False
        #don't forget to move pointer
        left += 1
        right -= 1
    return True

isPalindrome("A man, a plan, a canal: Panama")