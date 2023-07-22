from typing import List


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2
    #run binary search on the array that contains the fewest number of elements
    if len(B) < len(A):
        A, B = B, A
    #run binary search on the smaller of A and B, we defined it to be A
    l, r = 0, len(A) - 1
    while True:
        # Pointer for A
        i = (l + r ) // 2

        # Pointer for B
        j = half - i - 2

        #Handle edge cases
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if i + 1 <= len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if j + 1 <= len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            #odd
            if total % 2:
                return min(Aright, Bright)
            # even
            else:
                return max(Aleft, Bleft) + min(Aright, Bright) / 2
        elif Aleft > Bright:
            #too many elements from A
            r = i - 1
        else:
            #increase size of left partition from A
            l = i + 1

def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2
    if len(B) < len(A):
        A, B = B, A
    l, r = 0, len(A) - 1
    while True:
        i = (r + l) // 2
        j = half - i - 2
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if i < len(A) else float("infinity")
        Bleft = B[i] if i >= 0 else float("-infinity")
        Bright = B[i + 1] if i < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            #odd
            if total % 2:
                #the median must be located on the first value of the right partition
                return min(Aright, Bright)
            else:
                #max of left partition and the min of right partition
                #even means that we have to take the middle
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

