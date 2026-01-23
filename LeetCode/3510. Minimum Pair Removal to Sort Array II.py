from lc import *
# ============================================================
# 3510. Minimum Pair Removal to Sort Array II
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
# ============================================================


class Node:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
        self.prev = None
        self.next = None


class PQItem:
    def __init__(self, first, second, cost):
        self.first = first
        self.second = second
        self.cost = cost

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.first.idx < other.first.idx
        return self.cost < other.cost


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        pq = []
        head = Node(nums[0], 0)
        current = head
        merged = [False] * len(nums)
        total, cnt = 0, 0

        for i in range(1, len(nums)): # init
            newNode = Node(nums[i], i)
            current.next = newNode
            newNode.prev = current
            heapq.heappush(
                pq,
                PQItem(
                    current,
                    newNode,
                    current.value + newNode.value
                )
            )

            cnt += 1 if nums[i-1] > nums[i] else 0

            current = newNode

        while cnt:
            item = heapq.heappop(pq)
            first, second, cost = item.first, item.second, item.cost

            if ( # checked
                merged[first.idx] 
                or merged[second.idx] 
                or first.value + second.value != cost
            ):
                continue

            total += 1

            if first.value > second.value:
                cnt -= 1

            prevNode = first.prev
            nextNode = second.next
            first.next = nextNode

            if nextNode:
                nextNode.prev = first

            if prevNode:

                if (
                    prevNode.value > first.value
                    and prevNode.value <= cost
                ):
                    cnt -= 1
                
                elif (
                    prevNode.value <= first.value
                    and prevNode.value > cost
                ):
                    cnt += 1

                
                heapq.heappush(
                    pq,
                    PQItem(
                        prevNode,
                        first,
                        prevNode.value + cost
                    )
                )

            if nextNode:

                if (
                    second.value > nextNode.value
                    and cost <= nextNode.value
                ):
                    cnt -= 1
                
                elif (
                    second.value <= nextNode.value 
                    and cost > nextNode.value
                ):
                    cnt += 1

                heapq.heappush(
                    pq,
                    PQItem(
                        first,
                        nextNode,
                        cost + nextNode.value
                    )
                )

            first.value = cost
            merged[second.idx] = True

        return total
        


test("""
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.
An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
 
Example 1:

Input: nums = [5,2,3,1]
Output: 2
Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].

The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]
Output: 0
Explanation:
The array nums is already sorted.

 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


""")
