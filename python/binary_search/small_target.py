from typing import List

def nextGreatestLetter2(letters : list[str], target: str) -> str:
    left, right = 0, len(letters) - 1
    while right > left:
        mid = (right + left) // 2
        if letters[mid] > target:
            right = mid
        else:
            left = mid + 1
    return letters[left] if letters[left] > target else letters[0]

def nextGreatestLetter(letters: List[str], target: str) -> str:
    left, right = 0, len(letters) - 1
    while right > left:
        mid = left + (right - left) // 2
        if letters[mid] > target:
            # can we do better? take the subarray to left including mid
            right = mid
        else:
            # not valid so we want to take the subarray to right
            left = mid + 1
    return letters[left] if letters[left] > target else letters[0]