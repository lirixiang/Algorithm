package singleton

import "sync"

type singleton map[string]string

var (
	once sync.Once
	instance singleton
)

func New() map[string]string  {
	once.Do(func() {
		instance = make(singleton)
	})
	return instance
}