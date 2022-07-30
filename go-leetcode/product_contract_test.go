package go_leetcode

import (
	"fmt"
	"testing"
)



func Test(t *testing.T) {
	ch := make(chan int,5)
	quit := make(chan bool)
	for i := 0; i < 2; i++ {
		go func() {
			for j := 0; j < 10; j++ {
				ch <- j
			}
			quit <- true
		}()
	}

	for i := 0; i < 3; i++ {
		go func(i int) {
			for {
				select {
				case num :=  <- ch:
					fmt.Println(fmt.Sprintf("the worker is %d",i))
					fmt.Println(num)
					fmt.Println()
				}
			}
		}(i)
	}
	for i := 0; i < 2; i++ {
		<- quit
	}

}