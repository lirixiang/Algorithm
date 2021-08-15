package decorator

import "log"

type Object func(int)int

func LogDecorate(fn func(int,int)int) Object  {
	return func(i int) int {
		log.Println("Starting the execution with the integer", i)
		result := fn(i,i)
		log.Println("Execution is completed with the result", i)
		return result
	}
}