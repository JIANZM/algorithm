"""
对称二叉树
实现一个函数判断是否是对称二叉树
if __name__ == "__main__":
    a = TreeNode('a')
    b1 = TreeNode('b')
    b2 = TreeNode('b')
    c1 = TreeNode('c')
    c2 = TreeNode('c')
    a.left = b1
    a.right = b2
    b1.left = c1
    b2.right = c2
    s = Solution()
    print(s.isSymmetrical(a))
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, tree):
        left = tree.left
        right = tree.right
        return self._isSymmetrical(left, right)

    def _isSymmetrical(self, left, right):
        if left == right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self._isSymmetrical(left.left, right.right) or self._isSymmetrical(left.right, right.left)
