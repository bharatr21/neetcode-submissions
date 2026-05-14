# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        lh = height(root.left)
        rh = height(root.right)
        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)
        return max(lh + rh, ld, rd)