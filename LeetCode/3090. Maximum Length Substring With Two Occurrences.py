from lc import *
# ============================================================================
# 3090. Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
# ============================================================================


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d, st, total = defaultdict(int), deque(), 0
        for char in s:
            st.append(char); d[char] += 1
            while d[char] > 2:
                d[st.popleft()] -= 1
            total = max(total, len(st))
        return total


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        return max(j - i for i, j in combinations(range(len(s)+1), 2) if max(map(s[i:j].count,s)) < 3)


test("""
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 
Example 1:

Input: s = "bcbbbcba"
Output: 4
Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"
Output: 2
Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 
Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.


""")
