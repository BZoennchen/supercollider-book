(sec-variables)=
# Variables and Scope

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
number = 10;
```

results in an error because ``number`` is undefined. 
The code evaluation works similar to the cell evaluation in a ``Python`` Jupyter notebook, but variables (except for the single character) are *local*.
*Local* and *global variables* are **not** saved in the current *environment*.
Local variables only live inside their block and global/interpreter variables are constructed and saved prematurely.
You can print out the *current environment* by just accessing it:

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
:name: remark-exponential
:class: remark
Like ``Python``, ``sclang`` supports the exponential operator ``**``.

```isc
2**4 // 16.0
```
````