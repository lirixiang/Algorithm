package go_leetcode

import "testing"

func TestNumberOfBoomerangs(t *testing.T) {
	numberOfBoomerangs([][]int{
		{0,0},
		{1,0},
		{2,0}})
}

func numberOfBoomerangs(points [][]int) (ans int) {
	for _,p := range points{
		m := map[int]int{}
		for _,q := range points{
			dis := (p[0]-q[0]) * (p[0]-q[0]) + (p[1]-q[1]) * (p[1]-q[1])
			m[dis]++
		}
		for _,v := range m {
			ans += v*(v-1)
		}
	}

	return
}
