# Basics

Before we go into the details I have to say that, coming from programming languages such as ``Java``, ``C`` and ``Python``, the syntax of ``sclang`` is not the most beautiful.
However, this first expression hides the fact that a lot of decisions regarding syntax make sense at a second glance.
So don't be scared by the first impression.

In this section, I will give a starting point such that the reader can start experimenting with SuperCollider.
By only reading this section and [The Ecosystem](sec-ecosystem) you have a good building ground to start your discovery with the SuperCollider platform.

## Code Execution

The [SuperCollider IDE](sec-scide) (SCIDE) is build for interaction.
If you are familiar with the concept of Notebooks, for example, Jupyter-Notebooks or Mathematica-Notebooks, you already know what I mean.
The idea is that you can execute code while developing.
Instead of writing a complete program, you are constantly stimulated to run small code snippets.
In live coding, this is embraced even more but it is also good practice if you learn and explore SuperCollider in general.

### Triggering the Evaluation

Let's start!
Let's write some ``sclang`` code and execute it via the REPL (Read–Eval–Print Loop).

To execute the following line press ``SHIFT`` + ``RETURN`` while your cursor is at the code line.

```isc
"Hello World!".postln;
```

To execute multiple lines we have to enclose the code in brackets ``(``, ``)`` and we have to evaluate the code using ``CMD`` + ``RETURN`` on Mac and ``CTRL`` + ``RETURN`` on Windows.

```{admonition} Code Execution 
:name: hint-code-execution
:class: hint
Use ``SHIFT`` + ``RETURN`` to evaluate a single line of code and use ``CMD`` + ``RETURN`` to evaluate a code block.
```

For example:

```isc
(
"Hello World!".postln;
"We make some music".postln;
)
```

In both cases you will notice that the last line is printed twice in the post windows.
This is because the last statement will always be printed on the post window.

