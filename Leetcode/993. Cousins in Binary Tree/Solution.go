/**
 * Definition for a binary tree node.
 * type c struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isCousins(root *TreeNode, x int, y int) bool {
	var y_parent *TreeNode = nil
	var x_parent *TreeNode = nil
	depth, x_level, y_level := 0, 0, 0
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)

	for len(queue) > 0 {
		aux_queue := make([]*TreeNode, 0)
		depth += 1
		for _, node := range queue {
			childs := [2]*TreeNode{node.Left, node.Right}
			same_parent := 0
			for _, child := range childs {
				if child != nil {
					aux_queue = append(aux_queue, child)

					if child.Val == x {
						same_parent += 1
						x_parent = node
						x_level = depth
					}
					if child.Val == y {
						same_parent += 1
						y_parent = node
						y_level = depth
					}
				}
			}
			if same_parent == 2 {
				return false
			}
			if x_parent != nil && y_parent != nil {
				if y_level == x_level && x_parent.Val != y_parent.Val {
					return true
				}
			}
			queue = aux_queue
		}
	}
	return false
}