package array;

import java.util.*;

public class Solution {
    public static List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList<Integer> list = new ArrayList<>(); //create a new list
        //Mapping [0, n-1] -> [1, n]: set valid in-value nums[i - 1] = - abs(nums[i - 1])
        for (int i = 0; i < nums.length; i++) { //
            int num = Math.abs(nums[i]); //could be positive or neg
            nums[num - 1] = -1 * Math.abs(nums[num - 1]);
        }

        //second pass to add to list
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num > 0) {
                list.add(i + 1);
            }
        }
        return list;
    }

    public static int singleNumber(int[] nums) {
        //Basically just Xor all the nums array
        //this works because if a number is repeated then a pair of same value xor'ed must be 0
        //thus yielding last number that is not zero
        int out = nums[0];
        for (int i = 1; i < nums.length; i++) {
            out = out ^ nums[i];
        }
        return out;

    }

    public static int[][] construct2DArray(int[] original, int m, int n) {
        int length = original.length;
        int transform_len = m * n;
        if (length != transform_len) {
            int[][] out = new int[0][0];
            return out;
        }
        int[][] out = new int[m][n];
        int count = 0;
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j++) {
                out[i][j] = original[count];
                count++;
            }
        }
        return out;
    }

    public static int[] productExceptSelf(int[] nums) {
        //divide into two problems prefix and postfix:
        //this is efficient due to recurrence relations
        // prefix[i] := nums[i] * prefix[i - 1];
        // postfix[len(nums) - 1 + i] := nums[len(nums) - 1 + i] * postfix[len(nums) - 1 + i];
        // for i, num in nums: take product of prefix in i - 1 and postfix in i + 1 to get ans in i
        int len = nums.length;
        int[] ans = new int[len];
        int[] prefix = new int[len];
        int[] postfix = new int[len];
        for (int i = 0; i < len; i++) {
            int prefix_val = nums[i];
            int postfix_val = nums[len - 1 - i];
            if (i == 0) {
                prefix[i] = prefix_val;
                postfix[len - 1 - i] = postfix_val;
            } else {
                prefix[i] = prefix_val * prefix[i - 1];
                postfix[len - 1 - i] = postfix_val * postfix[len - i];
            }
        }

        for (int j = 0; j < len; j++) {
            int pre = (j == 0) ? 1 : prefix[j - 1];
            int post = (j == len - 1) ? 1 : postfix[j + 1];
            ans[j] = pre * post;
        }
        return ans;
    }

    public static int findDuplicate(int[] nums) {
        // This is another problem that contains the constraint of [1, n-1] and finding
        // a repeated value
        // we could do inplace modifaction such that we set
        // the idea is that each of the values in nums could technically map 1-1 in the index of nums
        // -1 -> absolute_val of num has already been set -> duplicate
        int len = nums.length;
        int res = -1;
        for (int i = 0; i < len; i++) {
            // n items -> [1, n - 1]
            int abs_num = Math.abs(nums[i]);
            if (nums[abs_num - 1] < 0) {
                res = abs_num;
                break;
            } else {
                //set the corresponding value
                nums[abs_num - 1] = -1 * Math.abs(nums[abs_num - 1]);
            }
        }
        // revert back into original state
        for (int i = 0; i < len; i++) {
            if (nums[i] < 0) {
                nums[i] *= -1;
            }
        }
        return res;
    }

    //Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    // this solution O(n*m) time complexity
    // O(n + m) space complexity
    public static void setZeroes(int[][] matrix) {
        int row_len = matrix.length;
        int col_len = matrix[0].length;
        boolean[] row_to_zero = new boolean[row_len];

        Arrays.fill(row_to_zero, false);

        boolean[] col_to_zero = new boolean[col_len];

        Arrays.fill(col_to_zero, false);

        for (int i = 0; i < row_len; i++) {
            for (int j = 0; j < col_len; j++) {
                //entries can be a value of 0, 1, 2, 3
                // 0 -> we have found 0 in original matrix
                // 1 -> we have found 1 in original matrix
                // 2 -> we have found 2 that had 0 set
                int num = matrix[i][j];
                if (num == 0) {
                    row_to_zero[i] = true;
                    col_to_zero[j] = true;
                }
            }
        }

        for (int i = 0; i < row_len; i++) {
            boolean is_fill = row_to_zero[i];
            if (is_fill) {
                for (int j = 0; j < col_len; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < col_len; i++) {
            boolean is_fill = col_to_zero[i];
            if (is_fill) {
                for (int j = 0; j < row_len; j++) {
                    matrix[j][i] = 0;
                }
            }
        }

    }

    //Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    // this solution O(n*m) time complexity
    // O(1) space complexity
    public static void setZeroes2(int[][] matrix) {
        int row_len = matrix.length;
        int col_len = matrix[0].length;
        int row_zero = 1;
        for (int i = 0; i < row_len; i++) {
            for (int j = 0; j < col_len; j++) {
                int num = matrix[i][j];
                if (num == 0) {
                    if (i == 0) {
                        //set row 0 to fill
                        row_zero = 0;
                    } else {
                        //set rest to fill
                        matrix[i][0] = 0;
                    }
                    //set col j to fill
                    matrix[0][j] = 0;
                }
            }
        }

        /* One issue you can face is that setting some entire rows to 0 might screw up checking cols as newly set
        * 0 will also mean that the entire column will be set to zero. We don't want that.
        *  */

        /*
        * To mitigate this, we first set zeroes to all the values in the inner matrix (not 0th row or col)
        * */
        for (int i = 1; i < row_len; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 1; j < col_len; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int j = 1; j < col_len; j++) {
            boolean isZero = matrix[0][j] == 0;
            if (isZero) {
                for (int i = 1; i < row_len; i++) {
                    matrix[i][j] = 0;
                }
            }
        }

        /* Set outer rows and columns accordingly, temp is a TEMPORARY variable */
        int temp = matrix[0][0];
        if (row_zero == 0) {
            for (int j = 0; j < col_len; j++) {
                matrix[0][j] = 0;
            }
        }
        if (temp == 0) {
            for (int i = 1; i < row_len; i++) {
                matrix[i][0] = 0;
            }
        }

    }

    /* Helper function for spiralOrder */
    public static boolean checkIfOut(int row_start, int row_end, int col_end, int col_start) {
        return (row_end < row_start) || (col_end < col_start);
    }

    public static List<Integer> spiralOrder(int[][] matrix) {
        int row_len = matrix.length;
        int col_len = matrix[0].length;
        int row_start = 0;
        int row_end = row_len - 1;
        int col_start = 0;
        int col_end = col_len - 1;
        ArrayList<Integer> list = new ArrayList<>();
        while (row_end >= row_start && col_end >= col_start) {
            //1. iterate through the columns
            for (int j = col_start; j < col_end + 1; j++) {
                int num = matrix[row_start][j];
                list.add(num);
            }
            //move pointer to avoid adding redundant values
            row_start++;
            //check if this is the last step by checking if the boundary goes out of bounds
            if (checkIfOut(row_start, row_end, col_end,col_start)) {
                break;
            }
            //2. iterate through rows
            for (int i = row_start; i < row_end + 1; i++) {
                int num = matrix[i][col_end];
                list.add(num);
            }
            col_end--;
            if (checkIfOut(row_start, row_end, col_end,col_start)) {
                break;
            }
            //3. iterate through columns
            for (int j = col_end; j >= col_start; j--) {
                int num = matrix[row_end][j];
                list.add(num);
            }
            row_end--;
            if (checkIfOut(row_start, row_end, col_end,col_start)) {
                break;
            }
            //4. iterate through rows
            for (int i = row_end; i >= row_start; i--) {
                int num = matrix[i][col_start];
                list.add(num);
            }
            //5. ensure that all start are shifted +1 and all end are shifted -1
            col_start++;
        }
        return list;
    }

    /* Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time. */
    /* Use a min heap to keep track of values in ascending order -> O(n) space and O(log(n)) time complexity
       for insertion.
        keep track of largest_so_far and then replace it if it is the longestConsecutive. If not consecutive, then
        reset to 1.
        return the longest conseq.
        */
    public static int longestConsecutive(int[] nums) {
        int lce = 0;
        int size = nums.length;
        if (size == 0) {
            return 0;
        } else if (size == 1) {
            return 1;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num: nums) {
            pq.add(num);
        }
        int val2;
        int val = pq.poll();
        int larg_sofar = 1;
        for (int i = 0; i < size - 1; i++) {
            val2 = pq.poll();
            if (val2 == val + 1) {
                larg_sofar++;
                if (larg_sofar > lce) {
                    lce = larg_sofar;
                }
            } else if ( val != val2 ) {
                larg_sofar = 1;
            }
            val = val2;
        }
        return Math.max(larg_sofar, lce);
    }

    public static HashSet<Integer> arrayToSet(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
        for (int num : nums) {
            hs.add(num);
        }
        return hs;
    }

    // somehow slower than ??????
    /* The idea with this implementation is that you want to convert nums into a HashSet -> constant lookup
    * Iterate through all of nums and check if there is NO LEFT NEIGHBOR (num - 1) -> start of a sequence
    *   -> we can call this sequence head
    * Then, check iteratively to right neighbor until there is no right neighbor ( looking for consecutive sequence )
    * update largest if the sequence is larger
    *  */
    public static int longestConsecutive2(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        HashSet<Integer> hs = arrayToSet(nums);
        int lcs = 1;
        for (int num : nums) {
            //check if left neighbor exist
            int left_neighbor = num - 1;
            boolean contains_left_neighbor = hs.contains(left_neighbor);
            if (!contains_left_neighbor) {
                //start of set
                int long_sofar = 1;
                int right = num + 1;
                while (hs.contains(right)) {
                    long_sofar++;
                    right++;
                }
                if (long_sofar > lcs) { //update lcs
                    lcs = long_sofar;
                }
            }
        }
        return lcs;
    }

    public static int firstMissingPositive(int[] nums) {
        // we want to encode nums carry information about whether or not it is missing from [1, n + 1]
        int len = nums.length;
        // first pass -> set all non-negative numbers to len + 1
        // this is to ensure that existing negative numbers do not get assumed for our encoding
        for (int i = 0; i < len; i++) {
            int num = nums[i];
            if (num <= 0) {
                nums[i] = len + 1; //
            }
        }

        //second pass -> set negative numbers if exists
        for (int i = 0; i < len; i++) {
            int num = nums[i];
            int abs_num = Math.abs(num);
            if (abs_num <= len && abs_num > 0) {
                nums[abs_num - 1] = - 1 * Math.abs(nums[abs_num - 1]); //set to negative
            }
        }

        //third pass will check for POSITIVE values because that means it either means that the mapped values
        // i + 1 hasn't been called yet or otherwise
        for (int i = 0; i < len; i++) {
            int num = nums[i];
            if (num > 0) {
                return i + 1;
            }
        }
        return len + 1;
    }

    /* You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation. */
    /*
    * This is very similar to the spiral matrix problem except for the fact that you observe that the rotation of 90
    * degrees only requires keeping track of 4 variables and do kinda like a shift to the right
    * do a while loop to ensure validity and a single iteration is going from outer matrix to inner matrix
    * then iterate from right - left or bottom - top, and do the swapping
    * after section of matrix is done, modify the counter to go inner matrix.
    *  */
    public static void rotate(int[][] matrix) {
        int n = matrix.length;
        if (n == 1) {
            return;
        }
        int left = 0;
        int right = n - 1;
        int top = 0;
        int bottom = n - 1;
        while (right >= left && bottom >= top) {
            for (int i = 0; i < (right - left); i++) {
                int first = matrix[top][left + i];
                int second = matrix[top + i][right];
                int third = matrix[bottom][right - i];
                int fourth = matrix[bottom - i][left];
                matrix[top + i][right] = first;
                matrix[bottom][right - i] = second;
                matrix[bottom - i][left] = third;
                matrix[top][left + i] = fourth;
            }
            left++;
            right--;
            top++;
            bottom--;
        }
    }

    public static void main(String[] args) {
        int[][] test1 = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
        System.out.println(test1);
        rotate(test1);
        System.out.println(test1);
    }
}
