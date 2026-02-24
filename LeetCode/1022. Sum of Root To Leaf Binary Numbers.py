from lc import *
# ============================================================
# 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# ============================================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current):
            nonlocal result
            current = (current << 1) + node.val
            
            if node.left is None and node.right is None:
                result += current
            
            if node.left: dfs(node.left, current)
            if node.right: dfs(node.right, current)
                
        result = 0
        dfs(root, 0)
        return result if root else 0


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], total=0) -> int:
        if not root: return 0

        total = (total<<1) + root.val
        if root.left is None and root.right is None:
            return total
        left = self.sumRootToLeaf(root.left, total)
        right = self.sumRootToLeaf(root.right, total)

        return left + right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return (f:=lambda root, total: root and(f(root.left, total := (total<<1) + root.val) + f(root.right, total) or total) or 0)(root,0)


test("""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
The test cases are generated so that the answer fits in a 32-bits integer.
 
Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:

Input: root = [0]
Output: 0

 
Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.


""")
