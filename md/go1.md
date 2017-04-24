title: Go language
subtitle: Programming paradigms
figure: images/dev/gopher.jpg

---

title: Hello, Gopher

code: go

    package main

    import "fmt"

    func main() {
        fmt.Println("Hello, Gopher")
    }

code: shell

    go run hello.go

---

title: Packages

- Import statements can be separated, or *factored*
- *Package name* = last element of *import path*
- A package exports only names starting with a *capital letter*

code: go

    package main

    import (
        "fmt"
        "math/rand"
        "time"
    )

    func main() {
        rand.Seed(time.Now().UnixNano())
        fmt.Println("My favorite number is", rand.Intn(10))
    }

---

title: Functions

- Type comes after variable name (or multiple names)
- Call by value

code: go

    func hypotenuse(a, b float64) float64 {
        return math.Sqrt(a * a + b * b)
    }

    func main() {
        fmt.Println(hypotenuse(3, 4))
    }

---

title: Multiple results

- Go does *not* have built-in *tuples*
- But functions can return multiple values

code: go

    func swap(x, y string) (string, string) {
        return y, x
    }

    func main() {
        a, b := swap("hello", "world")
        fmt.Println(a, b)
    }

---

title: Named return values

- Go's return values may be named (~ local variables)
- To document the meaning of return values
- *Naked return*

code: go

    func coords(index, width int) (x, y int) {
        x = index % width
        y = index / width
        return
    }

    func main() {
        fmt.Println(coords(15, 6))
    }

---

title: Variables

- Variables can be created with `var` (or `const`...)
    - If initial value, type can be omitted (**type inference**)
    - If no initial value, their *zero value* is assigned
- Variables can also be created with `:=`

code: go

    func main() {
        var i, j int = 1, 2
        k := 3
        c, python, java := true, false, "no!"

        fmt.Println(i, j, k, c, python, java)
    }

---

title: Basic types

- `bool`
- `string` - Sequence of bytes, source is *utf-8*
- `int, uint` - 32 or 64 bits, system-dependent
- `int8, int16, int32, int64`
- `uint8, uint16, uint32, uint64`
- `float32, float64`
- `complex64, complex128`
- `byte` - Alias for `uint8`
- `rune` - Alias for `int32`, a *Unicode code point*
    - Obtained for example through a *for range*...
- `uintptr` - An int representing a pointer, unsafe
- Note: casts are always *explicit*

---

title: For loops

- Only one looping construct, the **`for`** loop
- Init statement; condition; post statement
- All are optional...
- No parentheses, but mandatory braces

code: go

    sum := 0
    for i := 0; i < 10; i++ {
        sum += i
    }
    fmt.Println(sum)

---

title: While and forever

code: go

    sum := 1
    for sum < 1000 {
        sum += sum
    }
    fmt.Println(sum)

code: go

    for {
    }
    
---

title: If selections

- Init statement; condition
- Init is optional
- No parentheses, but mandatory braces

code: go

    func pow(x, n, lim float64) float64 {
        if v := math.Pow(x, n); v < lim {
            return v
        } else {
            fmt.Printf("%g >= %g\n", v, lim)
        }
        // can't use v here, though
        return lim
    }
    // test: pow(3, 2, 10), pow(3, 3, 20)

---

title: Switch selections

- Optional init statement and condition
- Implicit break, unless `case` ends with `fallthrough`

code: go

    fmt.Print("Go runs on ")
    switch os := runtime.GOOS; os {
    case "darwin":
        fmt.Println("OS X.")
    case "linux":
        fmt.Println("Linux.")
    default:
        // freebsd, openbsd,
        // plan9, windows...
        fmt.Printf("%s.", os)
    }
    
---

title: Switch w/o condition

- Clean chain of selections

code: go

    t := time.Now()
    switch {
    case t.Hour() < 12:
        fmt.Println("Good morning!")
    case t.Hour() < 17:
        fmt.Println("Good afternoon.")
    default:
        fmt.Println("Good evening.")
    }

---

title: Defer

- Statement to defer execution of a function...
- Until the surrounding function ends
- Deferred functions are pushed in a stack (*LIFO*)
- Arguments are evaluated immediately

code: go

    func main() {
        defer fmt.Println("world")

        fmt.Println("hello")
    }

---

