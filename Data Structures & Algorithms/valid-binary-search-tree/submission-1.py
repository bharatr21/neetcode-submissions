# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValid(root: Optional[TreeNode], mini: int, maxi: int) -> bool:
    flag = True
    if not root: return True
    if root.val <= mini or root.val >= maxi: return False
    return isValid(root.left, mini, root.val) and isValid(root.right, root.val, maxi)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return isValid(root, -1000000001, 1000000001)