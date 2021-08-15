package go_leetcode

import "testing"

func TestSearch(t *testing.T) {
	res := search([]int{1,2,3,45,5},-1)
	t.Log("res:",res)
}