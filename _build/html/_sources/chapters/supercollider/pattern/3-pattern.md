# Pattern

[Pattern](https://doc.sccode.org/Classes/Pattern.html) is an abstract class that is the base for the patterns library. 
The classes of the pattern library form a rich and concise score language for music.
Patterns are the *stateless* blueprint of streams.
Calling ``asStream`` on a ``Pattern`` transforms it into a ``Stream``.
As already mentioned, all simple objects respond to this interface, by returning themselves.
Consequently, most objects are ``Pattern`` that define a ``Stream`` representing an infinite sequence of that object.

```{admonition} Pattern and Streams
:name: remark-pattern-and-streams
:class: remark
Similar to classes and objects, a [Pattern](https://doc.sccode.org/Classes/Pattern.html) is the blueprint for a [Stream](https://doc.sccode.org/Classes/Stream.html).
```

The incredible power of patterns lies in their ability to combine them.
Similar to unit generators, they are very flexible.
Let us look at a non-trivial example:

```isc
p = Pseq(list: [Prand((5..7)), Prand((1..4))], repeats: 2) * 10;
q = p.asStream();
q.next; // random number between 50 and 70
q.next; // random number between 10 and 40
q.next; // random number between 50 and 70
q.next; // random number between 10 and 40
q.next; // nil
```

``Pseq`` transforms an ``Array`` into a ``Pattern``. 
``Prand`` chooses from an array a random element.
In the above example, we combine both patterns.
``Pseq`` gets an array consisting of two ``Prand``patterns.
By using the parameter ``repeats: 2``, we configure ``Pseq`` to go over ``list`` twice.

Calling ``next`` on a ``Stream`` defined by a pattern consisting of pattern will lead to a recursive evaluation.
``next`` is called as long as the return value is another ``Stream``.
Let us look at another example.
In the following, we generate three melodies noted by midi notes, randomly (but weighted) chosen and transformed into frequencies.

```isc
(
var mel1, mel2, mel3;
mel1 = Pseq([40, 45, 55]);
mel2 = Pseq([77, 55, 67, 61]);
mel3 = Pseq([65, 43, 71]);
p = Pwrand([mel1, mel2, mel3], [3, 5, 2].normalizeSum, inf).midicps;
q = p.asStream;

10.do({
    q.next.postln;
})
)
```

Why are patterns useful?
Well, they can be combined, and all regular math functions can manipulate them if they return numbers.
In the above example, we multiply the ``Pseq``-pattern by 10 (calling ``asStream`` returns a ``BinaryOpStream``).
Patterns are compelling for building complex ``Streams``.
Therefore, they offer us a very comfortable way of building melodies without dealing with threads directly.
The pattern library abstracts the task of thread creation, synchronization, joining, termination, and clean up away.

Let us look at the following example.
Instead of using a pattern, we create an infinite loop.
Within the loop, we play a random midi note and sleep for ``0.2`` seconds.

```isc
// playing sound without using any pattern or stream
// instead we create a new thread.
(
{
inf.do({
    var midinote = 50 + 20.rand;
    midinote.play;
    0.2.wait;
})
}.fork;
)
```

This example, seems to work just fine.
But when our piece becomes more complicated and we use and manipulate multiple parameters of our synth, the code becomes hard to read and to interact with.

The difference between [Pattern](https://doc.sccode.org/Classes/Pattern.html) and (its) [Stream](https://doc.sccode.org/Classes/Stream.html) becomes clear if we think in musical terms.
A composition is a specific ``Pattern`` and a performance is a ``Stream`` of that pattern. 
Playing a piano can be seen as a stream of specific [Events](https://doc.sccode.org/Classes/Event.html).
We press some keys, with some velocity, for some duration, then we might wait for some amount of time and press the next keys.
