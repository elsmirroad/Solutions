from lc import *
# ============================================================
# 3714. Longest Balanced Substring II
# https://leetcode.com/problems/longest-balanced-substring-ii/
# ============================================================


class Solution:
    def longestBalanced(self, s: str) -> int:
        n, total = len(s), 0

        # One char
        i = 0
        while i < n:
            j = i
            while j < n and s[i] == s[j]: j += 1
            total = max(total, j - i)
            i = j

        if len(set(s)) == 1: return total

        # Two chars
        def two(x, y, exclude):
            res, i = 0, 0
            
            while i < n:

                if s[i] == exclude:
                    i += 1
                    continue

                m = {0: i-1}
                countX, countY = 0, 0
                while i < n and s[i] != exclude:
                    if s[i] == x: countX += 1
                    else: countY += 1
                    key = countX - countY
                    if key in m:
                        res = max(res, i - m[key])
                    else: m[key] = i
                    i += 1
            return res

        for x, y, ex in (('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')):
            total = max(total, two(x, y, ex))

        # three chars
        m = {(0, 0): -1}
        countA, countB, countC = 0, 0, 0
        for i in range(n):
            if s[i] == 'a': countA += 1
            elif s[i] == 'b': countB += 1
            else: countC += 1
            
            key = (countA - countB, countB - countC)
            if key in m:
                total = max(total, i - m[key])
            else: m[key] = i
        
        return total


test("""
You are given a string s consisting only of the characters 'a', 'b', and 'c'.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s.
 
Example 1:

Input: s = "abbac"
Output: 4
Explanation:
The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "aabcc"
Output: 3
Explanation:
The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

Example 3:

Input: s = "aba"
Output: 2
Explanation:
One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 
Constraints:

1 <= s.length <= 105
s contains only the characters 'a', 'b', and 'c'.


""")
