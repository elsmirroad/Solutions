from lc import *
# ============================================================
# 1756. Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# ============================================================


class Solution:
    def minimumDeletions(self, s: str) -> int:
        t = n = len(s)
        cB = cA = 0
        bBefore, aAfter = [0] * n, [0] * n
        
        for i in range(n):
            bBefore[i] = cB
            cB += 1 if s[i] == 'b' else 0
            
        for i in range(n-1, -1, -1):
            aAfter[i] = cA
            cA += 1 if s[i] == 'a' else 0
            
        for i in range(n):
            sumD = aAfter[i] + bBefore[i]
            t = min(t, sumD)

        return t


class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = dels = 0
        for char in s:
            if char == 'b': bCount += 1
            else: dels = min(dels+1, bCount)
        return dels


class Solution:
    def minimumDeletions(self, s: str) -> int:
        total = cnt = 0
        for char in s:
            if char == 'b':
                cnt += 1
            elif cnt:
                total += 1
                cnt -= 1
        return total


test("""
You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.
 
Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

 
Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.


""")
