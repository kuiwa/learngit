# -*- coding: utf-8 -*-
# file: PySort.py
#
import sys
sys.setrecursionlimit(100000)
class BTree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    def insertLeft(self, value):
        self.left = BTree(value)
        return self.left
    def insertRight(self, value):
        self.right = BTree(value)
        return self.right
    def show(self):
        print self.data
def inorder(node):
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)
def rinorder(node):
    if node.data:
        if node.right:
            rinorder(node.right)
        node.show()
        if node.left:
            rinorder(node.left)
def insert(node, value):
    if value > node.data:
        if node.right:
            insert(node.right, value)
        else:
            node.insertRight(value)
    else:
        if node.left:
            insert(node.left, value)
        else:
            node.insertLeft(value)
lis = [ 7, 10, 11, 30, 20, 21, 22, 20, 2, 3, 4, 1 ]
root = BTree(lis[0])
node = root
for i in range(1, len(lis)):
    insert(node, lis[i])
inorder(node)
rinorder(node)
list3000 = []
for i in range(1, 3000):
    list3000.append(i)
node3000 = BTree(list3000[0])
for i in range(1, len(list3000)):
    insert(node3000, list3000[i])
rinorder(node3000)
