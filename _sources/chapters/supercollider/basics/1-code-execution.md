# Code Execution

The [SuperCollider IDE](sec-scide) is build for interaction.
If you are familiar with the concept of notebooks, for example, Jupyter notebooks or Mathematica notebooks, you already know what I mean.
The idea is that you can execute code while developing.
Instead of writing a complete program, you are constantly stimulated to run small code snippets.
In live coding, this is embraced even more, but it is also good practice if you learn and explore SuperCollider in general.

SuperCollider initializes an [Environment](https://doc.sccode.org/Classes/Environment.html), i.e., a collection of things that can be accessed via name.
Interacting with the IDE will manipulate this environment on the fly.

## Triggering the Evaluation

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

## Execution of C++ Code

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

## Order of Execution

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

Especially in within control structures this can lead to bugs that are hard to find. 
The following code prints ``'ho'`` the the post window.

```isc
(
if(true || false && false,{
    "hi".postln;
}, {
    "ho".postln;
})
)
```