Similar to any other object-oriented language, we call a **method** ``postln`` on the **object** representing a ``String``.
However, in the [SuperCollider documentation](https://doc.sccode.org/) they use different terms.
The object is the **receiver** of a **message** (method).

The object is always the first argument of the method (similar to ``Python``).
We refer to this object as ``this``.
For example, we could also use the following syntax:

```isc
postln("Hello World!");
```

A very useful key combination is ``CMD`` + ``d``.
It will open the documentation of the code your cursor is at.

```{admonition} Lookup Documentation
:name: hint-lookup-documentation
:class: hint
Use ``CMD`` + ``d`` to look at the documentation of the class or method your cursor is at.
```

### Execution of C++ Code

```{admonition} Lookup Source Code
:name: hint-lookup-source-code
:class: hint
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
It is executed and if nothing goes wrong the code below (``^this.primitiveFailed``) is **not** executed.
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

In the [documentation](https://doc.sccode.org/Guides/WritingPrimitives.html) we find the following explanation

>``g->sp`` is the top of the stack and is the last argument pushed. ``g->sp - inNumArgsPushed + 1`` is the **receiver** and where the result goes.

In our case ``g->sp`` is the ``String`` object.
This interaction between ``sclang`` and ``C++`` reminds me of the interaction between ``Python`` and ``C++``.
As long as we do not write our own [primitives](https://doc.sccode.org/Guides/WritingPrimitives.html) we can ignore the ``C++`` interaction.

### Order of Execution

In ``sclang`` the code is strictly evaluated from left to the right.
This means that all operands have the same priority which might lead to unexpected results.

```isc
4 + 4 * 5
```

gives ``(4 + 4) * 5 = 40`` instead of ``4 + (4 * 5) = 24``.

```{admonition} Order of Execution 
:name: important-order-of-execution
:class: important
``sclang`` uses a *strictly left to right order of execution*.
```

## Variables and Scope

Here we encounter the first inconvenience. 
In [(SC)](https://supercollider.github.io/) there are some special pre-defined variables. 
Each **single character variable** ``[a-z]`` is pre-defined and globally available.
They are called *Interpreter variables*.

```{admonition} The Local Server Variable 
:name: important-local-server-variable
:class: important
By default, the variable ``s`` holds a reference to the local audio server.
```


If you come from a modern programming language, this is strange. 
However, it is often useful for prototyping in [(SC)](https://supercollider.github.io/). 
A very special variable is ``s`` because it holds a reference to the default local server. 
Therefore, to start the audio server, we evaluate:

```isc
s.boot;
```

No one stops you from overwriting ``s``, but I would not recommend it. 
As already mentioned, to define a code-block we use round brackets. 
We can use ``x`` without defining it because it is already defined for us.

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
The code evaluation works similar to the cell evaluation in a ``Python`` Jupyter-Notebook but variables (except for the single character) are *local*.
Without round brackets, the following code does not work

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
Note that we have to execute the whole block otherwise ``number`` is still *local* within one line.

To define our own *global* variable we have to use ``~`` in front of the variable name, for example:

```isc
~number = 10;
~number;
```

works just fine.
These variables are called *Environment variables*.

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

As their name indicates, variables can be reassigned and we can give them any new value (dynamic types) at any time.

## Arrays

A signal is basically a sequence of numbers.
This sequence can be realized by an ``Array``.

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

There are also factory methods to create two

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

and even n-dimensional Arrays

```isc
// [ [ [ 0, 0, 0, 0 ], [ 0, 1, 2, 3 ], [ 0, 2, 4, 6 ], [ 0, 3, 6, 9 ] ], 
//   [ [ 0, 1, 2, 3 ], [ 0, 2, 4, 6 ], [ 0, 3, 6, 9 ], [ 0, 4, 8, 12 ] ], 
//   [ [ 0, 2, 4, 6 ], [ 0, 3, 6, 9 ], [ 0, 4, 8, 12 ], [ 0, 5, 10, 15 ] ], 
//   [ [ 0, 3, 6, 9 ], [ 0, 4, 8, 12 ], [ 0, 5, 10, 15 ], [ 0, 6, 12, 18 ] ] ]

Array.fillND([4, 4, 4], { arg a, b, c; a+b*c; }); 
```

### Concatenation

First, we can concatenate by creating a new array and copying all elements:

```isc
[1,2,3] ++ [4,5,6] // [ 1, 2, 3, 4, 5, 6 ]
```

or we can add all elements from one Array to the other:

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

In ``sclang`` functions are first-class objects which means that a function can be an argument of another function.
The language drives the programmer to make use of this fact in various ways.

To define a function, we encapsulate its content by curly brackets, and to execute it, we call ``value`` on it:

```isc
(
var func = {
  var x = 10;
  x;
};
func.value();   // returns 10
)
```

We actually do not have to write down ``value`` to call a function

```isc
(
var func = {
  var x = 10;
  x;
};
func.();   // returns 10
)
```

This looks a little bit weird but works just fint.

In ``sclang`` there is no ``return`` keyword.
We only have to call ``func.value`` for functions and not for methods of an object or class.
A function always returns the content of the last evaluated statement, in this case ``x``.
In my personal opinion, an additional keyword can make the code more readable.

To see what I mean by making use of functions as first-class objects we can look at the [control structures](https://doc.sccode.org/Reference/Control-Structures.html).
``if`` is in fact a function that takes three arguments:

1. the condition
2. a function which is executed if the condition is ``true``
3. a function which is executed if the condition is ``false``
   
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

If we want the ``func`` to return the same randomly chosen value each time it is called we can use a [Closure](https://en.wikipedia.org/wiki/Closure_(computer_programming))
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
We already saw the ``if``-Functions which expect one boolean expression (a predicate) and two functions.

The ``while``-functions expects one predicate and another function that can be executed as long as the predicate is true.
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
For example I implemented a new class ``Utils`` which offers a **class-method** ``initUtils`` that initializes all the useful analyzing tools depicted in {numref}`Fig. {number} <fig-ide-tools>`.

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

Another important difference between functions and methods is that for methods, the return value has to be marked by a ``^``.
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

First the origin array ``this`` is copied.
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
``aNumber`` is another complex number and ``adverb`` is a modifier that modifies, in this case, modifies the plus operation.
If we ignore the second argument, the ``+`` method returns a new complex number by adding two complex numbers together.
Therefore, ``+`` is a pure function.

I may come back to object-oriented programming with ``sclang`` but for now we do not really need it.
The best way to learn more about it is to look into the source code pressing ``i + CMD``.

## A First Sine Wave

Let us create the most simple sound possible: the sound of a sine wave. 
First, we define a function that returns a so-called unit generator [UGen](sec-ugens) that starts when we call ``play()``.
In fact ``play()`` is shorthand too and 

1. transforms our the [UGen](sec-ugens) into a ``SynthDef`` (synth definition), 
2. adds it to the server and 
3. executes it.

```{admonition} Protect your ears!
:name: hint-protect-your-ears
:class: warning
[SC](https://supercollider.github.io/) will not protect you from any wrongdoing. 
It will play the sound you defined and if this sound can hurt your ears you have to be sure to protect them.
It is good practice to use headphones that are far away from your ears if you do not know what sound to expect!
```

There are hundreds of different [UGens](sec-ugens).
Basically, they spit out real numbers over time. 
For example ``SineOsc`` samples a sine wave.

```isc
~sine = {arg freq=200; SinOsc.ar(freq, mul: 0.2)};
~sineplay = ~sine.play();
```

If we execute this code, we get a warning that the server 'localhost' is not running.
We have to boot the real-time audio server **scsynth** fist, by:

```isc
s.boot;
~sine = {arg freq=200; SinOsc.ar(freq, mul: 0.2)};
~sineplay = ~sine.play();
```

```{admonition} Sound termination
:name: hint-sound-termination
:class: hint
To terminate all sound press ``CMD`` + ``.``. **This might be the most important shortcut of all.**
```

``~sine`` is a function that returns ``SinOsc.ar(freq, mul: 0.2)`` which is a ``BinaryOpUGen``.

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
For example we can increase ``fadeTime``:

```isc
~sineplay = ~sine.play(fadeTime: 2.0);
```

``play`` comes in handy if we wanna just try something out -- if we want to explore sounds in a quick and dirty way.
For complex synth, we will define our own ``SynthDef``.


## A First SynthDef

Instead of using ``play()`` we can instead implement our own ``SynthDef``.
This gives us much more control over sound creation.

```isc
(
// (1) Define a new SynthDef / a blueprint for a Synth
var synthDef = SynthDef(\sineWave, {
    arg freq=200;
    var sig, env;

    env = EnvGen.kr(Env.perc, doneAction: Done.freeSelf);
    sig = SinOsc.ar(freq, mul: 0.2)!2 * env;

    Out.ar(0, sig);
});

// (2) Add the SynthDef to the server
synthDef.add();
)

// (3) Generate a new Synth of \sineWave on the server
Synth(\sineWave);
```

By calling ``SynthDef.new()`` or just ``SynthDef()`` we generate a new factory object that produces synth according to the ``SynthDef`` blueprint.
On behalf of the perspective of the audio server **scsynth**, this factory object produces ``Synth`` objects!
A ``SynthDef`` encapsulates the client-side representation of a given definition and provides methods for creating new defs, writing them to disk, and streaming them to a server.

Each ``SynthDef`` has a name which we have to use if we want to generate a ``Synth`` produced by ``SynthDef``.
The name can either be a ``String`` ``"sineWave"`` or a symbol ``\sineWave``.

By calling ``synthDef.add()`` we add our ``SynthDef`` to the server.
From then on, we can create ``Synth`` of this definition.
Note that if we terminate the server, the ``SynthDef`` is lost.

The second argument of the ``SynthDef`` is a function that has to be a **UGen Graph Function**.
It is an instance of Function which details how the ``SynthDef`` unit generators are interconnected, their inputs and outputs, and what parameters are available for external control.

We declare an argument called ``freq`` with a default value of ``200``.
Then we create an [envelope](sec-envelope) which has a percussive shape.
The envelope controls the amplitude of our sine wave over time.
Finally, we send the audio signal ``sig`` to the output bus ``0``.

By using ``!2`` after the signal creation,

```isc
SinOsc.ar(freq, mul: 0.2)!2
```

we duplicate the signal.
The result is an array of lengths two each containing a signal.
By writing this array to the output bus at channel ``0``, channel ``0`` gets the first element of the array and channel ``1`` the second one.
Therefore, we hear the sound in both speakers.

We can also **store** the ``SynthDef`` permanently on our hard drive by calling ``store()`` instead of ``add()``.
This call will create the file ``sineWave.scsyndef`` in the ``synthdefs`` directory which can be found in your [SuperCollider](https://supercollider.github.io/) Application directory.
If you restart [SuperCollider](https://supercollider.github.io/) all ``SynthDefs`` in the ``snythdefs`` directory are added to the server automatically.

## Server-side and Client-side language

``SynthDefs`` are static!
This means that the dynamics of a sound can only be influenced by [UGens](sec-ugens) and the arguments of the **UGen Graph Function**.
Those arguments can only be arguments of [UGens](sec-ugens)!
For example, any iteration or ``Array`` within a ``SynthDef`` has to be of fixed size.
Randomness can only be provided by [UGens](sec-ugens).

For example, the following ``SynthDef`` creates ``Synth`` of equal frequency which is chosen by random between ``200`` and ``400`` at the time of the creation of the ``SynthDef``:


```isc
SynthDef(\sineWave, {
    var sig, env;

    env = EnvGen.kr(Env.perc, doneAction: Done.freeSelf);
    sig = SinOsc.ar(200.rand + 200, mul: 0.2)!2 * env;

    Out.ar(0, sig);
});
```

Therefore, each time we create a ``Synth`` it sounds the same.
However, we can use the [UGen](sec-ugens) ``Rand`` which is evaluated when we actually play the ``Synth``:

```isc
SynthDef(\sineWave, {
    var sig, env;

    env = EnvGen.kr(Env.perc, doneAction: Done.freeSelf);
    sig = SinOsc.ar(Rand(200, 400), mul: 0.2)!2 * env;

    Out.ar(0, sig);
});
```

Each time we call ``Synth(\sineWave)`` we hear a different sound.