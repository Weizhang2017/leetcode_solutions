# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else:
            return []

if __name__ == '__main__':
    node_left = TreeNode(1)
    node_right = TreeNode(2)
    root = TreeNode(0, node_left, node_right)
    s = Solution()
    print(s.preorderTraversal(root))
    
