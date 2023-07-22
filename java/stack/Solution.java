package stack;

import java.util.HashMap;
import java.util.Stack;

public class Solution {
    public static HashMap<Character, Character> paranthesisMap() {
        HashMap<Character, Character> hm = new HashMap<>();
        hm.put(')', '(');
        hm.put('}', '{');
        hm.put(']', '[');
        return hm;
    }

    /*
     * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
     * determine if the input string is valid.
     * */
    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> hm = paranthesisMap();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (stack.empty()) {
                //so that peeking in empty stack doesn't error
                stack.push(c);
            } else if (stack.peek() == hm.get(c)) { // got the oppostive
                stack.pop();
            } else {
                //push value onto stack to be evaluated later
                stack.push(c);
            }
        }
        return stack.empty();
    }
    public static void main(String[] args) {

    }
}
