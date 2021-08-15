package observer

import (
	"fmt"
	"testing"
	"time"
)

func TestEventObserver_OnNotify(t *testing.T) {
	n := eventNotifier{observers: map[Observer]struct{}{}}
	n.Register(&eventObserver{id: 1})
	n.Register(&eventObserver{id: 2})

	stop := time.NewTimer(10 * time.Second).C
	tick := time.NewTicker(time.Second).C

	for {
		select {
		case <-stop:
			return
		case t := <-tick:
			fmt.Println("******" )
			n.Notify(Event{Data: time.Unix(t.Unix(), 0).Format("2006-01-02 15:04:05")})
		}
	}
}