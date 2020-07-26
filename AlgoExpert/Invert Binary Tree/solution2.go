package main

type BinaryTree struct {
	Value int

	Left  *BinaryTree
	Right *BinaryTree
}

func (tree *BinaryTree) InvertBinaryTree() {
	queue := make([]*BinaryTree, 0)
	queue = append(queue, tree)

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		temp := node.Right
		node.Right = node.Left
		node.Left = temp

		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
}
