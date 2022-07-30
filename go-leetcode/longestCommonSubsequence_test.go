package go_leetcode

import "testing"

func TestLongestCommonSubsequence(t *testing.T) {
	text1, text2 := "abcde" , "ace"
	longestCommonSubsequence(text1, text2)
}

func longestCommonSubsequence(text1 string, text2 string) int {
	m, n := len(text1),len(text2)
	dp := make([][]int,m+1)
	for i := range dp{
		dp[i] = make([]int,n+1)
	}
	for i,word1 := range text1{
		for j, word2 := range text2{
			if word1 == word2{
				dp[i+1][j+1] = dp[i][j] + 1
			}else{
				dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
			}
		}
	}
	lcs := dp[m][n]
	return m + n - lcs * 2
}

func max(a,b int) int {
	if a > b{
		return a
	}
	return b
}