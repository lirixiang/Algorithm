package go_leetcode

import (
	"container/heap"
	"fmt"
	"sort"
	"testing"
)

func TestFindMaximizedCapital(t *testing.T) {
	findMaximizedCapital(2,0,[]int{1,2,3},[]int{0,1,1})
}

type hp struct {
	sort.IntSlice
}

func (h hp)Less(i,j int) bool {
	return h.IntSlice[i] > h.IntSlice[j]
}
func (h *hp)Push(v interface{})  {
	h.IntSlice = append(h.IntSlice,v.(int))
}
func (h *hp)Pop()interface{}  {
	arr:= h.IntSlice
	last := arr[len(arr)-1]
	h.IntSlice = arr[:len(arr)-1]
	return last

}

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	n := len(profits)
	type pair struct {
		c,p int
	}
	arr := make([]pair,n)
	for i := 0; i < n; i++{
		arr[i] = pair{
			c: capital[i],
			p: profits[i],
		}
	}
	sort.Slice(arr, func(i, j int) bool {
		return arr[i].c < arr[j].c
	})
	fmt.Println(arr)

	h := &hp{}
	i := 0
	for k > 0{
		for i < n && arr[i].c <= w{
			heap.Push(h,arr[i].p)
			i++
		}
		if h.Len() == 0{
			break
		}
		w += heap.Pop(h).(int)
		k--
	}
	return w

}