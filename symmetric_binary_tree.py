# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        global same
        same = True
        ans = self._traversal(root.left, root.right)
        return same
    
    def _traversal(self, left, right):
        global same
        # print(left.val, right.val)
        if same == False: return
        if left and right:
            if left.val == right.val:
                self._traversal(left.left, right.right)
                self._traversal(left.right, right.left)
            else:
                same = False
        elif (left and not right) or (not left and right):
            same = False

if __name__ == '__main__':
    p2 = TreeNode(15, None, None)
    p1 = TreeNode(15, None, None)
    p0 = TreeNode(10, p1, p2)

    s = Solution()
    print(s.isSymmetric(p0))