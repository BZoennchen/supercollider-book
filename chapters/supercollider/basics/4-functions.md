(sec-functions)=
# Functions

In ``sclang``, functions are first-class objects, meaning a function can be an argument of another function.
The language drives the programmer to use this fact in various ways.

## Definition

To define a function, we encapsulate its content by curly brackets.
To execute it, we call ``value`` on it:

```isc
(
~func = {
  var x = 10;
  x;
};
~func.value();   // returns 10
)
```

We can omit ``value`` to call a function:

```isc
~func.();   // returns 10
```

This looks a little bit weird, but it works just fine.

In ``sclang`` there is no ``return`` keyword.
We only have to call ``func.value`` for functions and not for methods of an object or class.
A function always returns the content of the last evaluated statement, in this case, ``x``.
In my personal opinion, an additional keyword can make the code more readable.

To see what I mean by making use of functions as first-class objects, we can look at the [control structures](https://doc.sccode.org/Reference/Control-Structures.html).
``if`` is in fact, a function that takes three arguments:

1. the condition
2. a function that is executed if the condition is ``true``
3. a function that is executed if the condition is ``false``
   
Compare the following code that returns ``10`` if the argument of ``func`` is ``10`` and a random integer between 0 and 19 (20 excluded).

```isc
(
var func = {
    arg input;
    if(input == 10, {
        input;
    }, {
        rand(20);
    });
};
func.(11).postln;
func.(11).postln;
func.(11).postln;
)
```

It is important to understand, that the function ``{rand(20);}`` is evaluated each time we call ``func.value(11);``.
Again, we can either write ``rand(20);`` or ``20.rand;``.

## Closures

If we want the ``func`` to return the same randomly chosen value each time it is called, we can use a [Closure](https://en.wikipedia.org/wiki/Closure_(computer_programming))
In short, a [Closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) is a function combined with a set of variables that are neither defined within the function nor are arguments of the functions.

```isc
(
var r = rand(20);
var func = {
    arg input;
    if(input == 10, {
        input;
    }, {
        r;
    });
};
func.(11).postln;
func.(11).postln;
func.(11).postln;
)
```

Of course, we can do the same without using a [Closure](https://en.wikipedia.org/wiki/Closure_(computer_programming))

```isc
(
var val = rand(20);
var func = {
    arg input, r;
    if(input == 10, {
        input;
    }, {
        r;
    });
};
func.(11, val).postln;
func.(11, val).postln;
func.(11, val).postln;
)
```

but since functions are first-class objects it is often convenient to use a [Closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)).

## Arguments

Let's look at another example:

```isc
(
var add = {
    arg a = 5, b;
    a + b;
};
add.(a: 6, b: 11) // returns 17
add.(b: 11) // returns 16
)
```

Similar to ``Python``, one can define a default value for each argument, and we can ignore the order if we add the names.
To define a specific argument in the function call, we have to use ``:`` instead of ``=``.
Furthermore, there is another rather strange shortcut:

```isc
(
var add = {|a = 5, b|
    a + b;
};
add.(b: 11) // returns 16
)
```

## Compositions

In ``sclang`` the mathematical operation of composing functions, i.e., $f \circ g$ is approxiated by the ``<>`` operator.

```isc
f = {arg x; x*x};
g = {arg x; 2*x};

f.(5); // 25
g.(5); // 10

h = f <> g;
h.(5); // f(g(5)) = (2*5)^2 = 10 * 10 = 100
```