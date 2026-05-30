from lc import *
# ======================================================
# 3161. Block Placement Queries
# https://leetcode.com/problems/block-placement-queries/
# ======================================================


class SegmentTree:
    def __init__(self):
        self.st = [0] * (4 * (10**5 + 1))

    def insert(self, idx, value, node=1, l=0, r=10**5):
        if l == r:
            self.st[node] = value
            return
        mid = l + (r - l) // 2
        if idx <= mid: self.insert(idx, value, node*2, l, mid)
        else: self.insert(idx, value, node * 2 + 1, mid+1, r)
        self.st[node] = max(self.st[node * 2], self.st[node * 2 + 1])

    def check(self, ql, qr, node=1, l=0, r=10**5):
        if r < ql or l > qr: return 0
        if ql <= l and qr >= r: return self.st[node]
        mid = l + (r - l) // 2
        return max(
            self.check(ql, qr, node * 2, l, mid),
            self.check(ql, qr, node * 2 + 1, mid + 1, r)
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        total = []
        obs = SortedList([0, 10**5])
        st = SegmentTree()
        st.insert(0, 10**5)
        for q in queries:
            if q[0] == 1:
                _, x = q
                i = obs.bisect_left(x)
                l, r = obs[i-1], obs[i]
                st.insert(l, x-l)
                st.insert(x, r-x)
                obs.add(x)
            else:
                _, x, sz = q
                i = obs.bisect_left(x)
                l, r = 0, obs[i-1]
                prev = st.check(l, r-1)
                tail = x-r
                mx = max(prev, tail)
                total.append(mx >= sz)
        return total


test("""
There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.
You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.

Return a boolean array results, where results[i] is true if you can place the block specified in the i^th query of type 2, and false otherwise.
 
Example 1:

Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
Output: [false,true,true]
Explanation:

For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:

Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
Output: [true,true,false]
Explanation:


Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.


 
Constraints:

1 <= queries.length <= 15 * 10^4
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 10^4, 3 * queries.length)
The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
The input is generated such that there is at least one query of type 2.


""")
