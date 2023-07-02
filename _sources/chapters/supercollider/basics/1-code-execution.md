# Code Execution

The [SuperCollider IDE](sec-scide) iis designed for interactivity. 
If you're familiar with the concept of notebooks, such as Jupyter or Mathematica notebooks, you'll grasp what I mean. 
The idea is to execute code incrementally as you develop. Instead of writing a complete program all at once, you're encouraged to run small code snippets. Each code execution alters your environment, that is, the state of your program. This dynamic interaction is especially evident in live coding, but it's also a useful practice when learning and exploring SuperCollider in general.

SuperCollider initializes an [Environment](https://doc.sccode.org/Classes/Environment.html), which is a collection of entities accessible by name. 
Interacting with the IDE allows you to manipulate this environment in real-time."

## Triggering the Evaluation

Let's get started! 
We'll write some ``sclang`` code and execute it via the REPL (Read-Eval-Print Loop). 
To execute the following line, press ``SHIFT`` + ``RETURN`` while your cursor is on the code line.

```isc
"Hello World!".postln;
```

In SuperCollider, as there is no use of code cells, we must define blocks of code ourselves.
To execute multiple lines, we need to enclose the code within brackets ``(`` and ``)``, then evaluate the code using ``CMD`` + ``RETURN`` on Mac or ``CTRL`` + ``RETURN`` on Windows.

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

In both scenarios, you'll observe that the last line appears twice in the post window. 
SuperCollider always prints the last statement in the post window.

As in any other object-oriented language, we call a **method** named ``postln`` on an **object** that represents a [String](https://doc.sccode.org/Classes/String.html).
However, different terminology is used in the [SuperCollider documentation](https://doc.sccode.org/).
In this context, the object is the **receiver** of a **message** (method).

The object always functions as the first argument to the method (much like in ``Python``).
We refer to this object as ``this``.
For instance, we could also employ the following syntax:

```isc
postln("Hello World!");
```

A very useful hotkey is ``CMD`` + ``d`` (Mac OS) or ``CTRL`` + ``d`` (Windows).
It will open the documentation of the code your cursor is at.

```{admonition} Lookup Documentation
:name: remark-lookup-documentation
:class: remark
Use ``CMD`` + ``d`` (Mac OS) or ``CTRL`` + ``d`` (Windows) to look at the documentation of the class or method your cursor is at.
```

## Execution of C++ Code

Let's reverse-engineer the process that occurs when we print a string to the post window.

```{admonition} Lookup Source Code
:name: remark-lookup-source-code
:class: remark
Use ``CMD`` + ``i`` (Mac OS) or ``CTRL`` + ``i`` to look at the actual implementation of the class or method your cursor is at.
```

If we look into the source code of the ``postln`` method by using ``CMD`` + ``i`` and navigate to the class ``Object``, we can digest the following implementation:

```isc
postln { this.asString.postln; }
```

The curly brackets define a function with the name ``postln``.
As mentioned, ``this`` is either

1. the object the method is called on (if we use ``"Hello World!".postln;``) or
2. the first argument of the method (if we use ``postln("Hello World!");``)

Calling ``this.asString`` transformes the object into a ``String``.
Then ``postln`` of that ``String`` is called.
Of course in our case, the object is already a ``String`` and we directly call ``postln`` of ``String``!

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

>``g->sp`` is the top of the stack and the last argument pushed. 
``g->sp - inNumArgsPushed + 1`` is the **receiver** and where the result goes.

In our case, ``g->sp`` is the [String](https://doc.sccode.org/Classes/String.html) object.
This interaction between ``sclang`` and ``C++`` reminds me of the interaction between ``Python`` and ``C++``.
As long as we do not write our own [primitives](https://doc.sccode.org/Guides/WritingPrimitives.html), we can ignore the ``C++`` interaction.

## Order of Execution

In ``sclang``, the code is strictly evaluated from left to right.
All operands have the same priority, which might lead to unexpected results.
The expression

```isc
4 + 4 * 5 // 40
```

returns ``(4 + 4) * 5 = 40`` instead of ``4 + (4 * 5) = 24``.

```{admonition} Order of Execution 
:name: attention-order-of-execution
:class: attention
``sclang`` uses a *strictly left to right order of execution*.
```

Especially within control structures this can lead to bugs that are hard to find. 
The following code prints ``'ho'`` to the the post window.

```isc
(
// true || false => true && false => false
if(true || false && false,{
    "hi".postln;
}, {
    "ho".postln;
})
)
```