# https://leetcode.com/problems/path-sum

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if root.val == targetSum and not root.right and not root.left:
            return True

        targetSum -= root.val
        return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)

if __name__ == '__main__':
    s = Solution()
    p2 = TreeNode(15, None, None)
    p1 = TreeNode(10, None, None)
    p0 = TreeNode(10, p1, p2)
    print(s.hasPathSum(p0, 15))