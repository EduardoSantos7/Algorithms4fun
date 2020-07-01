package main

type BinaryTree struct {
	Value       int
	Left, Right *BinaryTree
}

type Node struct {
	Node  *BinaryTree
	Depth int
}

func NodeDepths(root *BinaryTree) (sum int) {
	stack := []Node{{Node: root, Depth: 0}}
	var current Node

	for len(stack) > 0 {
		current, stack = stack[len(stack)-1], stack[:len(stack)-1]
		if current.Node != nil {
			sum += current.Depth
			stack = append(stack, Node{Node: current.Node.Left, Depth: current.Depth + 1})
			stack = append(stack, Node{Node: current.Node.Right, Depth: current.Depth + 1})
		}
	}
	return
}
