(sec-array)=
# Arrays

A signal is a sequence of numbers.
An array can realize this sequence.
Therefore, it is no surprise that ``sclang`` offers a rich interface to create, manipulate and combine arrays.
Thinking about multidimensional arrays can be both mind bending and mind expanding.

## Creation

To create a new ``Array`` the class offers many factory methods.

```isc
a = Array.new(maxSize: 3); // [  ]
a = Array.interpolation(3, 0, 1) // [ 0.0, 0.5, 1.0 ]
a = [1, 2, 3] // [1, 2, 3]
a = (1..5) //  [1, 2, 3, 4, 5]
a = Array.fill(5, {arg i; i*i}) // [ 0, 1, 4, 9, 16 ]
a = Array.with(1, 2, 'abc', 1.2) // [ 1, 2, abc, 1.2 ]
a = Array.series(size: 4, start: 1, step: 5); // [ 1, 6, 11, 16 ]
a = Array.geom(size: 4, start: 1, grow: 5); // [ 1, 5, 25, 125 ]
```

There are also factory methods to create two-

```isc
(
var rows = 3;
var cols = 4;

// [ [ 0, 1, 2, 3 ], [ 0, 2, 4, 6 ], [ 0, 3, 6, 9 ] ]
a = Array.fill2D(rows, cols, {arg r, c; r*c+c});
)

// [ [ 1, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ] ]
Array.fill2D(3, 3, {arg r, c; if(r == c, {1}, {0})});
```

and even n-dimensional arrays.

```isc
// [ [ [ 0, 0, 0, 0 ], [ 0, 1, 2, 3 ], [ 0, 2, 4, 6 ], [ 0, 3, 6, 9 ] ], 
//   [ [ 0, 1, 2, 3 ], [ 0, 2, 4, 6 ], [ 0, 3, 6, 9 ], [ 0, 4, 8, 12 ] ], 
//   [ [ 0, 2, 4, 6 ], [ 0, 3, 6, 9 ], [ 0, 4, 8, 12 ], [ 0, 5, 10, 15 ] ], 
//   [ [ 0, 3, 6, 9 ], [ 0, 4, 8, 12 ], [ 0, 5, 10, 15 ], [ 0, 6, 12, 18 ] ] ]

Array.fillND([4, 4, 4], { arg a, b, c; a+b*c; }); 
```

## Concatenation

First, we can concatenate two arrays without changing any of the two originals:

```isc
[1,2,3] ++ [4,5,6] // [ 1, 2, 3, 4, 5, 6 ]
```

We can also add all elements from one array to the other:

```isc
a = [1,2,3];
a.addAll([4,5,6]); // [ 1, 2, 3, 4, 5, 6 ]
```

## Access of Elements

We can access any element by ``.at(index)`` or by the shorthand ``@index``:

```isc
(
a = [1, 2, 3, 4];
a.at(2); // 3
)
```

Instead of ``at``, we can use the ``a@2;`` as shorthand. 
Similar to ``numpy`` arrays, can also index multiple entries at once:

```isc
(
a = [1, 2, 3, 4];
a.at([2, 3]); // [3, 4]
)
```

Similar to ``Python`` we can slice an array:

```isc
(
a = [1, 2, 3, 4];
a.at([2, 3]); // [3, 4]
)
```

Instead of using ``.at`` we can also use brackets:

```isc
(
a[[2, 3]]; // [3, 4]
a[0]; // 1
)
```

In signal processing, we want to manipulate elements of such a sequence.
Therefore, an ``Array`` in ``sclang`` is implemented accordingly.

## Manipulation

To **set** a specific value we can use the default syntax well-known for almost all existing programming languages:

```
(
a = [2, 4, 5, 6];
a[0] = -10;
a; // [-10, 4, 5, 6];
)
```

**Multiplying** an array with a number, will result in a new array for which each element is multiplied by the number.

```isc
(
a = [2, 4, 5, 6];
b = a * 2;
a.postln;
b.postln;
)
```

Note that ``a`` has not changed.
**Multiplying two arrays** ``a * b`` will result in a new array where the ``i``-th element equals ``a[i] * b[i%a.size]``.

```isc
(
a = [2, 4, 5, 6];
b = [2, 3];
a * b; // [ 4, 12, 10, 18 ]
)
```

**Division** works the same way:

```isc
(
a = [2, 4, 5, 6];
b = [2, 3];
a / b; // [ 1.0, 1.3333333333333, 2.5, 2.0 ]
)
```

We can **duplicate** an array ``k`` times by using ``!k``:

```isc
5!2!3 // [ [ 5, 5 ], [ 5, 5 ], [ 5, 5 ] ]
```

(sec-array-adverbs)=
## Adverbs

``J`` and ``APL`` are programming languages that are made for processing arrays of data and are able to express complex notions of iterations implicitely.
``J`` is a purely functional programming language that was developed around 1990 and is based on ``APL`` (**A** **P**rogramming **L**anguage).
Since ``J`` specializes in array (and matrix) operations, it is especially useful to solve mathematical and statistical problems.
``J`` is capable of the MIMD (multiple instruction, multiple data) paradigm.

In ``Python``, we realise such operations using ``numpy`` arrays.

``sclang`` borrows some of the concepts of ``J``.
One of them is the *adverbs*-concept.
Adverbs are a third argument passed to binary operations that modifies how they iterate over sequencable collections or streams.

When we normally add two arrays we add componentwise wrapping around if the arrays do not have the same number of elements.

```isc
[1, 2, 3, 4] + [10, 20, 30] // gives [11, 22, 33, 14]
```

Using adverbs can change this behaviour.
Adverbs are symbols and they follow a ``.`` (dot) after the binary operator.
Adverbs can be applied to **all** binary operators.

The **short adverb** ``s`` avoids the wrapping and returns an array that has only as many elements as the shorter one.

```isc
[1, 2, 3, 4] +.s [10, 30] // gives [11, 32]
```

This also works for multiplication.

```isc
[1, 2, 3, 4] *.s [10, 30] // gives [10, 60]
```

The **fold adverb** ``f`` uses folded indexing instead of wrapped.

```isc
[1, 2, 3, 4, 5, 6] +.f [10, 20, 30] // gives [ 11, 22, 33, 24, 15, 26 ]
```

The **table adverb** ``t`` makes an array of arrays where each item in the first array is added to the whle second array and the resulting arrays are collected.

```isc
[10, 20, 30, 40, 50] +.t [1, 2, 3]
// gives [[11, 12, 13],[21, 22, 23],[31, 32, 33],[41, 42, 43],[51, 52, 53]]
```

The **flat table adverb** ``x`` is like table, except that the result is a flat array.

```isc
[10, 20, 30, 40, 50] +.x [1, 2, 3]
// gives [11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53]
```

This adverb is also defined for [Streams](sec-stream).

```isc
p = (Pseq([10, 20]) +.x Pseq([1, 2, 3])).asStream;
Array.fill(7, { p.next });
```

gives

```isc
[ 11, 12, 13, 21, 22, 23, nil ]
```