title: Pointers

- Like C, w/o pointer arithmetics

code: go

    i, j := 42, 2701

    p := &i         // point to i
    fmt.Println(*p) // read i through the pointer
    *p = 21         // set i through the pointer
    fmt.Println(i)  // see the new value of i

    p = &j         // point to j
    *p = *p / 37   // divide j through the pointer
    fmt.Println(j) // see the new value of j

---

title: Structs

- A `struct` is a collection of fields
- Fields accessed using a *dot*

code: go

    type Vertex struct {
        X int
        Y int
    }

    func main() {
        v := Vertex{1, 2}
        v.X = 4
        fmt.Println(v)
    }

---

title: Pointers to structs

- Access to fields: we could write `(*p).X`, or...
- Just `p.X`, without the explicit *dereference*

code: go

    v := Vertex{1, 2}
    p := &v
    p.X = 4
    fmt.Println(v)

---

title: Struct literals

- Fields can be intialized by name

code: go

    v1 = Vertex{1, 2}  // has type Vertex
    v2 = Vertex{X: 1}  // Y:0 is implicit
    v3 = Vertex{}      // X:0 and Y:0
    p  = &Vertex{1, 2} // has type *Vertex

---

title: Arrays

- A numbered sequence of elements of a single type with a fixed length

code: go

    var a [2]string
    a[0] = "Hello"
    a[1] = "World"
    fmt.Println(a[0], a[1])
    fmt.Println(a)

    primes := [6]int{2, 3, 5, 7, 11, 13}
    fmt.Println(primes)

---

title: Slices

- A segment of an underlying array
- It does not store any data
- Changes are applied to the underlying array
- Visible to other slices sharing the same array

code: go

    primes := [6]int{2, 3, 5, 7, 11, 13}  // an array

    var s []int = primes[1:4]             // a slice
    fmt.Println(s)

- Slice literal: create an array and get a slice over it

code: go

    q := []int{2, 3, 5, 7, 11, 13}

---

title: Multiple slices

code: go

    names := [4]string{
        "John",
        "Paul",
        "George",
        "Ringo",
    }
    fmt.Println(names)

    a := names[0:2]
    b := names[1:3]
    fmt.Println(a, b)

    b[0] = "XXX"
    fmt.Println(a, b)
    fmt.Println(names)

---

title: Length and capacity

- Length of a slice `s`: number of elements it contains, `len(s)`
- Capacity of a slice `s`: number of elements in the underlying array, `cap(s)`
- `nil`: slice with `0` for both len and cap
- Note: when slicing, high or low bounds can be omitted

code: go

    func printSlice(s []int) {
        fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
    }

---

title: Re-slicing

code: go

    s := []int{2, 3, 5, 7, 11, 13}
    printSlice(s)

    s = s[:0]  // Slice the slice to give it zero length
    printSlice(s)

    s = s[:4]  // Extend its length
    printSlice(s)

    s = s[2:]  // Drop its first two values
    printSlice(s)

---

title: Slices of slices

code: go

    // Create a tic-tac-toe board.
    board := [][]string{
        []string{"_", "_", "_"},
        []string{"_", "_", "_"},
        []string{"_", "_", "_"},
    }

    // The players take turns.
    board[0][0] = "X"
    board[2][2] = "O"
    board[1][2] = "X"
    board[1][0] = "O"
    board[0][2] = "X"

    for i := 0; i < len(board); i++ {
        fmt.Printf("%s\n", board[i])
    }
    
---

title: Appending to a slice

- `append`: returns a slice containing all original elements, plus provided value(s)
- If the backing array is too small, a bigger array will be allocated

code: go

    var s []int
    printSlice(s)

    s = append(s, 0)  // append works on nil slices
    printSlice(s)

    s = append(s, 1)  // The slice grows as needed
    printSlice(s)

    s = append(s, 2, 3, 4)  // Add more elements
    printSlice(s)

---

title: Ranges

- Range `for` loop, to iterate over a slice
- Two values are returned for each iteration: index, copy of the element
- Drop the index using `_`, or drop the value entirely

code: go

    pow := []int{1, 2, 4, 8, 16, 32, 64, 128}

    for i, v := range pow {
        fmt.Printf("2**%d = %d\n", i, v)
    }

---

title: Maps

