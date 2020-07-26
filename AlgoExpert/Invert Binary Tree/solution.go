package main

type BinaryTree struct {
	Value int

	Left  *BinaryTree
	Right *BinaryTree
}

func (tree *BinaryTree) InvertBinaryTree() {
	if tree == nil {
		return
	}

	temp := tree.Right
	tree.Right = tree.Left
	tree.Left = temp

	tree.Left.InvertBinaryTree()
	tree.Right.InvertBinaryTree()
}
