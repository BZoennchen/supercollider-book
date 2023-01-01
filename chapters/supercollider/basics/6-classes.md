# Classes and Objects

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

Objects of this class have two (object)-attributes ``real`` and ``img`` indicated by the ugly ``<>`` and initialized by the constructor.
Furthermore, it has a method ``+`` which takes one non-optional and one optional argument.
``aNumber`` is another complex number and ``adverb`` is a modifier that modifies the plus operation if ``aNumber`` is not a number.
If we ignore the second argument, the ``+`` method returns a new complex number by adding two complex numbers together.
Therefore, ``+`` is a *pure function*.

I may come back to object-oriented programming with ``sclang`` but for now we do not really need it.
The best way to learn more about it is to look into the source code pressing ``i + CMD``.