package builder

import "log"

type Speed float64

const (
	MPH Speed 	= 1
	KPH 		= 1.60934
)

type Color string

const (
	BlueColor  		Color = "blue"
	GreenColor   		  = "green"
	RedColor		      = "red"
)


type Wheels string

const (
	SportsWheels    	 Wheels = "sports"
	SteelWheels	     	Wheels = "steel"
)

type Car interface {
	Drive()
	Stop()
}

type Builder interface {
	Paint(Color) Builder
	Wheels(Wheels) Builder
	TopSpeed(Speed) Builder
	Build() Car
}



type CarImpl struct {
	Speed Speed
	Color Color
	Wheels Wheels
}

func (c *CarImpl) Drive()  {
	log.Print("car drive",c)
}

func (c *CarImpl) Stop()  {
	log.Print("car stop",c)
}



type NewBuilder struct {
	Car *CarImpl
}

func (c *NewBuilder)Paint(color Color) Builder {
	c.Car.Color = color
	return c
}

func (c *NewBuilder)Wheels(wheels Wheels) Builder {
	c.Car.Wheels = wheels
	return c
}

func (c *NewBuilder)TopSpeed(speed Speed) Builder {
	c.Car.Speed = speed
	return c
}

func (c *NewBuilder)Build() Car {
	return c.Car
}

