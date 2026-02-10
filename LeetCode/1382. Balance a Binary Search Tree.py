from lc import *
# ============================================================
# 1382. Balance a Binary Search Tree
# https://leetcode.com/problems/balance-a-binary-search-tree/
# ============================================================


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes: list = list()

        def dfs(node):
            if not node: return
            l = dfs(node.left)
            nodes.append(node.val)
            r = dfs(node.right)
        dfs(root)

        def build(l: int, r: int):
            if l > r: return
            mid:int = (l + r) // 2
            node = TreeNode(nodes[mid])
            node.left = build(l, mid-1)
            node.right = build(mid+1, r)
            return node
        
        return build(0, len(nodes)-1)


test("""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
 
Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:


Input: root = [2,1,3]
Output: [2,1,3]

 
Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105


""")
