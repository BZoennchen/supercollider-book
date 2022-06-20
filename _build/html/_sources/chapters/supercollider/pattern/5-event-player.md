# Event Player

Let us have a look at a first, very simple composition.
We finally make use of [Pbind](https://doc.sccode.org/Classes/Pbind.html) to construct a *discreate musical event simulation*.

```isc
(
Pbind(
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], inf),
    \dur, 0.4,
    \sustain, 0.1 
).play;
)
```

As already mentioned, ``Pbind`` is a unique ``Pattern`` that generates a ``Stream`` that spits out (musical) ``Events``.
Using the ``play`` method on the ``Pbind`` pattern, we play all the events the event stream gives us.
In that case, ``dur`` determines the waiting time between two successive events.
Thereby, we do not play all events instantly but create a rhythm.

```{admonition} Legato and Duration
:name: remark-legato-duration
:class: remark
If the sound sustains longer than ``dur`` we get overlapping sounds, i.e., [legato](sec-legato).
```

For example:

```isc
(
p = Pbind(
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], inf),
    \dur, 0.1,
    \sustain, 0.3
).play;
)
```

The same can be achieved by using the ``legato`` parameter:

```isc
(
p = Pbind(
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], inf),
    \dur, 0.1,
    \legato, 3.0
).play;
)
```

We can call ``stop`` on the ``Stream`` (not the ``Pattern``!) to stop it (or we can hit ``CMD`` + ``.`` / ``Ctrl`` + ``.`` as always).

Now you might ask: what do the events actually look like?
As already mentioned, each event is filled with default arguments if they are not defined.
For each defined argument, in our case, ``instrument``, ``freq``, ``dur``, and ``legato``, the method ``next`` is called on the value referenced by the corresponding name.
As we learned, if this value is a number, the number itself is returned.
If it is a pattern, it was already transformed into a stream when ``play`` was called and will return what the recursive evaluation of ``next`` gives us.

## Argument Dependence

Since we combine multiple ``Streams`` we may want to influence one value stream by the other.
For example, we might want that the ``amp`` depends on the frequency such that we can reduce the amplitude for higher pitches.#
There are multiple ways to do so.
One is by using one of the most powerful ``Pattern``, that is [Pfunc](https://doc.sccode.org/Classes/Pfunc.html).

``Pfunc`` expects a function as an argument and this function is called whenever the respective ``Stream`` generates its next value.
The argument of the ``next`` call is passed to the function.

```isc
(
var pattern = Pfunc({arg val; val*val;});
var square = pattern.asStream();
square.next(5);
)
```

``Pbind`` passes the whole event to this function.
Therefore, we can look inside the event, and use the information to compute our value.
In the following code snippet, we print the ``amp`` so you can see the effect.

```isc
(
p = Pbind(
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], inf),
    \dur, 0.25,
    \sustain, 0.3,
    \amp, Pfunc({arg event; min(1.0, event[\freq].linexp(100, 500, 1.0, 0.2)).postln;})
);
q = p.play;
)
```

``Pfunc`` can do a lot of other things and there is a pattern that is specifically designed for our case.
It is called [Pkey](https://doc.sccode.org/Classes/Pkey.html).
The following code creates exactly the same sound.

```isc
(
p = Pbind(
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], inf),
    \dur, 0.25,
    \sustain, 0.3,
    \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
);
q = p.play;
)
```

The third way to do this is to use a global variable.
However, this seems to be a really dirty method which I do not recommend.
I think, using ``Pkey`` is the cleanest way to do things.

## Cascading Pbinds

We can, of course, use multiple ``Pbinds``.

```isc
(
var intro, middle, outro;
intro = Pbind(
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], 3),
    \dur, 0.25,
    \sustain, 0.3,
    \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
);

middle = Pbind(
    \instrument, \saw,
    \freq, Pseq([233, 321, 344], 3),
    \dur, 0.25,
    \sustain, 0.3,
    \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
);

outro = intro = Pbind(
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], 3),
    \dur, 0.25,
    \sustain, 0.3,
    \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
);

p = Pseq(list: [intro, middle, outro], repeats: 2);
q = p.play;
)
```

What a masterpiece ;).
We can generate the same piece using only one ``Pbind``:

```isc
(
p = Pbind(
    \instrument, \saw,
	\freq, Pseq([
		Pseq([440, 220, 330], 3), 
		Pseq([233, 321, 344], 3),
		Pseq([440, 220, 330], 3)
	], repeats: 2),
    \dur, 0.25,
    \sustain, 0.3,
    \amp, Pkey(\freq).linexp(100, 500, 1.0, 0.2)
);
q = p.play;
)
```

We can also play multiple ``Pbinds`` in parallel.
We can imagine that each ``Pbind`` represents one musician in our assemble.
[Ppar](http://doc.sccode.org/Classes/Ppar.html) is a pattern that allows us to play multiple ``Pbinds`` in parallel.
In this example I use a fixed ``dur`` and [Rest](http://doc.sccode.org/Classes/Rest.html) to adjust the actual duration.

```isc
(
var melody = Pbind(
    \instrument, \saw,
    \scale, Scale.minor,
    \octave, 5,
    \degree, Pseq([
        3, 4, 3, \r,
        1, \r, 6, \r,
    ], inf),
    \dur, 1/4,
    \sustain, 0.2
);
var rythm = Pbind(
    \instrument, \snare,
    \dur, 1/8,
    \amp, Pseq([
        0.9, 1.2, \r, \r, 
        0.8, \r, 1.3, \r,
    ], inf)*0.2
);

Ppar([rythm, melody], inf).play;
)
```

Later we will see that we can organize our piece by using multiple ``Pbind``.
But for now, let's move on.

## Dynamic Changes

Ok, so we can define a pattern of events, i.e., a ``Pbind`` and play it.
But would it not be nice to change the pattern while playing it?
SuperCollider supports live programming via its powerful [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html).
I will discuss live programming in detail in section [Live Coding](sec-live-coding), but here, I want to mention the [Pbindef](https://doc.sccode.org/Classes/Pbindef.html) class.

``Pbindef`` keeps a reference to a ``Pbind`` in which single keys can be replaced.
It plays on when the old stream ends and a new stream is set and schedules the changes to the beat.
Basically, this means that we can:

1. change our pattern
2. re-evaluate the code 

and the change will appear soon after without ever stopping the pattern.
The only difference to ``Pbind`` is that a ``Pbindef`` requires a unique name.
Use the following ``Pbindef``, change the frequencies and re-evaluate the code.
Listen to what happens!

```isc
(
Pbindef(\melody,
    \instrument, \saw,
    \freq, Pseq([440, 220, 330], inf),
    \dur, 0.4,
    \sustain, 0.1 
).play;
)
```

## Naming Conventions

As mentioned in section [Value Conversions](sec-value-conversion), behind the scenes SuperCollider's event player helps us transforming different values into other values.
For example, we can play ``\midinote`` instead of ``\freq``.
The player will convert the pitch to the correct frequency.

However, we can only take advantage of this support if we name the arguments of the function defined in the ``SynthDef`` appropriately.

```{admonition} Naming Conventions
:name: attention-naming-convention
:class: attention
Always use the appropriate names, such as ``amp`` and ``freq`` for your ``SynthDef`` arguments!
```

## Examples

There are many different ``Pattern``, I will only discuss some of them which I find most important.
In fact, the official [documentation of SuperCollider](https://doc.sccode.org/) is not always super helpful but the tutorial [Understanding Streams, Patterns and Events](https://doc.sccode.org/Tutorials/Streams-Patterns-Events1.html) is an excellent source to get started.

TODO!
