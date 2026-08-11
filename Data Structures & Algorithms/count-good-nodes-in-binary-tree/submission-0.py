# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        if not root: return good
        q = deque()
        q.append((root, root.val))
        while q:
            node, mx = q.popleft()
            if mx <= node.val:
                good += 1
            mx = max(mx, node.val)
            if node.left:
                q.append((node.left, mx))
            if node.right:
                q.append((node.right, mx))

        return good
