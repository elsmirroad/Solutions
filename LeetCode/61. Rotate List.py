from lc import *
# ==========================================
# 61. Rotate List
# https://leetcode.com/problems/rotate-list/
# ==========================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head: return head

        t, r = 0, []
        while head:
            t += 1
            r.append(head.val)
            head = head.next

        k = k % t
        r[:] = r[-k:] + r[:-k]
        head = ListNode(r.pop(0))
        curr = head

        while r:
            curr.next = ListNode(r.pop(0))
            curr = curr.next
        return head


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head: return head

        n, tail = 1, head
        while tail.next:
            n, tail = n+1, tail.next

        k %= n
        tail.next = head
        steps = n - k
        newTail = head
        for _ in range(steps - 1):
            newTail = newTail.next

        newHead = newTail.next
        newTail.next = None

        return newHead


test("""
Given the head of a linked list, rotate the list to the right by k places.
 
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]

 
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9


""")
