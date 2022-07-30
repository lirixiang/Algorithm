package go_leetcode_test

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

func TestLimit(t *testing.T) {
	maxSem := 5
	SemChan := make(chan struct{},maxSem)
	wg := sync.WaitGroup{}
	maxTime := time.Duration(10)
	for i:= 0; i< 10000; i++{
		wg.Add(1)
		SemChan <- struct{}{}
		go func(i int) {
			defer func() {
				wg.Done()
				<- SemChan
			}()
			fmt.Println("正在处理请求",i)
			time.Sleep(1 * time.Second)
		}(i)
		if len(SemChan) == maxSem{
			time.Sleep(time.Second * maxTime)
		}
	}
	wg.Wait()
}
