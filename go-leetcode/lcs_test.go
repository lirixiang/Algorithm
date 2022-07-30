package go_leetcode

import (
	"fmt"
	"testing"
)

func lcs(s1, s2 string){
	n1 := len(s1)
	n2 := len(s2)
	dp := make([][]string, n1+1)
	for i := 0; i < n1; i++{
		dp[i] = make([]string, n2+1)
	}
	//fmt.Println(dp)
	maxLen := 0
	for i := 0; i < len(s1); i++{
		for j := 0; j < len(s2); j++ {
			if s1[i] == s2[j]{
				dp[i+1][j+1] = dp[i][j] + string(s1[i])
				maxLen = Max(maxLen, len(dp[i+1][j+1]))
			}
		}
	}

 	fmt.Println(dp)
	for i := 0; i < len(s1)+1; i++ {
		for j := 0; j < len(s2)+1; j++ {
			fmt.Println(dp[i][j])
			if len(dp[i][j]) == maxLen{
				fmt.Println(dp[i][j])
			}
		}
	}
}



func TestLCS(t *testing.T) {

	lcs("abccasde","cas")
}