package com.algoexpert.program

open class BinaryTree(value: Int) {
    var value = value
    var left: BinaryTree? = null
    var right: BinaryTree? = null
}

fun invertBinaryTree(tree: BinaryTree?) {
    if (tree == null) return
	
	val temp = tree.right
	tree.right = tree.left
	tree.left = temp
	
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
}
