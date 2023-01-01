(sec-stream)=
# Streams

A [Stream](https://doc.sccode.org/Classes/Stream.html) is a series of elements that you can obtain one after another in a *lazy* fashion.
It is very similar to an [Array](https://doc.sccode.org/Classes/Array.html) with the difference that it is *lazy*.
*Laziness* means that instead of holding all values of the stream in memory (like an array does), values are generated on demand by a function.
Therefore, a stream can, in principle, offer infinitely many values, which is impossible for an array!
For example, we can define a function that gives us all integers.

```isc
~val = 0;
f = {~val = ~val + 1; ~val;};
f.();
```

If we evaluate the last line multiple times, we get 1, 2, 3, and so on.
``f`` represents an infinite stream of values.
We can use [FuncStream](https://doc.sccode.org/Classes/FuncStream.html) to create a [Stream](https://doc.sccode.org/Classes/Stream.html) of integers, i.e., an object that understands certain messages.
Then we can call ``next`` on the stream to get the next value.
If a (finite) stream runs out of values, it returns ``nil``.

```isc
(
~val = 0;
f = {~val = ~val + 1; ~val;};
x = FuncStream(f);
)
x.next(); // 1
x.next(); // 2
x.next(); // 3
```

In ``sclang`` everything is an [Object](https://doc.sccode.org/Classes/Object.html) and the class ``Object`` defines ``next`` to return the object itself.
Therefore, every object is a ``Stream`` that streams itself.
Consequently, almost everything can be viewed as a stream.
A ``5`` is a stream returning ``5``.
Calling ``next`` on an array will return itself.

```isc
5.next();  // 5
"hello".next; // "hello"
[1,2,3,4].next; // [1,2,3,4]
SinOsc().next // SinOsc
```

```{admonition} Everything is a Stream
:name: remark-everything-streams
:class: remark
In Supercollider's ``sclang`` everything is a stream.
```