- An unordered collection of key-value pairs
- Aka associative array, hash table, or dictionary

code: go

    x := make(map[string]int)
    x["key"] = 10
    fmt.Println(x["key"])
    
---

title: Map literals

code: go

    m := map[string]Vertex{
        "Bell Labs": {40.68433, -74.39967},
        "Google":    {37.42202, -122.08408},
    }

- Delete an element: `delete(m, key)`
- Test that a key is present: `elem, ok := m[key]`
    - If `key` is not in the map, then `elem` is the zero value and `ok` is `false`

---

title: Higher order functions

- Functions are values too: they may be used as function arguments and return values

code: go

    func compute(fn func(float64, float64) float64) float64 {
        return fn(3, 4)
    }

    func main() {
        hypotenuse := func(x, y float64) float64 {
            return math.Sqrt(x*x + y*y)
        }
        fmt.Println(hypotenuse(5, 12))

        fmt.Println(compute(hypotenuse))
        fmt.Println(compute(math.Pow))
    }

---

title: Closures

- A function referencing outside variables

code: go

    // f. that returns a f. that returns an int
    func fibonacci() func() int {
        curr, next := 0, 1
        return func() int {
            val := curr
            curr, next = next, next + curr
            return val
        }
    }
    func main() {
        f := fibonacci()
        for i := 0; i < 10; i++ {
            fmt.Println(f())
        }
    }

---

title: Methods

- No classes, but possible to define methods on types
- A method is just a function with a *receiver* argument
- The receiver type must be defined in the same *package*

code: go

    type Vertex struct {
        X, Y float64
    }

    func (v Vertex) Abs() float64 {
        return math.Sqrt(v.X*v.X + v.Y*v.Y)
    }

    func main() {
        v := Vertex{3, 4}
        fmt.Println(v.Abs())
    }

---

title: Pointer receivers

- Methods with pointer receivers can modify the receiver obj
- Convenience referencing and dereferencing
    - A method with pointer rec. can be used on a value
    - A method with value rec. can be used on a pointer

code: go

    func (v *Vertex) Scale(f float64) {
        v.X = v.X * f
        v.Y = v.Y * f
    }

    func main() {
        v := Vertex{3, 4}
        v.Scale(10)
        fmt.Println(v.Abs())
    }

---

title: Methods vs. functions

code: go

    func Abs(v Vertex) float64 {
        return math.Sqrt(v.X*v.X + v.Y*v.Y)
    }

    func Scale(v *Vertex, f float64) {
        v.X = v.X * f
        v.Y = v.Y * f
    }

    func main() {
        v := Vertex{3, 4}
        Scale(&v, 10)
        fmt.Println(Abs(v))
    }

---

title: Value or pointer receiver?

- There are two reasons to use a pointer receiver
    - Modify the value that its receiver points to
    - Avoid copying the value on each method call, for efficiency
- In general, all methods on a given type should have *either* value or pointer receivers
    - But **not a mixture** of both
    - Problems with *interfaces*...
- For `Vertex`, both `Abs` and `Scale` should use a pointer receiver!

---

title: Vertex, the way to go

code: go

    type Vertex struct {
        X, Y float64
    }

    func (v *Vertex) Abs() float64 {
        return math.Sqrt(v.X*v.X + v.Y*v.Y)
    }

    func (v *Vertex) Scale(f float64) {
        v.X = v.X * f
        v.Y = v.Y * f
    }

---

title: Interfaces

- A set of method signatures
    - A value of interface type can hold any value...
    - that implements all those methods
- A type implements an interface by implementing its methods
    - No explicit declaration, no `implements` keyword
    - Definition of an interface decoupled from its implementation
    - Different packages, no pre-arrangement
- Under the covers, interface value ~ tuple: `(value, type)`
    - Method of an interface value → method of its underlying type
    - Interface value holding a `nil`: itself is non-nil; its methods are callable

---

title: Abser

code: go

    type Abser interface {
        Abs() float64
    }

    func main() {
        var a Abser
        v := Vertex{3, 4}

        a = &v // a *Vertex implements Abser
        // a = v // error! Vertex is not Abser; *Vertex is

        fmt.Println(a.Abs())
    }

---

title: Another abser

