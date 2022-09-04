# Routines & Tasks

A [Routine](https://doc.sccode.org/Classes/Routine.html) is like a function that you can evaluate only partly at a time.
Routines and functions can be used almost interchangeable.
Within a routine, you use the ``yield`` method to return a value and pause its execution.
The next time you evaluate the routine, it picks up where it left off.
In that sense, a routine is similar to a [stream](sec-stream) but it does not only return values but can do stuff, i.e., realize *sideeffects*.

```isc
(
r = Routine({
    1.yield;
    2.yield;
    3.yield;
});
r.next.postln; // 1
r.next.postln; // 2
r.next.postln; // 3
r.next.postln; // nil
)
```

Routines that return numeric values can be scheduled on a *clock*.
If we ``play`` the routine, it will be automatically scheduled on the default clock.

```isc
(
r = Routine({
    "1".postln;
    1.yield;
    "2".postln;
    2.yield;
    "3".postln;
    3.yield;
    "4".postln;
});
r.play;
)
```

We can schedule the routine on a specific clock ``t`` by providing it via ``r.play(t)``

There is even a shorter version of this code.
*Forking* a function will transform the function into a routine and *play* it immediately.

```isc
(
{
    "1".postln;
    1.yield;
    "2".postln;
    2.yield;
    "3".postln;
    3.yield;
    "4".postln;
}.fork;
)
```

A [Task](https://doc.sccode.org/Classes/Task.html) is a pausable process.
It can only be played in combination with a *clock*.
In contrast to a routine, a task can be *paused*.
In addition, it prevents you from playing it multiple times.

The following example is from *The SuperCollider Book* {cite}`wilson:2011`.
Note that when the *task* reaches the line ``nil.yield`` it will *pause*.
If you evaluate ``t.resume(0)``, it will *resume*.
The example uses the *gated* [default instrument](sec-default-instrument).

```isc
(
t = Task({
    loop({
        3.do({
            x.release(0.1);
            x = Synth(\default, [\freq: 76.midicps]);
            0.5.wait;
            x.release(0.1);
            x = Synth(\default, [\freq: 73.midicps]);
            0.5.wait;
        });
        "Waiting".postln;
        nil.yield;
        x.release(0.1);
        x = Synth(\default, [\freq: 69.midicps]);
        1.wait;
        x.release;
    });
});
)

t.resume(0);
```