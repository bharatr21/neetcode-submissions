# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lev = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while q:
            node, lvl = q.popleft()
            if node:
                lev[lvl].append(node.val)
                q.append((node.left, lvl + 1))
                q.append((node.right, lvl + 1))
        res = []
        for lvl, vals in sorted(lev.items()):
            res.append(vals)
        return res
