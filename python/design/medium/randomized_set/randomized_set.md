# Insert Delete GetRandom `O(1)`

# Data Structures
1. Lists, Hashmap
2. Lists have a contant time insertion and deletion at the END of the list 

# Approach
1. The first thing to notice is that to get a random sample without replacement we would need an array.
   1. value_to_index: We could have a mapping of set values to indices for getRandom operation
   2. values: array for sampling
4. insert operation:
   5. just append value to `values` array: O(1)
   6. map value_to_index of the value to last element of `values`: O(1)
7. getRandom:
   8. we can use randint of a known range `values` to get randomized results
9. Deletion:
   10. Since only the end of the insertion we must have the target value be at end of list
   11. This can be done by flipping the value at end of list to the target array
   12. make sure to update value_to_index
   13. Pop the last value and make sure to delete entry from value_to_index