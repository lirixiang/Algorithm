package go_leetcode

import "testing"

func TestMinimumSwitchingTimes(t *testing.T) {
	t.Run("test", func(t *testing.T) {
		source := [][]int{
			{1,3},
			{5,4},
		}
		target := [][]int{
			{1,3},
			{6,5},
		}

		minimumSwitchingTimes(source,target)
	})
}

func quick_sort(a []int, l, r int) {
	if l >= r {
		return
	}
	i, j, key := l, r, a[l] //选择第一个数为key
	for i < j {
		for i < j && a[j] > key { //从右向左找第一个小于key的值
			j--
		}
		if i < j {
			a[i] = a[j]
			i++
		}

		for i < j && a[i] < key { //从左向右找第一个大于key的值
			i++
		}
		if i < j {
			a[j] = a[i]
			j--
		}
	}
	a[i] = key
	quick_sort(a, l, i-1)
	quick_sort(a, i+1, r)
}

func minimumSwitchingTimes(source [][]int, target [][]int) int {
	source_ := []int{}
	for i := 0; i < len(source); i++{
		for j := 0; j < len(source[i]); j++{
			source_ = append(source_,source[i][j])
		}
	}
	target_ := []int{}
	for i := 0; i < len(target); i++{
		for j := 0; j < len(target[i]); j++{
			target_ = append(target_,target[i][j])
		}
	}
	quick_sort(target_,0,len(target_)-1)
	quick_sort(source_,0,len(source_)-1)
	L := []int{}
	for i:=0; i < len(source_); i++{
		for j := 0; j < len(target_); j++{
			if source_[i] == target_[j]{
				L = append(L,source_[i])
				break
			}
		}
	}
	return  len(source_) - len(L)
}