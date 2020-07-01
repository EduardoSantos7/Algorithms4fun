package main

type BinaryTree struct {
	Value       int
	Left, Right *BinaryTree
}

func NodeDepths(root *BinaryTree) int {
	if root == nil {
		return 0
	}
	return Bfs(root)
}

func Bfs(root *BinaryTree) (depth int) {
	node := root
	queue := []*BinaryTree{node, nil}
	level := 0
	was_nil := false

	for len(queue) > 0 {
		node, queue = queue[0], queue[1:]

		if node == nil {
			if was_nil {
				break
			}
			was_nil = true
			queue = append(queue, nil)
			level += 1
			continue
		}

		was_nil = false
		depth += level
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}

	return
}
