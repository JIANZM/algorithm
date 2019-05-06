'''
重建二叉树
输入前序遍历和中序遍历，然后重建该二叉树

from TraverseTree import *
from reConstructTree import *
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
s=Solution()
t=s.reConstructTree(pre,tin)
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructTree(self, pre, tin):
        if (set(pre) != set(tin)) or not pre:
            return None
        root = TreeNode(pre[0])
        root.val = pre[0]
        i = tin.index(pre[0])
        root.left = self.reConstructTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructTree(pre[i+1:], tin[i+1:])
        return root
