from lc import *
# ========================================================================
# 3121. Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/
# ========================================================================


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        total, low, up = 0, {}, {}
        for i, char in enumerate(word):
            if char.islower(): low[char] = i
            elif char.isupper() and char not in up: up[char] = i
        for char in set(word.lower()):
            total += 1 if char in low and char.upper() in up and low[char] < up[char.upper()] else 0
        return total


class Solution:
    def numberOfSpecialChars(self, word: str, total=0) -> int:
        for low, up in zip(ascii_lowercase, ascii_uppercase):
            if low not in word or up not in word: continue
            total += word.rfind(low) < word.find(up)
        return total


class Solution:
    def numberOfSpecialChars(self, word: str, total=0) -> int:
        return sum(word.rfind(char) < word.find(char.upper()) for char in {*word})


test("""
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word.
 
Example 1:

Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"
Output: 0
Explanation:
There are no special characters in word.

Example 3:

Input: word = "AbBCab"
Output: 0
Explanation:
There are no special characters in word.

 
Constraints:

1 <= word.length <= 2 * 10^5
word consists of only lowercase and uppercase English letters.


""")
