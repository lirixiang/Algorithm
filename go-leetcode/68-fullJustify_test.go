package go_leetcode

import (
	"fmt"
	"testing"
)

/*
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
"This  is  an",
 "example of text", "justification. "
]

 */
func TestFullJustify(t *testing.T) {
	words := []string{"This", "is", "an", "example", "of", "text", "justification."}
	ws := blank(4)
	fmt.Println(ws)
	/*
	[
	   "This    is    an",
	   "example  of text",
	   "justification.  "
	]
	 */

	maxWidth := 16
	_ = fullJustify(words,maxWidth)
}

func fullJustify(words []string, maxWidth int) []string {

	LL := 0
	L := []string{}
	for i := 0; i < len(words); i++{
		word := words[i]
		LL += len(word)+1
		if LL - 1  >  maxWidth{
			break
		}
		L = append(L,word)
	}
	rowL := 0
	for i := 0; i < len(L); i++{
		rowL += len(L[i])
	}
	remain := maxWidth - rowL
	spaceInterval := len(L) - 1
	spaceIntervalCnt :=  remain / spaceInterval
	spaceRemainCnt :=  remain % spaceInterval
	fmt.Println(spaceIntervalCnt,spaceRemainCnt)

	return nil
}
func blank(n int) (s string) {
	for i := 0; i < n; i ++{
		s += " "
	}
	return
}
