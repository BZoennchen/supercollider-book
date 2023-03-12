# Reference

There are many different ``Pattern``, I will only discuss some of them which I find most important.
In fact, the official [documentation of SuperCollider](https://doc.sccode.org/) is not always super helpful but the tutorial [Understanding Streams, Patterns and Events](https://doc.sccode.org/Tutorials/Streams-Patterns-Events1.html) is an excellent source to get started.

## Primary Pattern

### Listen

[Pseq](https://doc.sccode.org/Classes/Pseq.html) is the most basic pattern that can be used to play through a list of values.

```isc
// [ 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2 ]
Pseq(list: [1,2,3,4], repeats: 3, offset: 2).asStream.all;
```

[Prand](https://doc.sccode.org/Classes/Prand.html) chooses items from the list randomly (same as list.choose).

```isc
// e.g. [ 4, 3, 4, 3, 3, 2, 1, 3, 2, 4 ]
Prand(list: [1,2,3,4], repeats: 10).asStream.all;
```

[Pxrand](https://doc.sccode.org/Classes/Pxrand.html) chooses randomly, but never repeat the same item twice.

```isc
// e.g. [ 2, 1, 2, 4, 3, 1, 4, 1, 2, 4 ]
Pxrand(list: [1,2,3,4], repeats: 10).asStream.all;
```

[Pshuf](https://doc.sccode.org/Classes/Pshuf.html) shuffles the list in random order, and use the same random order 'repeats' times.

```isc
// e.g. [ 3, 1, 4, 2, 3, 1, 4, 2, 3, 1, 4, 2 ]
Pshuf(list: [1,2,3,4], repeats: 3).asStream.all;
```

[Pwrand](https://doc.sccode.org/Classes/Pwrand.html) choose randomly by weighted probabilities (like list.wchoose(weights)).

```isc
// e.g. [ 1, 2, 1, 2, 2, 2, 1, 2, 2, 2 ]
Pwrand(list: [1,2,3,4], weights: [20, 30,1, 5].normalizeSum, repeats: 10).asStream.all;
```

### Series

[Pseries](https://doc.sccode.org/Classes/Pseries.html) generates numbers according to the arithmetic series (addition).

```isc
// [ 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1 ]
Pseries(start: 1, step: -0.1, length: 10).asStream.all;
```

[Pgeom](https://doc.sccode.org/Classes/Pgeom.html) generates numbers according to the geometric series (multiplication).

```isc
// [ 1, 0.5, 0.25, 0.125, 0.0625 ]
Pgeom(start: 1, grow: 0.5, length: 5).asStream.all;
```

### Distributions

[Pwhite](https://doc.sccode.org/Classes/Pwhite.html) generates random numbers, equal/uniform distribution (*white noise*), like ``rrand(lo, hi)``.

```isc
// e.g. [ 0.55498147010803, 1.88440990448, 1.8215901851654, 1.8560950756073 ]
Pwhite(lo: 0, hi: 2.0, length: 4).asStream.all;
```

[Pexprand](https://doc.sccode.org/Classes/Pexprand.html) generates random numbers, exponential distribution, like ``exprand(lo, hi)``.
Zero can not be in the interval!

```isc
// e.g. [ 0.35829930578573, 1.0719818402671, 1.0689460460456, 0.12406136454322 ]
Pexprand(lo: 0.1, hi: 2.0, length: 4).asStream.all;
```

[Pbrown](https://doc.sccode.org/Classes/Pbrown.html) generates numbers according to the Brownian motion, arithmetic scale (addition).
The ``step`` argument determines the maximum change per step.
Internal the pattern uses ``xrand2`` to determine the next step change, i.e., a uniform distribution fron ``-step`` to ``+step``.

```isc
// e.g. [ 0.044661736488342, 0.12499458789825, 0.20763206481934, 0.30759530067444 ]
Pbrown(lo: 0, hi: 5, step: 0.1, length: 4).asStream.all;
```

### Functions

[Pfunc](https://doc.sccode.org/Classes/Pfunc.html) gets the stream values from a user-supplied function.

```isc
// e.g. [ 3, 1, 3, 0, 0 ]
Pfunc(nextFunc: {4.rand}).asStream.nextN(5)
```

[Pfuncn](https://doc.sccode.org/Classes/Pfunc.html) gets values from the function, but stop after ``repeats`` items.

```isc
// e.g. [ 3, 3, 2, 1, 0, 0, 0 ]
Pfuncn(func: {4.rand}, repeats: 7).asStream.all;
```


[Prout](https://doc.sccode.org/Classes/Prout.html) uses the function like a routine.
The function should return values using ``.yield`` or ``.embedInStream``.
The folling code constructs a pattern that spits out the first 10 Fibonacci numbers.

```isc
// [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ]
(
Prout(routineFunc: {
    var fib0 = 0, fib1 = 1, tmp = 0;
    10.do{
        fib0.yield;
        tmp = fib0;
        fib0 = fib1;
        fib1 = tmp + fib1;
    }
}).asStream.all;
)
```

## Secondary Pattern

[Pser](https://doc.sccode.org/Classes/Pser.html) similar to [Pseq](https://doc.sccode.org/Classes/Pser.html) it plays through a list but the number of resulting times is defined by the second argument ``repeats``.

```isc
// [ 1, 2, 3 ]
Pser(list: [1,2,3,4], repeats: 3, offset: 0).asStream.all;
```

[Pslide](https://doc.sccode.org/Classes/Pslide.html) plays overlapping segments from the list.

```isc
// [ 2, 3, 4, 5, 4, 5, 6, 1, 6, 1, 2, 3 ]
(
Pslide(
    list: [1,2,3,4,5,6], 
    repeats: 3, 
    len: 4, 
    step: 2, 
    start: 1, 
    wrapAtEnd: true).asStream.all;
)
```

[Pwalk](https://doc.sccode.org/Classes/Pwalk.html) realizes a *random walk* over the list.
The direction and the steps of the walk can be controled by patterns.

```isc
// [ 1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 1, 2, 3, 4 ]
(
Pwalk(
    list: [1,2,3,4,5], 
    stepPattern: Pseq([1,1,-1,1,1,-1], inf), 
    directionPattern: 1, 
    startPos: 0).asStream.nextN(15);
)
```

[Place](https://doc.sccode.org/Classes/Place.html) interlaces any arrays found in the main list.
Basically this pattern returns elements in the list. 
But if an element is an array itself, it embeds the first element when it comes by first time, the second element when it comes by the second time and so on.
The $n$-th when it comes by the $n$-th time.
This can be very useful when we build a melodies.

```isc
// [ 1, 2, 5, 1, 3, 6 ]
Place(list: [1,[2,3,4],[5,6]], repeats: 2, offset: 0).asStream.all;
```

[Ppatlace](https://doc.sccode.org/Classes/Ppatlace.html) similar to [Place](https://doc.sccode.org/Classes/Pser.html) but for patterns.
Compare the following differences:

```isc
// [ 1, 2, 5, 6, 1, 3, 5, 6 ]
Place(list: [1,[2,3,4],Pseq([5,6])], repeats: 2, offset: 0).asStream.all;

// [ 1, [ 2, 3, 4 ], 5, 1, [ 2, 3, 4 ], 6 ]
Ppatlace(list: [1,[2,3,4],Pseq([5,6])], repeats: 2, offset: 0).asStream.all;

// [ 1, 2, 5, 1, 3, 6 ]
Ppatlace(list: [1,Pseq([2,3,4]),Pseq([5,6])], repeats: 2, offset: 0).asStream.all;
```

[Ptuple](https://doc.sccode.org/Classes/Pwalk.html) collects the list items into an array as the return value.
The ``list`` argument has to be an array of pattern.

```isc
// [ [ 1, 10, 4 ], [ 2, 11, 5 ], [ 1, 10, 4 ], [ 2, 11, 5 ] ]
(
Ptuple(list: 
    [
        Pseq([1,2,3]), 
        Pseq([10,11,12]), 
        Pseq([4,5,nil])
    ], 
    repeats: 2).asStream.all;
)
```