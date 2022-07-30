package go_leetcode

import (
	"testing"
)

func TestIsValidSudoku(t *testing.T) {
	board := [][]byte{
		{'5','3','.','.','7','.','.','.','.'},
		{'6','.','.','1','9','5','.','.','.'},
		{'.','9','8','.','.','.','.','6','.'},
		{'8','.','.','.','6','.','.','.','3'},
		{'4','.','.','8','.','3','.','.','1'},
		{'7','.','.','.','2','.','.','.','6'},
		{'.','6','.','.','.','.','2','8','.'},
		{'.','.','.','4','1','9','.','.','5'},
		{'.','.','.','.','8','.','.','7','9'}}
	isValidSudoku(board)
}

func isValidSudoku(board [][]byte) bool {
	for i,row := range board{
		for j := range row{
			return i == j
		}
	}
	return true
}

