package go_leetcode

import "testing"

func TestCheckValidString(t *testing.T) {
	checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
}

func checkValidString(s string) bool {
	if len(s) == 0{
		return true
	}
	if s[0] == ')'{
		return false
	}
	left := []int{}
	star := []int{}

	for i := 0; i < len(s); i++ {
		if s[i] == '('{
			left = append(left, i)
		}
		if s[i] == '*'{
			star = append(star, i)
		}
		if s[i] == ')'{
			ll := len(left)
			sl := len(star)
			if ll > 0 {
				left = left[:len(left)-1]
			}else if sl > 0{
				star = star[:len(star)-1]
			}else{
				return false
			}
		}
	}

	for i := len(left) - 1; i >= 0; i--{
		if len(star) == 0 || star[len(star)-1] < left[i]{
			return false
		}
		star = star[:len(star)-1]
	}

	return true
}