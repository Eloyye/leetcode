def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
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

threeSum([-1,0,1,2,-1,-4])