from lc import *
# ===========================================================
# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/
# ===========================================================


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        idxs, cntR, cntL = set(), 0, 0
        for i, char in enumerate(s+''):
            if cntL == cntR: idxs.add(i)
            if char == '(': cntL += 1
            else: cntR += 1
            if cntL == cntR: idxs.add(i)
        return ''.join(char for i, char in enumerate(s) if i not in idxs)


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, cnt = [], 0
        for char in s:
            if char == '(':
                if cnt: stack.append('(')
                cnt += 1
            else:
                if cnt != 1: stack.append(')')
                cnt -= 1
        return "".join(stack)


test("""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
 
Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

 
Constraints:

1 <= s.length <= 10^5
s[i] is either '(' or ')'.
s is a valid parentheses string.


""")
