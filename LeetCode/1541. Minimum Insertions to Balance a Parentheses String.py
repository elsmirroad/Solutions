from lc import *
# =================================================================================
# 1541. Minimum Insertions to Balance a Parentheses String
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# =================================================================================


class Solution:
    def minInsertions(self, s: str) -> int:
        d, t = 0, 0
        for char in s:
            if char == '(':
                d += 2
                if d%2: t += 1; d -= 1
            else:
                if d == 0: d += 2; t += 1
                d -= 1
        return t + d


class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "|")
        need, total = 0, 0
        for char in s:
            if char == "(": need += 2
            else:
                if char == ")": total += 1
                if need: need -= 2
                else: total += 1
        return total + need


test("""
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.
Return the minimum number of insertions needed to make s balanced.
 
Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

 
Constraints:

1 <= s.length <= 10^5
s consists of '(' and ')' only.


""")
