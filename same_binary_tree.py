# https://leetcode.com/problems/same-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # order_p = []
        # order_q = []
        global same
        same = True
        ans = self._traversal(p, q)
        return same
        # self._traversal(q, order_q, 'root')
        # if order_p == order_q:
        #     return 1
        # else:
        #     return 0

    def _traversal(self, p_root, q_root):
        global same
        if same == False: return
        if p_root and q_root:
            if p_root.val == q_root.val:
            # order.append((root.val, type))
                self._traversal(p_root.left, q_root.left)
                self._traversal(p_root.right, q_root.right)
            else:
                same = False
        elif (p_root and not q_root) or (not p_root and q_root):
            same = False

if __name__ == '__main__':
    p2 = TreeNode(15, None, None)
    p1 = TreeNode(5, None, None)
    p0 = TreeNode(10, p1, p2)

    # q4 = TreeNode(2, None, None)
    # q3 = TreeNode(2, None, None)
    q2 = TreeNode(15, None, None)
    q1 = TreeNode(5, None, q2)
    q0 = TreeNode(10, q1, None)

    s = Solution()
    print(s.isSameTree(p0, q0))