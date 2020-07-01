package com.algoexpert.program

open class BinaryTree(value: Int) {
    var value = value
    var left: BinaryTree? = null
    var right: BinaryTree? = null
}

fun nodeDepths(root: BinaryTree): Int {
    // Write your code here.
    return dfs(root, 0)
}

fun dfs(root: BinaryTree?, depth: Int): Int {
	if (root == null) {
		return 0
	}
	return depth + dfs(root.left, depth + 1) + dfs(root.right, depth + 1)
}
