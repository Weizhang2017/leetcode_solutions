# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# left

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.l = []
        self._traversal(root, p)
        print(self.l)

    def _traversal(self, node, target_node):
        if node:
            self.l.append(node)
            if node != target_node:
                self._traversal(node.left, target_node)
                self.l.pop()
                self._traversal(node.right, target_node)
                # self.l.pop()
        else:
            return self.l

if __name__ == '__main__':
    p2 = TreeNode(15, None, None)
    p1 = TreeNode(5, None, None)
    p0 = TreeNode(10, p1, p2)
    s = Solution()
    print(s.lowestCommonAncestor(p0, p1, p2))