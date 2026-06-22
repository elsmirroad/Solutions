from lc import *
# =========================================================
# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/
# =========================================================


class Solution:
    def maxNumberOfBalloons(self, text: str, total: int = 0) -> int:
        c, t = Counter(text), Counter('balloon')
        while True:
            c.subtract(t)
            if any(cnt < 0 for cnt in c.values()): return total
            total += 1


class Solution:
    def maxNumberOfBalloons(self, text: str, target: str = 'balloon') -> int:
        d = defaultdict(int)
        for char in text:
            if char in target: d[char] += 1
        if any(char not in d for char in target): return 0
        return min(d['b']//1, d['a']//1, d['l']//2, d['o']//2, d['n']//1)


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('b'), text.count('a'), text.count('l')//2, text.count('o')//2, text.count('n'))


test("""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
 
Example 1:


Input: text = "nlaebolko"
Output: 1

Example 2:


Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 
Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.

 
Note: This question is the same as  2287: Rearrange Characters to Make Target String.

""")
