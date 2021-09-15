package go_leetcode

import "testing"

func TestChalkReplacer(t *testing.T) {
	chalk := []int{48,16,42,32,46,28,34,41,2,32,45,41,39,18,35,37}
	k := 1696
	chalkReplacer(chalk,k)
}

func chalkReplacer(chalk []int, k int) int {
	s := 0
	for i := range chalk{
		s += chalk[i]
	}
	k %= s
	for i,v := range chalk{
		if k < v{
			return i
		}
		k -= v
	}
	panic(-1)
}