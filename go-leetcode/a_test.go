package go_leetcode_test

import (
	"math"
	"testing"
)

func TestTravel(t *testing.T) {

}

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func Travel(root *TreeNode) (int, int) {
	if root == nil{
		return 0,0
	}
	q := []*TreeNode{root}
	maxNum := -math.MaxInt8
	ret := [][]int{}
	for i := 0; len(q) > 0; i++{
		level := []*TreeNode{}
		ret = append(ret, []int{})
		for j := 0; j < len(q); j++{
			node := q[j]
			ret[i] = append(ret[i],node.Val)
			maxNum = max(maxNum,node.Val)
			if node.Left != nil{
				level = append(level,node.Left)
			}
			if node.Right != nil{
				level = append(level, node.Right)
			}
		}
		q = append(q, level...)
	}
	for i := 0; i < len(ret); i++ {
		for j := 0; j < len(ret[i]); j++ {
			if maxNum == ret[i][j]{
				return maxNum,i
			}
		}
	}
	return 0,0

}

func max(a, b int) int {
	if a > b{
		return a
	}
	return b
}