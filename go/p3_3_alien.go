package main

import . "g2d"

var as = Size{300, 300}
var b  = NewAlien(Point{100, 100})

type Alien struct {
	x, y, w, h int
	dx, dy     int
}

func NewAlien(pos Point) *Alien {
	return &Alien{pos.X, pos.Y, 20, 20, 5, 5}
}

func (b *Alien) Move() {
	if !(0 <= b.x+b.dx && b.x+b.dx <= as.W-b.w) {
		b.y += b.dy
		b.dx = -b.dx
	} else {
		b.x += b.dx
	}
}

func (b *Alien) Position() Rect {
	return Rect{b.x, b.y, b.w, b.h}
}

func update() {
	FillCanvas(Color{255, 255, 255}) // BG
	b.Move()
	DrawRect(Color{100, 100, 100}, b.Position()) // FG
}

func main() {
	InitCanvas(as)
	MainLoop(update, 1000/10)
}

