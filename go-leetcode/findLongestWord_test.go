package go_leetcode

import "testing"

func TestFindLongestWord(t *testing.T) {
	s := "abpcplea"
	dictionary := []string{"ale","apple","monkey","plea"}
	findLongestWord(s,dictionary)
}
func findLongestWord(s string, dictionary []string)(ans  string ){
	for _,v := range dictionary{
		i := 0
		for  j := range s{
			if s[j] == v[i]{
				i++
				if len(v) == len(ans) && s > ans  || len(v) > len(ans){
					ans = v
				}
				break
			}
		}
	}
	return
}
