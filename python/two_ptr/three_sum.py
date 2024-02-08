from typing import List


def threeSum2(nums : List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i, num in enumerate(nums):
        if i == 0 or nums[i] != nums[i - 1]:
            left, right = i + 1, len(nums) - 1
            while right > left:
                left_val = nums[left]
                right_val = nums[right]
                total = left_val + num + right_val
                if total == 0:
                    result.append([num, left_val, right_val])
                    left += 1
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
    return result
def threeSum(nums : List[int]) -> List[List[int]]:
    #sort so that you can reduce to 2sum II, which requires sorted array
    nums.sort()
    myList = []
    for i, num in enumerate(nums):
        #take care of duplicates in first value
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left_ptr = i + 1
        right_ptr = len(nums) - 1
        while right_ptr > left_ptr:
            #reduces to two sum
            left = nums[left_ptr]
            right = nums[right_ptr]
            sum = num + left + right
            if sum == 0:
                myList.append([num, left, right])
                left_ptr += 1 # don't forget to increment
                #take care of duplicates
                while right_ptr > left_ptr and nums[left_ptr] == nums[left_ptr - 1]:
                    left_ptr += 1
            elif sum < 0:
                left_ptr += 1
            else:
                right_ptr -= 1
    return myList

if __name__ == '__main__':
    res = threeSum2([-1,0,1,2,-1,-4])
    print(res)

