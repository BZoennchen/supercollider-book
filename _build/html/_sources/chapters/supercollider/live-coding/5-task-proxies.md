# Task Proxy

[Sonic Pi](https://github.com/sonic-pi-net/sonic-pi) uses the concept of *live loops*, i.e., named threaded loops that can be synchronized and updated on the fly.
I found *live loops* extremely fun and useful, especially to explore new rythms and melodies.
Is there something similar in SuperCollider?
The answer is yes!

[Tdef](https://doc.sccode.org/Classes/Tdef.html) is part of the SuperCollider's [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html) and allows us to register *tasks* by key.
Registered tasks can be replaced with other task **while playing**.
The old task and its replacement can automatically crossfade and the repalcement time can be quantized.

Evaluate the following code, change the message and re-evaluate the code.
Observe the post window.

```isc
(
Tdef(\melody, {loop{
    "test".postln;
    0.25.wait;
}}).play;
)
```

This is great!
Let us combine ``Tdef`` with [Patterns](sec-pattern) play a melody that we can change on the fly:

```isc
(
Tdef(\melody, {
    var notes = Pseq([65, 70, 55, 63, 55, 70], inf).asStream;
    loop{
        Synth(\beep, [\freq: notes.next.midicps]);
        0.25.wait;
    }
}).play;
)
```

The same can be accomplished using a [TaskProxy](https://doc.sccode.org/Classes/TaskProxy.html).

```isc
~melody = TaskProxy().play;
(
~melody.source = {
    var notes = Pseq([65, 70, 55, 63, 55, 70], inf).asStream;
    loop{
        Synth(\beep, [\freq: notes.next.midicps]);
        0.25.wait;
    }
};
)
```