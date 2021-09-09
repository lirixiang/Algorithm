package go_leetcode

import (
	"bytes"
	"fmt"
	"strconv"
	"testing"
)

func TestParse(t *testing.T) {
	t.Run("test", func(t *testing.T) {
		//evaluate("count(max('123'))")
	})
}

func evaluate(expression string) int {
	root := buildExpr(expression)
	operations := make([]callbackFunc, 0)

	exprRes := root.ToExpr(&operations)

	for len(operations) > 0 {
		op := operations[0]
		operations = operations[1:]
		op(&operations)
	}
	return exprRes.GetValue(make(map[string]int))
}

type callbackFunc func(operator *[]callbackFunc)

type token interface{
	ToExpr(operator *[]callbackFunc) expr
}

type strToken struct{
	Val string
}

func (receiver* strToken) ToExpr(operator *[]callbackFunc) expr{
	if isDigit(receiver.Val[0]) || receiver.Val[0] == '-'{
		res, _:=strconv.Atoi(receiver.Val)
		return &constExpr{
			Val: res,
		}
	}else{
		return &varExpr{
			Name: receiver.Val,
		}
	}
}

type complexToken struct{
	tokens []token
}

func (receiver* complexToken) ToExpr(operator *[]callbackFunc) expr{
	cmd := receiver.tokens[0].(*strToken).Val
	if cmd == "sum"{
		res := &sumExpr{}
		*operator = append(*operator, func(list *[]callbackFunc) {
			res.LeftExpr = receiver.tokens[1].ToExpr(list)
			res.RightExpr = receiver.tokens[2].ToExpr(list)
		})
		return res
	} else if cmd == "set"{
		res := &setExpr{}
		*operator = append(*operator, func(list *[]callbackFunc) {
			tokenLen := len(receiver.tokens)
			pairs := receiver.tokens[1:]
			times := (tokenLen-2)>>1

			for i:= 0; i< times; i++{
				t1,t2 := pairs[i<<1], pairs[(i<<1)+1]
				res.evaluateList = append(res.evaluateList, evaluatePair{
					VarName: t1.(*strToken).Val,
					ValExpr: t2.ToExpr(list),
				})
			}

			res.ValExpr = receiver.tokens[tokenLen-1].ToExpr(list)
		})
		return res
	}else{
		panic(fmt.Sprintf("unknown command: %s", cmd))
	}
}

func buildExpr(exprStr string) token {
	depth := 0
	mainToken := &complexToken{}
	stack := []*complexToken{mainToken}

	for i:=0; i < len(exprStr); i++{
		c := exprStr[i]
		if c == '('{
			depth++
			last :=stack[len(stack)-1]
			cur := &complexToken{}
			last.tokens = append(last.tokens, cur)
			stack = append(stack, cur)
		}else if c == ')'{
			depth--
			stack = stack[0:len(stack)-1]
			if depth == 0{
				break
			}
		}else if c == ' '{
			continue
		}else {
			last :=stack[len(stack)-1]
			last.tokens = append(last.tokens, buildStrToken(&i, exprStr))
			i--
		}
	}
	return mainToken.tokens[0]
}

func buildStrToken(p *int, str string) *strToken {
	buf := bytes.Buffer{}
	for{
		i := *p
		c := str[i]
		if (c >= '0' && c <='9') || (c >= 'a' && c <= 'z') || c == '-'{
			buf.WriteByte(c)
			*p++
		}else {
			break
		}
	}
	return &strToken{
		Val: buf.String(),
	}
}

func isDigit(c uint8) bool{
	return c <= '9' && c >= '0'
}

// 表达式抽象接口
type expr interface {
	GetValue(varMapping map[string]int) int
}

// 常量表达式
type constExpr struct{
	Val int
}

func (receiver *constExpr) GetValue(map[string]int) int {
	return receiver.Val
}

// 变量表达式
type varExpr struct{
	Name string
}

func (receiver *varExpr) GetValue(varMapping map[string]int) int{
	res, _ := varMapping[receiver.Name]
	return res
}

// sum 相加表达式
type sumExpr struct{
	LeftExpr expr
	RightExpr expr
}

func (receiver *sumExpr) GetValue(varMapping map[string]int) int{
	return receiver.LeftExpr.GetValue(varMapping) + receiver.RightExpr.GetValue(varMapping)
}


// set 表达式内的赋值对
type evaluatePair struct{
	// 被赋值的变量名
	VarName string
	ValExpr expr
}

// let 表达式
type setExpr struct{
	evaluateList []evaluatePair
	ValExpr      expr
}

func (receiver *setExpr) GetValue(varMapping map[string]int) int{
	env := make(map[string]int)
	for k, v := range varMapping{
		env[k] = v
	}

	for _, pair := range receiver.evaluateList {
		env[pair.VarName] = pair.ValExpr.GetValue(env)
	}

	return receiver.ValExpr.GetValue(env)
}
