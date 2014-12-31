# -*- coding: utf-8 -*-
# file: TreeTraversal_prac.py
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
		print self.data

def preorder(node):
	if node.data:
		node.show()
		if node.left:
			preorder(node.left)
		if node.right:
			preorder(node.right)
def inorder(node):
	if node.data:
		if node.left:
			inorder(node.left)
		node.show()
		if node.right:
			inorder(node.right)
def postorder(node):
	if node.data:
		if node.left:
			postorder(node.left)
		if node.right:
			inorder(node.right)
		node.show()
if __name__ == '__main__':
	Root = BTree('Root')
	A = Root.insertLeft('A')
	C = A.insertLeft('C')
	D = A.insertRight('D')
	F = D.insertLeft('F')
	G = D.insertRight('G')
	B = Root.insertRight('B')
	E = B.insertLeft('E')
	print '*' * 30
	print 'Binary Tree Pre-Traversal'
	print '*' * 30
	preorder(Root)
	print '*' * 30
	print 'Binary Tree In-Traversal'
	print '*' * 30
	inorder(Root)
	print '*' * 30
	print 'Binary Tree Post-Traversal'
	print '*' * 30
	postorder(Root)