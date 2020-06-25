package main

// This is the struct of the input root. Do not edit it.
type BinaryTree struct {
	Value int
	Left  *BinaryTree
	Right *BinaryTree
}

func BranchSums(root *BinaryTree) []int {
	sums := make([]int, 0)
	if root == nil {
		return sums
	}
	Dfs(root, 0, &sums)
	return sums
}

func Dfs(root *BinaryTree, current_sum int, sums *[]int) {
	new_sum := root.Value + current_sum
	// Leaf node
	if root.Left == nil && root.Right == nil {
		*sums = append(*sums, new_sum)
	} else {
		if root.Left != nil {
			Dfs(root.Left, new_sum, sums)
		}
		if root.Right != nil {
			Dfs(root.Right, new_sum, sums)
		}
	}
}
