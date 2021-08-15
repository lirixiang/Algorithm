package decorator

import (
	"fmt"
	"testing"
)

func Double(x,y int) int  {
	return x + y
}

func TestLogDecorate(t *testing.T) {
	wrap := LogDecorate(Double)
	r := wrap(6)
	fmt.Println(r)
}
