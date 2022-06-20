(sec-array)=
# Arrays

A signal is a sequence of numbers.
An array can realize this sequence.
Therefore, it is no surprise that ``sclang`` offers a rich interface to create, manipulate and combine arrays.

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

In signal processing, we want to manipulate elements of such a sequence.
Therefore, an ``Array`` in ``sclang`` is implemented accordingly.

## Manipulation

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