package strategy

import (
	"fmt"
	"testing"
)

func TestStrategyAddition(t *testing.T) {
	add := Operation{Operator: Addition{}}
	fmt.Println(add.operate(5,3))
}

func TestStrategyMultiplication(t *testing.T) {
	mul := Operation{Operator: Multiplication{}}
	fmt.Println(mul.operate(5,3))
}