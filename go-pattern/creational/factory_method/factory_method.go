package factory_method

import "io"

type Store interface {
	Open(string) (io.ReadWriteCloser,error)
}

type StoreType int

const (
	DiskStorage StoreType = 1 << iota
	TempStorage
	MemoryStorage
)

func NewStore(t StoreType) Store  {
	switch t {
	case MemoryStorage:
		return newMemoryStorage()
	case TempStorage:
		return newTempStorage()
	default:
		return newDiskStorage()
	}
}

func newMemoryStorage() Store {
	panic("")
}

func newTempStorage() Store {
	panic("")
}

func newDiskStorage() Store {
	panic("")
}