# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]
            ld = dfs(root.left)
            rd = dfs(root.right)
            balanced = ld[0] and rd[0] and abs(ld[1] - rd[1]) <= 1
            return [balanced, 1 + max(ld[1], rd[1])]

        return dfs(root)[0]