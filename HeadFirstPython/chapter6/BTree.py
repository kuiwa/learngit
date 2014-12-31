# -*- coding: utf-8 -*-
# file: BTree.py
#
class BTree:
	def __init__(self, value):
		self.left = None
		self.data = value
		self.right = None
	def insertLeft(self, value):
		self.left = BTree(value)
		return self.left
	def insertRight(self, value):
		self.right = BTree(value)
		return self.right
	def show(self):
		print(self.data)
def inorder(node):
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def insert(node, value):
	if value < node.data:
		if node.left:
			insert(node.left, value)
		else:
			node.insertLeft(value)
	else:
		if node.right:
			insert(node.right, value)
		else:
			node.insertRight(value)
if __name__ == '__main__':
	l = [6, 19, 20, 18, 5, 4, 6, 8, 35, 1, 0, 5]
	Root = BTree(l[0])
	node = Root
	for i in l[1:]:
		insert(node, i)
	inorder(node)
	
