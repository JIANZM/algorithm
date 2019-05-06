"""
二叉树遍历
"""

from collections import deque


class TraverseTree:
    def preOrder(self, tree):
        if tree is not None:
            print(tree.val, end=' ')
            self.preOrder(tree.left)
            self.preOrder(tree.right)

    def midOrder(self, tree):
        if tree is not None:
            self.midOrder(tree.left)
            print(tree.val, end=' ')
            self.midOrder(tree.right)

    def postOrder(self, tree):
        if tree is not None:
            self.postOrder(tree.left)
            self.postOrder(tree.right)
            print(tree.val, end=' ')

    def levelOrder(self, tree):
        if tree is not None:
            q = deque()
            q.append(tree)
            while q:
                node = q.popleft()
                print(node.val, end=' ')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

