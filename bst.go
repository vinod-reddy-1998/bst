package main

import "fmt"

type Node struct {
	val   int
	left  *Node
	right *Node
}

func insert(root *Node, val int) *Node {
	if root == nil {
		return &Node{val: val}
	}
	if val < root.val {
		root.left = insert(root.left, val)
	} else {
		root.right = insert(root.right, val)
	}
	return root
}

func search(root *Node, val int) bool {
	if root == nil {
		return false
	}
	if root.val == val {
		return true
	}
	if val < root.val {
		return search(root.left, val)
	}
	return search(root.right, val)
}

func delete(root *Node, val int) *Node {
	if root == nil {
		return root
	}
	if val < root.val {
		root.left = delete(root.left, val)
	} else if val > root.val {
		root.right = delete(root.right, val)
	} else {
		if root.left == nil {
			return root.right
		} else if root.right == nil {
			return root.left
		}
		minNode := root.right
		for minNode.left != nil {
			minNode = minNode.left
		}
		root.val = minNode.val
		root.right = delete(root.right, minNode.val)
	}
	return root
}

func main() {
	root := &Node{val: 5}
	insert(root, 3)
	insert(root, 8)
	insert(root, 1)
	insert(root, 4)
	insert(root, 7)
	insert(root, 10)

	fmt.Println(search(root, 3))  // true
	fmt.Println(search(root, 10)) // true
	fmt.Println(search(root, 11)) // false

	root = delete(root, 8)
	fmt.Println(search(root, 8)) // false
}
