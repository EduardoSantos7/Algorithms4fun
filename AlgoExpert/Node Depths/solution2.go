package main

type BinaryTree struct {
	Value       int
	Left, Right *BinaryTree
}

func NodeDepths(root *BinaryTree) int {
	return dfs(root, 0)
}

func dfs(root *BinaryTree, depth int) int {
	if root == nil {
		return 0
	}
	return depth + dfs(root.Left, depth+1) + dfs(root.Right, depth+1)
}
