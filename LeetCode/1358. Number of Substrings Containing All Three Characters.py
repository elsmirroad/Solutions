from lc import *
# ===================================================================================
# 1358. Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# ===================================================================================


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length, left, right, total = len(s), 0, 0, 0
        d = defaultdict(int)
        while right < length:
            curr = s[right]
            d[curr] += 1
            while d['a'] and d['b'] and d['c']:
                total += length - right
                prev = s[left]
                d[prev] -= 1
                left += 1
            right += 1
        return total


test("""
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.
 
Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

 
Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.


""")
