package main

import . "g2d"

var ArenaW, ArenaH = 160, 120

type Ball struct {
	x, y, w, h int
	dx, dy     int
}

func NewBall(x, y int) *Ball {
	return &Ball{x, y, 20, 20, 5, 5}
}

func (b *Ball) Move() {
    if !(0 <= b.x+b.dx && b.x+b.dx <= ArenaW-b.w) {
	    b.dx = -b.dx
    }
    if !(0 <= b.y+b.dy && b.y+b.dy <= ArenaH-b.h) {
	    b.dy = -b.dy
    }
    b.x += b.dx
    b.y += b.dy
}

func (b *Ball) Position() Rect {
	return Rect{b.x, b.y, b.w, b.h}
}

func main1() {
    // Create two objects, instances of the Ball class
    b1 := NewBall(40, 80)
    b2 := NewBall(80, 40)

    for i := 0; i < 25; i++ {
        Println("Ball 1 @", b1.Position())
        Println("Ball 2 @", b2.Position())
        b1.Move()
        b2.Move()
    }
}

var balls = []*Ball{NewBall(40, 80), NewBall(80, 40)}

func update() {
    FillCanvas(Color{255, 255, 255}) // BG
    for _, b := range balls {
        b.Move()
        DrawRect(Color{100, 100, 100}, b.Position()) // FG
    }
}

func main() {
    InitCanvas(Size{ArenaW, ArenaH})
    MainLoop(update, 1000/30) // Millis
}
