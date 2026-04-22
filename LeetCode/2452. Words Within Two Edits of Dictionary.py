from lc import *
# ===================================================================
# 2452. Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
# ===================================================================


class Solution:
    def twoEditWords(self, q: List[str], d: List[str]) -> List[str]:

        def check(word, target):
            total = 0
            for i in range(len(word)):
                if word[i] != target[i]: total += 1
                if total > 2: break
            return total

        result = []
        for i in range(len(q)):
            for j in range(len(d)):
                if check(q[i], d[j]) < 3:
                    result.append(q[i]); break
        return result


class Solution:
    def twoEditWords(self, q: List[str], d: List[str]) -> List[str]:
        return [w for w in q if any(3>sum(map(ne, w, s)) for s in d)]


test("""
You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.
In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.
Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.
 
Example 1:

Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].

Example 2:

Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation:
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.

 
Constraints:

1 <= queries.length, dictionary.length <= 100
n == queries[i].length == dictionary[j].length
1 <= n <= 100
All queries[i] and dictionary[j] are composed of lowercase English letters.


""")
