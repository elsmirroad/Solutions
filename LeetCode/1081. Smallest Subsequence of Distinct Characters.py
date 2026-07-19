from lc import *
# ==========================================================================
# 1081. Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# ==========================================================================


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        f = Counter(s)
        st, seen = [], set()
        for char in s:
            f[char] -= 1
            if char in seen: continue
            while st and st[-1] > char and f[st[-1]]:
                seen.remove(st.pop())
            st.append(char); seen.add(char)
        return ''.join(st)


test("""
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
 
Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

 
Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

 
Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
""")
