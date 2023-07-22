package two_ptr;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution {


     public static class ListNode {
         int val;
         ListNode next;
         ListNode() {}
         ListNode(int val) { this.val = val; }
         ListNode(int val, ListNode next) { this.val = val; this.next = next; }

         ListNode(int[] vals) {
             int size = vals.length;
             if (size == 0) {
                 return;
             }
             ListNode ptr = this;
             for (int i = 0; i < size; i++) {
                 if (i == 0) {
                     this.val = vals[i];
                 } else {
                     ListNode new_node = new ListNode(vals[i]);
                     ptr.next = new_node;
                     ptr = new_node;
                 }
             }
         }
     }

     /* Given two linked lists, merge the two lists in ascending order and return the new linked list*/
    /* 1. Check for edge cases: whether l1, l2 are empty */
    /* 2. Set head (fixed) and pointer by initializing the head -> lowest of the first heads of l1 and l2 */
    /* 3. Compare two list and add the value that is the least and increment that list*/
    /* 4. add the remaining list1 or list2 */
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
         if (list1 == null && list2 != null) {
             return list2;
         } else if (list1 != null && list2 == null) {
             return list1;
         } else if (list1 == null && list2 == null) {
             return null;
         }
         ListNode head;
         ListNode ptr;
         int list1_val = list1.val;
         int list2_val = list2.val;
         if (list1_val < list2_val) {
            head = new ListNode(list1_val);
            list1 = list1.next;
        } else {
            head = new ListNode(list2_val);
            list2 = list2.next;
        }
        ptr = head;
        while (list1 != null && list2 != null) {
            list1_val = list1.val;
            list2_val = list2.val;
            ListNode node;
            if (list1_val < list2.val) {
                node = new ListNode(list1_val);
                list1 = list1.next;
            } else {
                node = new ListNode(list2_val);
                list2 = list2.next;
            }
            ptr.next = node;
            ptr = node;
        }

        while (list1 != null) {
            list2_val = list2.val;
            ListNode node;
            node = new ListNode(list1_val);
            list1 = list1.next;
            ptr.next = node;
            ptr = node;
        }

        while (list2 != null) {
            list1_val = list1.val;
            ListNode node;
            node = new ListNode(list2_val);
            list2 = list2.next;
            ptr.next = node;
            ptr = node;
        }

        return head;
    }

    /* Simpler, recursive algorithm O(n +m) , O(1) space complexity*/
    public static ListNode mergeTwoLists_impl_2(ListNode list1, ListNode list2) {
        if (list1 == null) { //base case, if first list is null then the other list must be filled
            return list2;
        }
        if (list2 == null) {
            return list1;
        }

        if (list1.val < list2.val) {
            //list1 is now the correct path, modify its next the be the merged of
            list1.next = mergeTwoLists_impl_2(list1.next, list2); // splicing existing nodes
            return list1;
        } else {
            //list2 is now the correct path, now modify its next
            list2.next = mergeTwoLists_impl_2(list1, list2.next);
            return list2;
        }
    }

    /* Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. */
    public static int[] sortedSquares(int[] nums) {
        //have a pointer at the last negative value
        int size = nums.length;
        if (size == 0) {
            return null;
        }
        int[] out = new int[size];
        int left = 0;
        int right = 1;
        int abs_num = Math.abs(nums[0]); //4 -> 1
        for (int i = 1; i < size; i++) {
            int abs_num2 = Math.abs(nums[i]);
            if (abs_num2 - abs_num <= 0) {
                left = i - 1;
                right = i;
            } else {
                //there is a point where values are increasing
                break;
            }
            abs_num = abs_num2;
        }

        int i = 0;
        while (left >= 0 && right < size) {
            int left_square = nums[left] * nums[left];
            int right_square = nums[right] * nums[right];
            if (left_square < right_square) {
                out[i] = left_square;
                left--;
            } else {
                out[i] = right_square;
                right++;
            }
            i++;
        }

        while (left >= 0) {
            int left_square = nums[left] * nums[left];
            out[i] = left_square;
            left--;
            i++;
        }

        while (right < size) {
            int right_square = nums[right] * nums[right];
            out[i] = right_square;
            right++;
            i++;
        }

        return out;
    }

    //Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
    //Do this in O(n) time complexity and O(1) space complexity
    public static boolean backspaceCompare(String s, String t) {
        int size_s = s.length();
        int size_t = t.length();
        int s_ptr = size_s - 1;
        int t_ptr = size_t - 1;
        int s_skip = 0;
        int t_skip = 0;
        while (s_ptr >= 0 || t_ptr >= 0) { //or because we want to finish the second item
            while (s_ptr >= 0) {
                if (s.charAt(s_ptr) == '#') {
                    s_skip++;
                    s_ptr--;
                } else if (s_skip > 0) {
                    s_skip--;
                    s_ptr--;
                } else {
                    break;
                }
            }
            while (t_ptr >= 0) {
                if (t.charAt(t_ptr) == '#') {
                    t_skip++;
                    t_ptr--;
                } else if (t_skip > 0) {
                    t_skip--;
                    t_ptr--;
                } else {
                    break;
                }
            }

            // Up until this point, I have finished taking into account of all backspaces

            if (s_ptr >= 0 && t_ptr >= 0 && s.charAt(s_ptr) != t.charAt(t_ptr)) {
                // comparison whether or not the characters of the pointers at s and t are the same
                return false;
            }

            if ((s_ptr >= 0) != (t_ptr >= 0)) {
                // I have finished scanning on one of the strings but there is still the other string to be parsed
                // hence, they are not the same evaluated string.

                // e.g s = "a#c", t = "c" -> this means that t has finished before s finishes parsing
                return false;
            }

            s_ptr--;
            t_ptr--;
        }
        return true;
    }

    /* Given numbers array that is SORTED in ascending order, find exactly a pair of indices indexed at 1 s.t
    * sum of the values at those indices = target.
    *  */

    /*
    * One intuition is that we want to eliminate upper values in the numbers arrays
    * such that the sum of the pointers > target.
    *
    * Hence we can keep track of two pointers in the array, one starting from start and one starting from the end
    * The idea is that if the values are equal to target, then we have found the indices
    * if the sum overshoots target, then we must decrement the end pointer (if we increment start -> it will increase sum)
    * otherwise, if we want to increase the sum, we must increment start pointer
    * */
    public static int[] twoSum2(int[] numbers, int target) {
        int size = numbers.length;
        int start_ptr = 0;
        int end_ptr = size - 1;
        int[] out;
        while (end_ptr > start_ptr) {
            int val_start = numbers[start_ptr];
            int val_end = numbers[end_ptr];
            int sum = val_start + val_end;
            if (sum == target) {
                out = new int[]{start_ptr + 1, end_ptr + 1};
                return out;
            } else if (sum > target) {
                end_ptr--;
            } else {
                start_ptr++;
            }
        }
        out = new int[]{start_ptr + 1, end_ptr + 1};
        return out;
    }

    /*
    * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    * such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    * Notice that the solution set must not contain duplicate triplets.
    * */

    /*
    * In fact, this problem can be reduced to a two-sum problem
    * */
    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); //sort nums
        int size = nums.length;
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            int start = nums[i];
            if (i > 0 && start == nums[i - 1]) {
                continue;
            }
            int left = i + 1;
            int right = size - 1;
            while (right > left) {
                int three_sum = start + nums[left] + nums[right];
                if (three_sum == 0) {
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(start);
                    triplet.add(nums[left]);
                    triplet.add(nums[right]);
                    out.add(triplet);
                    left++;
                    while (nums[left] == nums[left - 1] && left < right) {
                        left++;
                    }
                } else if ( three_sum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        return out;
    }

    public static int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums); //sort array so it works
        int size = nums.length;
        int closest_to_target = Integer.MAX_VALUE;
        for (int i = 0; i < size; i++) {
            int num = nums[i];
            int left_ptr = i + 1;
            int right_ptr = size - 1;
            while (right_ptr > left_ptr) {
                int sum = num + nums[left_ptr] + nums[right_ptr];
                int diff = Math.abs(sum - target);
                if (sum == target) {
                    return target;
                }

                if (diff < Math.abs(closest_to_target - target)) {
                    closest_to_target = sum;
                }

                if (sum < target) {
                    left_ptr++;
                } else {
                    right_ptr++;
                }
            }
        }
        return closest_to_target;
    }

    public static void main(String[] args) {
        int[] arr1 = {0,1,1};
        threeSum(arr1);

    }
}
