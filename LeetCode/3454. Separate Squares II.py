from lc import *


# ============================================================
# 3454. Separate Squares II
# https://leetcode.com/problems/separate-squares-ii/
# ============================================================
class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, sql, sqr, lb, rb, operation, position):
        if sqr <= self.xs[lb] or sql >= self.xs[rb + 1]:  # No overlap
            return

        if sql <= self.xs[lb] and sqr >= self.xs[rb + 1]:  # Full overlap
            self.count[position] += operation

        else:  # Partial overlap
            mid = (lb + rb) // 2
            self.update(sql, sqr, lb, mid, operation, position * 2 + 1)
            self.update(sql, sqr, mid + 1, rb, operation, position * 2 + 2)

        if self.count[position] > 0:
            self.covered[position] = self.xs[rb + 1] - self.xs[lb]
        elif lb == rb:
            self.covered[position] = 0
        else:
            self.covered[position] = (
                self.covered[position * 2 + 1] + self.covered[position * 2 + 2]
            )

    def query(self):
        return self.covered[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = set()
        events = []

        for x, y, size in squares:
            xs.add(x)
            xs.add(x + size)
            events.append([y, x, x + size, 1])  # Add segment
            events.append([y + size, x, x + size, -1])  # Del segment

        xs = sorted(xs)
        events.sort()

        st = SegmentTree(xs)

        # Get Total Area
        total = 0
        py = events[0][0]

        for y, sql, sqr, operation in events:
            total += st.query() * (y - py)
            st.update(sql, sqr, 0, st.n - 1, operation, 0)
            py = y

        # Get Smallest Y for First Half of Total Area
        acc_area = 0
        py = events[0][0]
        for y, sql, sqr, operation in events:
            comb_width = st.query()
            curr_area = comb_width * (y - py)
            if acc_area + curr_area >= total / 2:
                return py + ((total / 2) - acc_area) / comb_width
            acc_area += curr_area
            st.update(sql, sqr, 0, st.n - 1, operation, 0)
            py = y


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs, events = [], []

        for x, y, size in squares:
            xs += [x, x + size]
            events.append((y, 1, x, x + size))
            events.append((y + size, -1, x, x + size))

        xs = sorted(set(xs))
        events.sort()

        idx = {v: i for i, v in enumerate(xs)}
        n = len(xs)

        cnt = [0] * (4 * n)
        seg = [0.0] * (4 * n)

        def update(node, sql, sqr, lb, rb, val):
            if rb <= sql or sqr <= lb:
                return
            if lb <= sql and sqr <= rb:
                cnt[node] += val
            else:
                mid = (sql + sqr) // 2
                update(node * 2, sql, mid, lb, rb, val)
                update(node * 2 + 1, mid, sqr, lb, rb, val)

            if cnt[node] > 0:
                seg[node] = xs[sqr] - xs[sql]
            elif sqr - sql == 1:
                seg[node] = 0
            else:
                seg[node] = seg[node * 2] + seg[node * 2 + 1]

        total = 0
        py = events[0][0]
        strips = []

        for y, t, x1, x2 in events:
            if y > py:
                height = y - py
                width = seg[1]
                total += width * height
                strips.append((py, height, width))
                py = y
            update(1, 0, n - 1, idx[x1], idx[x2], t)

        target = total / 2
        acc = 0
        for y, height, width in strips:
            if acc + height * width >= target:
                return y + (target - acc) / width
            acc += height * width
        return 0


test("""
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.
Answers within 10-5 of the actual answer will be accepted.
Note: Squares may overlap. Overlapping areas should be counted only once in this version.
 
Example 1:

Input: squares = [[0,0,1],[2,2,1]]
Output: 1.00000
Explanation:

Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

Example 2:

Input: squares = [[0,0,2],[1,1,1]]
Output: 1.00000
Explanation:

Since the blue square overlaps with the red square, it will not be counted again. Thus, the line y = 1 splits the squares into two equal parts.

 
Constraints:

1 <= squares.length <= 5 * 104
squares[i] = [xi, yi, li]
squares[i].length == 3
0 <= xi, yi <= 109
1 <= li <= 109
The total area of all the squares will not exceed 1015.


""")
