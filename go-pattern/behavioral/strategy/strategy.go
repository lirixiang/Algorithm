package strategy

type Operator interface {
	Apply(int,int) int
}

type Operation struct {
	Operator Operator
}

func (o *Operation)operate(leftValue,rightValue int) int {
	return o.Operator.Apply(leftValue,rightValue)
}

type Addition struct {}

func (Addition) Apply(lval,rval int) int {
	return lval + rval
}

type Multiplication struct{}

func (Multiplication) Apply(lval, rval int) int {
	return lval * rval
}