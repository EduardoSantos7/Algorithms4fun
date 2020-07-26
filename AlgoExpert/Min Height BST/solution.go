package main

func MinHeightBST(array []int) *BST {
	return MinHeightBSTHelper(array, 0, len(array)-1)
}

func MinHeightBSTHelper(array []int, start, end int) *BST {
	if end < start {
		return nil
	}
	mid := (start + end) / 2
	root := &BST{
		Value: array[mid],
		Left:  MinHeightBSTHelper(array, start, mid-1),
		Right: MinHeightBSTHelper(array, mid+1, end)}
	return root
}

type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func (tree *BST) Insert(value int) *BST {
	if value < tree.Value {
		if tree.Left == nil {
			tree.Left = &BST{Value: value}
		} else {
			tree.Left.Insert(value)
		}
	} else {
		if tree.Right == nil {
			tree.Right = &BST{Value: value}
		} else {
			tree.Right.Insert(value)
		}
	}
	return tree
}
