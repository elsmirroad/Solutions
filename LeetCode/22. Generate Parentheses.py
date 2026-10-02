from lc import *
# ===================================================
# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# ===================================================


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def is_valid(s):
            stack = []
            for char in s:
                if char == "(": stack.append(char)
                else:
                    if stack and stack[-1] == "(": stack.pop()
                    else: return False
            return not stack
        def func(s):
            if len(s) == n*2:
                if is_valid(s): result.append(s)
            else:
                for par in '()': new = s+par; func(new)
        result = []
        for s in '()': func(s)
        return list(result)


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(open, close, s):
            if open == close and open + close == n*2:
                result.append(s)
                return
            if open < n:
                dfs(open+1, close, s+'(')
            if close < open:
                dfs(open, close+1, s+')')
        result = []; dfs(0, 0, '')
        return result


test("""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

 
Constraints:

1 <= n <= 8


""")
