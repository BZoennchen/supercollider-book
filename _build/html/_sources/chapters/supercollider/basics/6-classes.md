# Classes and Objects

**Disclaimer**: The book is not about programming in general. Therefore, this section contains only a short description of the topic and assumes that the reader is familiar with one or more object-orientated programming (OOP) languages.

Before we start, note that we can not interactively define new classes.
Thus, we can not use the interpreter window to define and execute the code that involves a new class.
Instead, classes have to be compiled before we can use them!
The following warning is copied from the official SuperCollider documentation from section [Writing Classes](https://doc.sccode.org/Guides/WritingClasses.html).

```{admonition} Compiling Class Files
:name: attention-class-files
:class: attention
Class definitions are statically compiled when you launch SuperCollider or recompile the library.
This means that class definitions must be saved into a file with the extension ``.sc``, in a disk location where SuperCollider looks for classes. Saving into the main class library (SCClassLibrary) is generally not recommended. 
It's preferable to use either the user or system extension directories.

It is not possible to enter a class definition into an interpreter window and execute it.
```

## Instantiation

In ``sclang`` the constructor of an object is called by ``Classname.new``.

```isc
var numbers = Array.new(10);
```

However, we can omit the ``new``.

```isc
var numbers = Array(10);
```

This calls the *class method* ``new`` of the [Array](https://doc.sccode.org/Classes/Array.html) class.

## Class Definition

All classes are [Objects](https://doc.sccode.org/Classes/Object.html), i.e., they inherit from the fundamental base class [Object](https://doc.sccode.org/Classes/Object.html) automatically.
This makes it necessary to call the constructor of [Object](https://doc.sccode.org/Classes/Object.html).

To copy the arguments of the constructor to into the object variables we can call ``newCopyArgs`` of [Object](https://doc.sccode.org/Classes/Object.html).
``Object.newCopyArgs(... args)`` creates a new instance and copies the arguments to the instance variable in **the order that the variables were defined**.
Of course, class variables will be ignored.
Therefore, the order is semantically significant!

```isc
MyClass {           // Object is implied
    var a, b, c;    // Object variables / attribtes
    classvar d;     // Class variabels / attributes

    *new {          // Class method
        arg arg1, arg2, arg3;
        // Will copy arg1, arg2, arg3 to variables a, b, c
        ^super.newCopyArgs(arg1, arg2, arg3);
    }

    add {           // Object method
        var sum = 0;
        sum = a + b + c;
        ^sum;
    }
}
```

If you need more control over the initiation of an object you can use the ``init`` object method:
The expression ``a = arg1 ? a;`` makes sure that ``a`` will only change if it is not already initialized, i.e., in case you call init after the object has been created.

```isc
MyClass {           // Object is implied
    var a, b, c;    // Object variables / attribtes
    classvar d;     // Class variabels / attributes

    *new {          // Class method
        arg arg1, arg2, arg3;
        ^super.new.init(arg1, arg2, arg3);
    }

    init {          // Object method
        arg arg1, arg2, arg3;
        a = arg1 ? a;
        b = arg2 ? b;
        c = arg3 ? c;
    }

    ...
}
```

Instance variables (the attributes of the object) are defined by using the keyword ``var`` while class variabels (the attribute of the class which are shared by all objects of the class) are defined via the keyword ``classvar``.
Instance variables will *shadow* class variables of the same name.

Classes can contain class methods (static methods) and object methods.
A class method starts with an ``*``.
For example, I implemented a new class [MIDIRecorder](https://github.com/BZoennchen/algorithmic-compositions/blob/main/sc/extensions/classes/MIDIRecorder.sc) which offers a *class-method* ``*new`` that calls ``init`` which initializes all the object variables.

```isc
MIDIRecorder {
    // Object variables / attribtes
    var name, instrument, history, synths, <events, clock, noteOn, mono, paused, pauseTime, midiDefOn, midiDefOff;

    *new {      // Class method
        arg name, instrument = \default, mono = false;
        ^super.new.init(name, instrument, mono);
    }

    init {      // Object method
        arg argname, arginstrument, argmono;
        name = argname ? name;
        instrument = arginstrument ? instrument;
        mono = argmono ? mono;
        history = Array.fill(127, {[]});
        synths = Array.newClear(127);
        clock = TempoClock();
        events = [];
        paused = true;
        noteOn = false;
        pauseTime = 0.0;

        clock.permanent = true;

        ...
    }

    record {    // Object method
        history = Array.fill(127, {[]});
        synths.do({arg synth; synth.set(\gate, 0);});
        synths = Array.newClear(127);
        events = [];
        paused = false;
    }

    ...

```

Another significant difference between functions and methods is that for methods, the return value has to be marked by a ``^``.
The following code depicts the object-method ``reverse`` of [ArrayedCollection](https://doc.sccode.org/Classes/ArrayedCollection.html) which is the super-class of [Array](https://doc.sccode.org/Classes/Array.html):

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

## Getter and Setter

By default, variables are not accessible outside of the class or instance.
A method must be added to explicitly give access.
These methods are called *getter* (returns the variable) and *setter* (sets the value of the variable).
``sclang`` allows these methods to be added via a shortcut by adding ``<`` (getter) and/or ``>`` (setter) in front of the variable definition.

Let us look at another example, i.e., the class [Complex](https://doc.sccode.org/Classes/Complex.html):

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

Objects of this class have two (object)-attributes ``real`` and ``img`` indicated by the signal word ``var`` and they are accessible from outside indicated by the ugly rue ``<>``.
The instance variables are initialized by the constructor.
The name **and order** is identical!

Furthermore, the class defines a method ``+`` which takes one non-optional and one optional argument.
``aNumber`` is another complex number and ``adverb`` is a modifier that modifies the plus operation if ``aNumber`` is not a number.
If we ignore the second argument, the ``+`` method returns a new complex number by adding two complex numbers together.
Therefore, ``+`` is a *pure function*.

I may come back to object-oriented programming with ``sclang`` but for now we do not really need it.
The best way to learn more about it is to look into the source code pressing ``i + CMD``.