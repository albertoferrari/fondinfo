title: C++ internals
subtitle: Object oriented programming in C++
figure: images/misc/cpp-logo.jpg

---

title: Hidden this pointer

code: C++

    class Accumulator {
    private:
        int value = 0;
    public:
        add(int inc) {
            value += inc;
        }
        get_val() { return y; }
    };

code: C++

    int main() {
        Accumulator a;
        a.add(10);
        cout << a.get_val() << endl;
    }

---

title: Hidden this, exposed

- When we call `a.add(10)`, compiler actually calls stg. like `Accumulator__add(&a, 10)`
    - Real name mangling is more complicated and proprietary
- Inside `add` f., the `this` pointer holds the address of object `a`
    - Any member variables inside `add` f. are prefixed with `this->`
    - So when we say `value += inc`, compiler actually executes `this->value += inc`

---

title: C++ class layout
figure: images/oop/cpp-struct-layout-a.png

- C-like structs
    - C++mostly upwards-compatible with C
    - Same simple struct layout rules
    - Members laid out in their declaration order
    - Implementation defined alignment padding
- *Note*: C++ structs are like classes, defaulting to `public`
    
code: C++

    struct A {  // or class
        char c;
        int i;
    };

---

title: More members
figure: images/oop/cpp-struct-layout-b.png

code: C++

    struct B {  // or class
    public:
        int bm1;
    protected:
        int bm2;
    private:
        int bm3;
        static int bsm;
        void bf();
        static void bsf();
        typedef void* bpv;
        struct N { };
    };

- Only the *non-static data members* occupy space in each instance

---

title: Single inheritance

code: C++

    struct C {
        int c1;
        void cf();
    };
    
    struct D : C {
        int d1;
        void df();
    };

- Derived class inherits all features of base class
- Each instance of `D` must contain a complete copy of the instance data of `C`

---

title: Upcast for single inheritance
figure: images/oop/cpp-struct-layout-c.png images/oop/cpp-struct-layout-d.png

code: C++

    struct C {
        int c1;
        void cf();
    };
    struct D : C {
        int d1;
        void df();
    };

- New instance data of `D` is simply *appended* to layout of `C`
    - Layout used by *all* known C++ *implementations*
    - Address of `C` object within `D` == first byte of `D` object
    - No displacement for *upcasting*, to obtain address of embedded `C`
    
---

title: Multiple inheritance

- Model for an organization that has:
    - A class `Manager` (who delegates), and
    - A class `Worker` (who actually does the work)
- How can we model a class `MiddleManager`?
    - Like a `Worker`, accepts work assignments from manager
    - Like a `Manager`, delegates work to employees

code: C++

    struct Manager ... { ... };
    struct Worker ... { ... };
    struct MiddleManager : Manager, Worker { ... };

---

title: Multiple inheritance layout
figure: images/oop/cpp-struct-layout-e.png images/oop/cpp-struct-layout-f.png

code: C++

    struct E {
        int e1;
        void ef();
    };
    struct F : C, E {
        int f1;
        void ff();
    };

- Struct `F` multiply inherits from `C` and `E`
- As with single inheritance, `F` contains a copy of instance data of each base class
- Here, address of embedded `E` within `F` ≠ address of `F` itself
- Displacement leads to a small overhead, for casting

---

title: Diamond problem
figure: images/oop/diamond-inheritance.svg

- What if both `Manager` and `Worker` are derived from `Employee`?

code: C++

    struct Employee { ... };
    struct Manager : Employee { ... };
    struct Worker : Employee { ... };
    struct MiddleManager : Manager, Worker { ... };

- They each contain a copy of `Employee` instance data
- `MiddleManager` will contain two instances of `Employee`, one from each base
- Duplication = storage overhead, inconsistencies

---

title: Virtual inheritance

In C++, this “sharing inheritance” is (unfortunately) called *virtual inheritance*

code: C++

    struct Employee { ... };
    struct Manager : virtual Employee { ... };
    struct Worker : virtual Employee { ... };
    struct MiddleManager : Manager, Worker { ... };

- More expensive to implement and use
- No fixed displacement from the address point of the derived class to its virtual base
- If derived class is further derived from, shared base placed at different offset

---

title: Virtual base table pointer
figure: images/oop/cpp-struct-layout-g.png images/oop/cpp-struct-layout-h.png images/oop/cpp-struct-layout-i.png
class: large-figure

code: C++

    struct G : virtual C {
        int g1; void gf();
    };
    struct H : virtual C {
        int h1; void hf();
    };
    struct I : G, H {
        int i1; void _if();
    };

- *Visual C++*: hidden `vbptr`
    - Pointer to a (*per-class*) table of displacements
    - From address of `vbptr`, to virtual base(s)
    - 32-bit platform: `GdGvbptrC` is `8`, `IdGvbptrC` is `20` (bytes)

---

title: Data member access

- No inheritance, like C lang

code: C++

    C* pc;
    pc->c1; // *(pc + dCc1);
   
- Single inheritance, displacement is `0`

code: C++

    D* pd;
    pd->c1; // *(pd + dDC + dCc1); // *(pd + dDCc1);
    pd->d1; // *(pd + dDd1);

- Multiple inheritance, constant displacement to a given base