code: go

    type MyFloat float64

    func (f MyFloat) Abs() float64 {
        if f < 0 {
            return float64(-f)
        }
        return float64(f)
    }

    func main() {
        var a Abser
        f := MyFloat(-math.Sqrt2)

        a = f  // a MyFloat implements Abser

        fmt.Println(a.Abs())
    }

---

title: Dogs and pigs

code: go

    type Dog struct {
        Name string
    }

    type Pig struct {
        Name string
    }

    func (d *Dog) Say() {
        fmt.Println("I'm " + d.Name + " and I say: WOOF!")
    }

    func (p *Pig) Say() {
        fmt.Println("I'm " + p.Name + " and I say: OINK!")
    }

---

title: Animals

code: go

    type Animal interface {
        Say()
    }

    func main() {
        // a1 Animal := Pig{"George"} // error, a pointer is needed

        animals := []Animal{ &Pig{"Peppa"}, &Dog{"Danny"} }
        for _, a := range animals {
            a.Say()
        }
    }

---

title: The empty interface

- The interface type that specifies zero methods is known as the empty interface

code: go

    interface{}

- An empty interface may hold values of any type
    - Every type implements at least zero methods
- Empty interfaces are used by code that handles values of *unknown type*
    - For example, `fmt.Print` takes any number of arguments of type `interface{}`

---

title: Type assertions

code: go

    var i interface{} = "hello"

    s := i.(string)
    fmt.Println(s)

    s, ok := i.(string)
    fmt.Println(s, ok)

    f, ok := i.(float64)
    fmt.Println(f, ok)

    //f = i.(float64) // panic
    fmt.Println(f)
    
---

title: Type switches

code: go

    func do(i interface{}) {
	    switch v := i.(type) {
	    case int:
		    fmt.Printf("Twice %v is %v\n", v, v*2)
	    case string:
		    fmt.Printf("%q is %v bytes long\n", v, len(v))
	    default:
		    fmt.Printf("I don't know about type %T!\n", v)
	    }
    }

    func main() {
	    do(21)
	    do("hello")
	    do(true)
    }

---

title: Basic interfaces

code: go

    type Stringer interface {
        String() string
    }

    type error interface {
        Error() string
    }

    type Reader interface {
            Read(p []byte) (n int, err error)
    }

---

title: Concurrency
class: segue dark

---

title: Goroutines

- A lightweight thread managed by the Go runtime
- Params are evaluated locally
- Access to shared memory must be synchronized (`sync` package)

code: go

    func say(s string) {
	    for i := 0; i < 5; i++ {
		    time.Sleep(100 * time.Millisecond)
		    fmt.Println(s)
	    }
    }

    func main() {
	    go say("world")
	    say("hello")
    }

---

title: Channels

- A typed conduit, to send and receive values
- Channel operator, `<-`

code: go

    func sum(s []int, c chan int) {
	    sum := 0
	    for _, v := range s {
		    sum += v
	    }
	    c <- sum             // (blocking) send sum to c
    }
    func main() {
	    s := []int{7, 2, 8, -9, 4, 0}
	    c := make(chan int)  // use `make` to create a channel
	    go sum(s[:len(s)/2], c)
	    go sum(s[len(s)/2:], c)
	    x, y := <-c, <-c     // (blocking) receive from c
	    fmt.Println(x, y, x+y)
    }

---

title: Using channels

- By default, sends and receives block until the other side is ready
- Channels can be buffered
    - `ch := make(chan int, 100) // buffer for 100 ints`
    - Sends to a buffered channel block only when the buffer is full
    - Receives block when the buffer is empty
- A sender can close a channel: no more values
    - `close(c)`
- A receiver can test whether a channel has been closed
    - `v, ok := <-ch`

---

title: Select

- Statement to wait on multiple communication operations
    - `default`, if no other case is ready

code: go

    func fibonacci(c, quit chan int) {
	    x, y := 0, 1
	    for {
		    select {
		    case c <- x:
			    x, y = y, x+y
		    case <-quit:
			    fmt.Println("quit")
			    return
		    }
	    }
    }

---

title: Operating two channels

code: go

    func main() {
	    c := make(chan int)
	    quit := make(chan int)
	    go func() {
		    for i := 0; i < 10; i++ {
			    fmt.Println(<-c)
		    }
		    quit <- 0
	    }()
	    fibonacci(c, quit)
    }


