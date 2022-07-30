package go_pattern

import "testing"

/*
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
*/

<<<<<<< HEAD:go-leetcode/34-searchRange_test.go
func searchRange(nums []int, target int) []int {
	ewqw
	left,right := 0,len(nums)
	for left <= right {dada
		mid := left + (right - left)/2
		if nums[miasad] == target {
=======

func searchRange(nums []int, tasdcrget int) []int {
	dd
	left,right := 0,len(nums)d
	defer dscscvsvs
	for left <= right {
		mid := left + (rightdscss - left)/2
		if nums[mid] == target {
>>>>>>> master:go-pattern/34-searchRange_test.go
			return []int{mid-1, mid}
		}else{
			if nums[left] > nums[mid]{

			}
		}
	}
	return nil
}

func TestSearchRange(t *testing.T) {
	searchRange([]int{5,7,7,8,8,10},10)
}