code: C++

    F* pf;
    pf->c1; // *(pf + dFC + dCc1); // *(pf + dFc1);
    pf->e1; // *(pf + dFE + dEe1); // *(pf + dFe1);
    pf->f1; // *(pf + dFf1);
 
---

title: Access to virtual base

- Virtual inheritance, access to virtual base is comparatively expensive
    - Fetch the vbptr
    - Fetch a vbtable entry
    - Add that displacement to vbptr address
- For other members, it's just a displacement

code: C++

    I* pi;
    pi->c1; // *(pi + dIGvbptr + (*(pi+dIGvbptr))[1] + dCc1);
    pi->g1; // *(pi + dIG + dGg1); // *(pi + dIg1);
    pi->h1; // *(pi + dIH + dHh1); // *(pi + dIh1);
    pi->i1; // *(pi + dIi1);
    I i;
    i.c1; // *(&i + IdIC + dCc1); // *(&i + IdIc1);

---

title: Casts

- Inexpensive to cast pointers, in case of derived classes
    - Add or subtract displacement (often 0).
    - Except for classes with virtual bases

code: C++

    F* pf;
    (C*)pf;  // (C*)(pf ? pf + dFC : 0); // (C*)pf;
    (E*)pf;  // (E*)(pf ? pf + dFE : 0);

---

title: Cast with virtual base

- Casting over a virtual inheritance path is relatively expensive
- About the same cost as accessing a member of a virtual base:

code: C++

    I* pi;
    (G*)pi;  // (G*)pi;
    (H*)pi;  // (H*)(pi ? pi + dIH : 0);
    (C*)pi;  // (C*)(pi ? (pi+dIGvbptr + (*(pi+dIGvbptr))[1]) : 0);

---

title: Member functions
figure: images/oop/cpp-struct-layout-p.png
class: large-figure

- Virtual member functions incur an instance size hit
- They require a pointer to a (*per-class*) **virtual function table**

code: C++

    struct P {
        int p1;
        void pf();           // new
        virtual void pvf();  // new
    };
    
---

title: The hidden this

- Each (non-static) member function of a class `X` receives a special hidden `this` parameter of type `X* const`
- Implicitly initialized from the object the member function is applied to
- Within the body of a member function, member access off the `this` pointer is implicit

code: C++

    void P::pf() {  // void P::pf([P *const this])
        ++p1;       // ++(this->p1);
    }

---

title: Overriding member functions
figure: images/oop/cpp-struct-layout-q.png
class: large-figure

- A derived class can override, or replace, an hinerited function definition
- Type of override depends upon whether the member function is declared `virtual`
    - Static override: determined at compile time
    - Dynamic override: determined at run-time, by concrete object addressed by object pointer

code: C++

    struct Q : P {
        int q1;
        void pf();           // overrides P::pf
        void qf();           // new
        void pvf();          // overrides P::pvf
        virtual void qvf();  // new
    };
    
---

title: Non-virtual override

code: C++

    P p; P* pp = &p; Q q; P* ppq = &q; Q* pq = &q;
    pp->pf();   // pp->P::pf();   // P::pf(pp);
    ppq->pf();  // ppq->P::pf();  // P::pf(ppq);
    pq->pf();   // pq->Q::pf();   // Q::qf(pq);
    pq->qf();   // pq->Q::qf();   // Q::pf((P*)pq);

- For non-virtual function calls, member function to call is statically determined, at compile time
- By type of pointer expression at left of `->` operator
- `ppq` points to a `Q`, but `ppq->pf()` calls `P::pf()`
- Pointer expression at left of `->` passed as hidden `this` parameter

---

title: Virtual override

code: C++

    pp->pvf(); // pp->P::pvf(); // P::pvf(pp);
    ppq->pvf(); // ppq->Q::pvf(); // Q::pvf((Q*)ppq);
    pq->pvf(); // pq->Q::pvf(); // Q::pvf((P*)pq);

- For virtual function calls, member function to call is determined at run-time
- Appropriate to actual instance addressed by pointer
- `ppq` has type `P*`, but it addresses a `Q`, and so `Q::pvf()` is called

---

title: Multiple inheritance of virtual f.s
figure: images/oop/cpp-struct-layout-r.png images/oop/cpp-struct-layout-s.png
class: large-figure

code: C++

    struct R {
        int r1;
        virtual void pvf(); // new
        virtual void rvf(); // new
    };
    struct S : P, R {
        int s1;
        void pvf(); // overrides P::pvf and R::pvf
        void rvf(); // overrides R::rvf
        void svf(); // new
    };

- More than one `vfptr` if class inherits them from multiple bases, each with virtual functions
- `S::pvf()` overrides both `P::pvf()` and `R::pvf()`
- `S::rvf()` overrides `R::rvf()`

---

title: Semantics of virtual calls

code: C++

    S s; S* ps = &s;
    ((P*)ps)->pvf();  // ((P*)ps)->P::vfptr[0])((S*)(P*)ps)
    ((R*)ps)->pvf();  // ((R*)ps)->R::vfptr[0])((S*)(R*)ps)
    ps->pvf();        // one of the above; calls S::pvf()

- Base `R` has a different address point than do `P` and `S`, as expected with multiple inheritance
- `S::pvf()` an `S*` as `this` parameter
- Automatically convert `R*` at call site into `S*` at callee
- In `vftable`, `pvf` slot points to an adjuster *thunk*




