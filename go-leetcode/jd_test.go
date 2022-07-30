package go_leetcode

import (
	"fmt"
	"testing"
)

func TestArr(t *testing.T) {
	//a := []int{3,4,5,6,9,10}
	////b := []int{4,7,8}
	////judge(a,b)
	//i := 0
	//j := len(a)-1
	//fmt.Println(binarySearch(a,i, j))
	fmt.Println(	lengthOfLongestSubstring("abcabcbb"))
}

func lengthOfLongestSubstring(s string) int {
	dic := map[byte]int{}
	i := -1
	res := 0
	for j := 0; j < len(s); j++{
		if _,ok := dic[s[j]];ok{
			i = Max(i, dic[s[j]])
		}
		dic[s[j]] = j
		res = Max(res, j - i)
	}
	return res
}


func Max(a, b int)int{
	if a > b{
		return a
	}
	return b
}
func judge(a, b []int)(c []int){
	m := make(map[int]struct{})
	for i := 0; i < len(b); i++{
		m[b[i]] = struct{}{}
	}

	for i := 0; i < len(a); i++{
		if _,ok := m[a[i]];!ok{
			c = append(c, a[i])
		}
	}
	fmt.Println(c)
	return c
}

func binarySearch(arr []int, i ,  j int)bool {

	target := 3
	for i <= j{
		mid := i + (j - i) / 2
		if arr[mid] == target{
			return true
		}
		if arr[mid] > target{
			return binarySearch(arr,i, mid - 1)
		}
		if arr[mid] < target{
			return binarySearch(arr, mid + 1 , j)
		}
	}
	return false
}
