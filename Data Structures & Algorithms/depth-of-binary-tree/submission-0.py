# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root: Optional[TreeNode]) -> int:
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        depth = height(root.left) + height(root.right)
        return max(depth, max(left_depth, right_depth))