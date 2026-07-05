from lc import *
# =============================================================
# 1301. Number of Paths with Max Score
# https://leetcode.com/problems/number-of-paths-with-max-score/
# =============================================================

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n, m = len(board), len(board[0])
        dp = [[[-1, 0]] * m for _ in range(n)]; dp[-1][-1] = [0, 1]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):

                if board[i][j] in 'SX': continue
                elif board[i][j] == 'E': curr = 0
                else: curr = int(board[i][j])
                best, cnt = -1, 0

                for pi, pj in ((i+1, j), (i, j+1), (i+1, j+1)):

                    if pi >= n or pj >= m: continue
                    score, pCnt = dp[pi][pj]

                    if score > best:
                        best = score; cnt = pCnt

                    elif score == best:
                        cnt = (cnt + pCnt) % (10**9+7)

                if best != -1:
                    dp[i][j] = [best + curr, cnt]

        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]


test("""
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.
You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.
Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
In case there is no path, return [0, 0].
 
Example 1:
Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:
Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:
Input: board = ["E11","XXX","11S"]
Output: [0,0]

 
Constraints:

2 <= board.length == board[i].length <= 100

""")
