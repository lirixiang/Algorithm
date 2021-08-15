package singleton

import (
	"testing"
)

func TestNew(t *testing.T) {
	s := New()

	s["this"] = "that"

	s2 := New()

	t.Log("This is ", s2["this"])
}