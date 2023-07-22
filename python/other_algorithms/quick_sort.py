
def partition(arr, left, right, pivot_ptr):
    left_ptr, right_ptr = left, right - 1
    while True:
        while arr[left_ptr] < arr[pivot_ptr]:
            left_ptr += 1
        while right_ptr > 0 and arr[right_ptr] > arr[pivot_ptr]:
            right_ptr -= 1
        if left_ptr >= right_ptr:
            break
        else:
            left_ptr, right_ptr = right_ptr, left_ptr
    left_ptr, right_ptr = right_ptr, left_ptr
    return left_ptr

def quicksort(arr):
    def quicksort_helper(arr, l, r):
        if (r - l) <= 0:
            return
        pivot = arr[r]
        part = partition(arr, l, r, pivot)
        quicksort()
    return quicksort_helper(arr, 0, len(arr) - 1)