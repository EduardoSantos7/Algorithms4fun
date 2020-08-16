/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func largestValues(root *TreeNode) []int {
    
    if root == nil {
        return make([]int, 0)
    }
    max_in_levels := make([]int, 0)
    row := make([]*TreeNode, 0)
    row = append(row, root)
    values := make([]int, 0)
    
    for len(row) > 0 {

        for i := 0; i < len(row); i++ { values = append(values, row[i].Val);}

        
        max_in_levels = append(max_in_levels, max(values))
        
        new_row := make([]*TreeNode, 0)
        
        for _, node := range row {
            if node.Right != nil { new_row = append(new_row, node.Right) }
            
            if node.Left != nil { new_row = append(new_row, node.Left) }
        }
        
        row = new_row
        values = nil
    }
    
    return max_in_levels
}


func max(a []int) int {
    max := int(math.Inf(-1))
    for _, elem := range a {
        if elem > max { max = elem }   
    }
    return max
}