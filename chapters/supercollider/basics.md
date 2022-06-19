(sec-basics)=
# Basics

In this section, I will give a starting point so the reader can start experimenting with SuperCollider.
Before you move on, you should understand the content of this whole chapter -- it lies the ground for further discussions.
At the same time, I assume that the reader has some experience in some other programming language.
If this is not the case, you can still enjoy the text but might also have to look into secondary materials.

By only reading [The Ecosystem](sec-ecosystem) and this section, you have an excellent basis to start your discovery with the SuperCollider platform.
Together, these two chapters act as a quick start.

Before we go into the details, I must warn you: coming from programming languages such as ``Java``, ``C`` and ``Python``, the syntax of ``sclang`` is not the most beautiful.
However, this first expression hides the fact that many decisions regarding syntax make sense at a second glance.
So don't be scared by the first impression.

## Code Execution

The [SuperCollider IDE](sec-scide) is build for interaction.
If you are familiar with the concept of notebooks, for example, Jupyter notebooks or Mathematica notebooks, you already know what I mean.
The idea is that you can execute code while developing.
Instead of writing a complete program, you are constantly stimulated to run small code snippets.
In live coding, this is embraced even more, but it is also good practice if you learn and explore SuperCollider in general.

SuperCollider initializes an [Environment](https://doc.sccode.org/Classes/Environment.html), i.e., a collection of things that can be accessed via name.
Interacting with the IDE will manipulate this environment on the fly.

### Triggering the Evaluation

Let's start!
Let's write some ``sclang`` code and execute it via the REPL (Read–Eval–Print Loop).
To execute the following line, press ``SHIFT`` + ``RETURN`` while your cursor is at the code line.

```isc
"Hello World!".postln;
```

Since SuperCollider does not use code cells, we have to define blocks of codes ourselves.
To execute multiple lines, we have to enclose the code in brackets ``(``, ``)`` and evaluate the code using ``CMD`` + ``RETURN`` on Mac and ``CTRL`` + ``RETURN`` on Windows.

```{admonition} Code Execution 
:name: remark-code-execution
:class: remark
Use ``SHIFT`` + ``RETURN`` to evaluate a single line of code and use ``CMD`` + ``RETURN`` to evaluate a code block.
```

For example:

```isc
(
"Hello World!".postln;
"We make some music".postln;
)
```

In both cases, you will notice that the last line is printed twice in the post windows.
SC always prints the last statement on the post window.

Like any other object-oriented language, we call a **method** ``postln`` on the **object** representing a ``String``.
However, they use different terms in the [SuperCollider documentation](https://doc.sccode.org/).
The object is the **receiver** of a **message** (method).

The object is always the method's first argument (similar to ``Python``).
We refer to this object as ``this``.
For example, we could also use the following syntax:

```isc
postln("Hello World!");
```

A very useful key combination is ``CMD`` + ``d``.
It will open the documentation of the code your cursor is at.

```{admonition} Lookup Documentation
:name: remark-lookup-documentation
:class: remark
Use ``CMD`` + ``d`` to look at the documentation of the class or method your cursor is at.
```

### Execution of C++ Code

Let us reverse engineer what happens if we print out a string to the post window.

```{admonition} Lookup Source Code
:name: remark-lookup-source-code
:class: remark
Use ``CMD`` + ``i`` to look at the actual implementation of the class or method your cursor is at.
```

If we look into the source code of the ``postln`` method by using ``CMD`` + ``i`` and navigate to the class ``Object``, we can digest the following implementation:

```isc
postln { this.asString.postln; }
```

The curly brackets define a function with the name ``postln``.
As mentioned, ``this`` is either

1. the object the method is called on (if we use ``"Hello World!".postln;``) or
2. the first argument of the method (if we use ``postln("Hello World!");``)

By ``this.asString``, the object is transformed into a ``String`` and ``postln`` of the ``String`` is called.
Of course in our case the object is already a ``String`` and we directly call ``postln`` of ``String``!

Let's have a look at ``postln`` of the class ``String``:

```isc
postln {
    _PostLine
    ^this.primitiveFailed
}
```

This looks strange.
What is going on here?
Here we enter the ``C++`` code.
``_PostLine`` is a [primitive](https://doc.sccode.org/Guides/WritingPrimitives.html).
It is executed, and if nothing goes wrong, the code below (``^this.primitiveFailed``) is **not** executed.
In the ``C++`` file [PyrPrimitive.cpp](https://github.com/supercollider/supercollider/blob/18c4aad363c49f29e866f884f5ac5bd35969d828/lang/LangPrimSource/PyrPrimitive.cpp) we find the following code snippet:

```cpp
definePrimitive(base, index++, "_PostLine", prPostLine, 1, 0);
```

and ``prPostLine`` is a method:

```cpp
int prPostLine(struct VMGlobals* g, int numArgsPushed) {
    PyrSlot* a;

    a = g->sp;
    // if (NotObj(a)) return errWrongType;
    // assume it is a string!
    postText(slotRawString(a)->s, slotRawString(a)->size);
    postChar('\n');
    return errNone;
}
```

In the [documentation](https://doc.sccode.org/Guides/WritingPrimitives.html), we find the following explanation

>``g->sp`` is the top of the stack and is the last argument pushed. ``g->sp - inNumArgsPushed + 1`` is the **receiver** and where the result goes.

In our case, ``g->sp`` is the ``String`` object.
This interaction between ``sclang`` and ``C++`` reminds me of the interaction between ``Python`` and ``C++``.
As long as we do not write our own [primitives](https://doc.sccode.org/Guides/WritingPrimitives.html), we can ignore the ``C++`` interaction.

### Order of Execution

In ``sclang`` the code is strictly evaluated from left to right.
All operands have the same priority, which might lead to unexpected results.
The expression

```isc
4 + 4 * 5
```

returns ``(4 + 4) * 5 = 40`` instead of ``4 + (4 * 5) = 24``.

```{admonition} Order of Execution 
:name: attention-order-of-execution
:class: attention
``sclang`` uses a *strictly left to right order of execution*.
```

## Variables and Scope

Here we encounter the first inconvenience. 
In [(SC)](https://supercollider.github.io/), there are some special pre-defined variables. 
Each **single character variable** ``[a-z]`` is pre-defined and globally available.
They are called *interpreter variables* or *global variables*.

```{admonition} The Local Server Variable 
:name: attention-local-server-variable
:class: attention
By default, the variable ``s`` holds a reference to the local audio server.
```

If you come from a modern programming language, this is strange. 
However, it is often helpful for prototyping in [(SC)](https://supercollider.github.io/). 
``s`` is a very special *global variable* because it holds a reference to the default local server. 
Therefore, to start/boot the [audio server](sec-audio-sever), we evaluate:

```isc
s.boot;
```

No one stops you from overwriting ``s``, but I would not recommend it. 
As already mentioned, to define a code block, we use round brackets. 
We can use ``x`` before defining it because it is already defined for us.

```isc
(
x = 10;
x;
)
```

Evaluating

```isc
number = 10
```

results in an error because ``number`` is undefined. 
The code evaluation works similar to the cell evaluation in a ``Python`` Jupyter notebook, but variables (except for the single character) are *local*.
*Local* and *global variables* are not saved in the current *environment*.
You can print out this environment by just accessing it:

```isc
currentEnvironment;
```

The following code does not work without round brackets

```isc
var number = 10;
number;
```

because ``number`` is *locally* defined within the scope of a single line!
If we use brackets

```isc
(
var number = 10;
number;
)
```

``number`` is *local* within the brackets.
Note that we have to execute the whole block; otherwise ``number`` is still *local* within one line.

To define our own *global* variable, we have to use ``~`` in front of the variable name, for example:

```isc
~number = 10;
~number;
```

works just fine.
These variables are called *environment variables* and they are stored in ``currentEnvironment``.

We can also use single character *local* variables. The following code returns ``13``

```isc
x = 10;
(
x = x + 3;
x;
)
```

but the code below returns ``3``.

```isc
x = 10;
(
var x = 0;
x = x + 3;
x;
)
```

In summary, there are three types of variables:

1. (global) single character *interpreter variables*, e.g., ``x``, ``y`` 
2. (global) *environment variables*, e.g. ``~number``
3. (local) *local variables* ``var variable = 10;``

As their name indicates, variables can be reassigned, and due to the dynamic type system, we can give them any new value at any time.

````{admonition} Exponential Operator
:name: sc-exponential
:class: sc
Like ``Python``, ``sclang`` supports the exponential operator ``**``.

```isc
2**4 // 16.0
```
````

(sec-array)=
## Arrays

A signal is a sequence of numbers.
An array can realize this sequence.
Therefore, it is no surprise that ``sclang`` offers a rich interface to create, manipulate and combine arrays.

### Creation

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

### Concatenation

First, we can concatenate two arrays without changing any of the two originals:

```isc
[1,2,3] ++ [4,5,6] // [ 1, 2, 3, 4, 5, 6 ]
```

We can also add all elements from one array to the other:

```isc
a = [1,2,3];
a.addAll([4,5,6]); // [ 1, 2, 3, 4, 5, 6 ]
```

### Access of Elements

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

### Manipulation

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

## Functions

In ``sclang``, functions are first-class objects, meaning a function can be an argument of another function.
The language drives the programmer to use this fact in various ways.
To define a function, we encapsulate its content by curly brackets.
To execute it, we call ``value`` on it:

```isc
(
var func = {
  var x = 10;
  x;
};
func.value();   // returns 10
)
```

We can omit ``value`` to call a function:

```isc
(
var func = {
  var x = 10;
  x;
};
func.();   // returns 10
)
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

## Basic Control Structures

In ``sclang``, control sequences are functions.
They expect one or multiple functions that are executed conditionally.
We already saw the ``if``-function, which expect one boolean expression (a predicate) and two functions.

The ``while``-function expects one predicate and another function that can be executed as long as the predicate is true.
For example:

```isc
(
var i = 0;
while({i < 10}, {i.postln; i = i + 1;});
)
```

The ``for``-function works much more restricted:

```isc
(
for(0, 9, {arg i; i.postln;})
)
```

A little more flexible is the ``forBy``-function for which ``for`` is a special case.
It allows us to define an additional ``stepValue``:

```isc
(
forBy(0, 9, 2, {arg i; i.postln;}) // 0 2 4 6 8
)
```

The ``do``-function iterates over a given sequence, similar to a ``foreach`` of other languages (``for`` in ``Python``).

```isc
(
do((1..9), {arg item, i; item.post; ",".post; i.postln;})
)
```

Here ``item`` is the element of the ``Array`` generated by ``(1..9)`` and ``i`` is the index of the element!

A ``switch``-function expects a ``value`` and pairs of tested values and functions to be executed.
The test checks for equality ``==``.
To be more flexible and to use different predicates one can use the ``case``-function which is as efficient as ``if``-statements.

## Classes and Objects

In ``sclang`` the constructor of an object is called by ``Classname.new``.

```isc
var numbers = Array.new(10);
```

However, we can omit the ``new``.

```isc
var numbers = Array(10);
```

Classes can contain class methods (static methods) and object methods.
A class method starts with an ``*``.
For example, I implemented a new class ``Utils`` which offers a *class-method* ``initUtils`` that initializes all the useful analyzing tools depicted in {numref}`Fig. {number} <fig-ide-tools>`.

```isc
Utils {
    *initTools {
        arg activateLimiter = false;
        // reboot all
        Server.killAll;
        Server.local.options.numBuffers = 1024 * 16;
        Server.local.options.memSize = 8192 * 64;
        Server.local.boot;
        Server.local.waitForBoot(onComplete: {
            // re-initialize tools
            Server.local.makeWindow;
            Server.local.meter;
            Server.local.scope;
            FreqScope.new;
            Server.local.plotTree;

            if(activateLimiter) {
                StageLimiter.activate;
            }
        });
    }
}
```

Another significant difference between functions and methods is that for methods, the return value has to be marked by a ``^``.
The following code depicts the object-method ``reverse`` of ``ArrayedCollection`` which is the super-class of ``Array``:

```isc
reverse {
    var i = 0;
    var res = this.copy;
    var size1 = res.size - 1;
    var halfsize = res.size div: 2;
    halfsize.do({ arg i;
        res.swap(i, size1 - i);
    });
    ^res
}
```

First the original array ``this`` is copied.
Then elements are swapped accordingly.
And finally the copy ``res`` is returned.
The expression ``res.size div: 2;`` is equivialent to ``res.size / 2;`` or ``res.size.div(2);``.

Let us look at another example, i.e., the class ``Complex``:

```isc
Complex : Number {
    var <>real, <>imag;

    *new { arg real, imag;
        ^super.newCopyArgs(real, imag);
    }

    + { arg aNumber, adverb;
        if ( aNumber.isNumber, {
            ^Complex.new(real + aNumber.real, imag + aNumber.imag)
        },{
            ^aNumber.performBinaryOpOnComplex('+', this, adverb)
        });
    }
...
```

The class has two attributes  ``real`` and ``img`` indicated by the ugly ``<>`` and initialized by the constructor.
Furthermore, it has a method ``+`` which takes one non-optional and one optional argument.
``aNumber`` is another complex number and ``adverb`` is a modifier that modifies the plus operation if ``aNumber`` is not a number.
If we ignore the second argument, the ``+`` method returns a new complex number by adding two complex numbers together.
Therefore, ``+`` is a *pure function*.

I may come back to object-oriented programming with ``sclang`` but for now we do not really need it.
The best way to learn more about it is to look into the source code pressing ``i + CMD``.

## Playing Sound

Let us create the most simple sound possible: the sound of a sine wave. 
First, we define a function that returns a so-called unit generator [UGen](sec-ugens) that starts when we call ``play()``.
In fact ``play()`` is shorthand for

1. transforming our [UGen](sec-ugens) into a full [SynthDef](sec-synths) (synth definition), 
2. adding it to the audio server and 
3. executing it by generating a synth on it.

```{admonition} Protect your ears!
:name: attention-protect-your-ears
:class: attention
[SC](https://supercollider.github.io/) will not protect you from any wrongdoing. 
It will play the sound you defined, and if this sound can hurt your ears, you have to be sure to protect them.
It is good practice to use headphones far away from your ears if you do not know what sound to expect!
```

There are hundreds of different [UGens](sec-ugens).
Basically, they spit out real numbers over time. 
For example, ``SineOsc`` samples a sine wave.

```isc
~sine = {arg freq=200; SinOsc.ar(freq, mul: 0.2)};
~sineplay = ~sine.play();
```

If we execute this code, we get a warning that the server ``localhost`` is not running.
We have to boot the real-time audio server **scsynth** first:

```isc
s.boot;
~sine = {arg freq=200; SinOsc.ar(freq, mul: 0.2)};
~sineplay = ~sine.play();
```

``~sine`` is a function that returns ``SinOsc.ar(freq, mul: 0.2)`` which is a ``BinaryOpUGen``.

```{admonition} Sound termination
:name: attention-sound-termination
:class: attention
To terminate all sound press ``CMD`` + ``.``. **This might be the most important shortcut of all.**
```

If we press ``CMD`` + ``i`` while the curser is at ``play()`` and we select the implementation for ``Function``, we can see lookup what ``~sine.play()`` actually does:

```isc
play { arg target, outbus = 0, fadeTime = 0.02, addAction=\addToHead, args;
    var def, synth, server, bytes, synthMsg;
    target = target.asTarget;
    server = target.server;
    if(server.serverRunning.not) {
        ("server '" ++ server.name ++ "' not running.").warn; ^nil
    };
    def = this.asSynthDef(
        fadeTime:fadeTime,
        name: SystemSynthDefs.generateTempName
    );
    synth = Synth.basicNew(def.name, server);
        // if notifications are enabled on the server,
        // use the n_end signal to remove the temp synthdef
    if(server.notified) {
        OSCFunc({
            server.sendMsg(\d_free, def.name);
        }, '/n_end', server.addr, argTemplate: [synth.nodeID]).oneShot;
    };
    synthMsg = synth.newMsg(target, [\i_out, outbus, \out, outbus] ++ args, addAction);
    def.doSend(server, synthMsg);
    ^synth
}
```

``play()`` constructs a new ``SynthDef``, adds it to the server, and generates a synth which is returned.
The ``fadeTime`` makes sure that the sound ramps up over a certain amount of seconds.
For example, we can increase ``fadeTime``:

```isc
~sineplay = ~sine.play(fadeTime: 2.0);
```

``play`` comes in handy if we wanna just try something out -- if we want to explore sounds in a quick and dirty way.
For complex synth, we will define our own ``SynthDef``.
