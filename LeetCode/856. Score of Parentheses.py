from lc import *
# ===================================================
# 856. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/
# ===================================================


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        lvl = total = 0
        for i, char in enumerate(s):
            if char == '(': lvl += 1
            else: lvl -= 1; total += 2**lvl if s[i-1] == '(' else 0
        return total


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == '(': stack.append(0)
            else:
                curr = stack.pop(); prev = stack.pop()
                stack.append(prev + max(2 * curr, 1))
        return stack.pop()


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return eval(s.replace('()', '+1').replace('(', '+2*('))


test("""
Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

 
Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2

 
Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.


""")
