'''
输入一棵二叉树，判断该二叉树是是平衡二叉树

from isBalanceTree import *
a=TreeNode('a')
b=TreeNode('b')
c=TreeNode('c')
d=TreeNode('d')
e=TreeNode('e')
a.left=b
a.right=c
c.left=d
d.left=e
s=Solution()
s.isBalanced_Solution(a)

'''
# 节点结构：
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.flag = True

    def isBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag

    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)+1
        right = self.getDepth(root.right)+1
        if abs(left - right) > 1:
            self.flag = False
        return left if left > right else right
