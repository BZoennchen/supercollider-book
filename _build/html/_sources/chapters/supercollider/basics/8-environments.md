(sec-environments)=
# Environments

An [Environments](https://doc.sccode.org/Classes/Environment.html) is a collection of things that can be accessed by name.
When we start the SuperCollider IDE, it automatically creates an environment that can be evaluated by the following line:

```isc
currentEnvironment;
```

If this is your first evaluated command, the environment should be empty.
This environment contains variables, more specifically all *environment variables*.
A variable starting with a tilde is a environment variable, e.g.:

```isc
~number = 100;
```

If we re-evaluate the first statement, we can observe that ``currentEnvironment`` contains the value ``100`` and this value can be accessed via the name ``number``.
In fact ``~number`` is a shortcut for 

```isc
currentEnvironment.at(\number);
```

and an assignment like ``~number = 100;`` stands for

```isc
currentEnvironment.put(\number, 100);
```

We can create a fresh environment and push it onto the stack of environments.
In fact, that is more or less what happens when we call a function.

Let us create an environment by using a *global variable* ``d``.
Then we push it onto the stack.
Additional, let us create a new *environment variable* for the environment ``d``.

```isc
d = ()
d.push;
~number = 233;
```

If we re-evaluate

```isc
currentEnvironment
```

we can see the new variable.
Note that even the names of these two variables are the same, they live in different environments.
If we call

```isc
d.pop;
```

we remove ``d`` from the stack and ``currentEnvironment`` is equal to the environment before we pushed ``d`` onto the stack.
``~number`` is now equals ``100``.