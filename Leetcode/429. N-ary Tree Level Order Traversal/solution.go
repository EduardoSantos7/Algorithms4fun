/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
	if root == nil {
		return make([][]int, 0)
	}
	queue := make([]*Node, 0)
	queue = append(queue, root)
	result := make([][]int, 0)

	for len(queue) != 0 {
		current_level := make([]int, 0)
		next_level := make([]*Node, 0)

		for _, node := range queue {
			current_level = append(current_level, node.Val)
			for _, child := range node.Children {
				if child != nil {
					next_level = append(next_level, child)
				}
			}
		}

		result = append(result, current_level)
		queue = next_level
	}
	return result

}