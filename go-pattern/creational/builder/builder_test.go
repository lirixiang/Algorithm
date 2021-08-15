package builder

import (
	"testing"
)


func testBuilder(t *testing.T) {
	assembly := NewBuilder{&CarImpl{}}
	familyCar :=  assembly.Paint(RedColor).Wheels(SportsWheels).TopSpeed(MPH).Build()
	familyCar.Drive()
}

func TestNew(t *testing.T) {
	t.Run("test Builder", testBuilder)
}

