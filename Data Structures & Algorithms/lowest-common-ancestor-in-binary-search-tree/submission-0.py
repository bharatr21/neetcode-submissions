# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q: return None
        if root == p or root == q: return root
        elif p.val < root.val and q.val < root.val:
            return self.lca(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lca(root.right, p, q)
        return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        return self.lca(root, p, q)