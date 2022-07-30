package go_leetcode

import (
	"testing"
)

func TestSplitListToParts(t *testing.T) {
	head := &ListNode{}
	node := head
	for _,val := range []int{1,2,3}{
		node.Next = &ListNode{
			Val:  val,
		}
		node = node.Next
	}
	head = head.Next
	splitListToParts(head,5)
}

type ListNode struct {
	Val int
	Next *ListNode
}

func splitListToParts(head *ListNode, k int) []*ListNode {
	p := head
	count := 0
	for p != nil{
		count++
		p = p.Next
	}
	divide := count / k
	remain := count % k
	L := []int{}
	for i:=0; i < k; i++{
		if remain > 0{
			tmp := divide
			tmp++
			remain--
			L = append(L, tmp)
		}else{
			L = append(L, divide)
		}
	}
	parts := make([]*ListNode, k)
	curr := head
	for i,val := range L{
		parts[i] = curr
		for j := 1; j < val; j++ {
			curr = curr.Next
		}
		if curr == nil{
			break
		}
		curr, curr.Next = curr.Next, nil
	}
	return parts
}

