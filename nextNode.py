"""
二叉树的下一个结点
给定一个二叉树和其中一个结点，找出中序遍历的下一个结点并返回。结点还包含指向父结点的指针。
from nextNode import *
from TraverseTree import *
a=TreeNode('a')
b=TreeNode('b')
c=TreeNode('c')
d=TreeNode('d')
e=TreeNode('e')
f=TreeNode('f')
a.left = b
a.right = c
b.left = d
b.right = e
b.parent = a
c.parent = a
d.parent = b
e.left = f
e.parent = b
t = TraverseTree()
t.midOrder(a)
n=NextNode()
n.getNextNode(a)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return self.val


class NextNode:
    def getNextNode(self, node):
        if node:
            if node.right:
                node = node.right
                while node.left:
                    node = node.left
                return node
            else:
                while node.parent:
                    if node.parent.left == node:
                        return node.parent
                    else:
                        node = node.parent
