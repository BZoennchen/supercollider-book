(sec-scheduling)=
# Scheduling

## Clocks

A *clock* is a timed scheduler.
It keeps track of time and allows tasks to be scheduled for some time in the future (``sched``, ``schedAbs`` or ``play``).
When the time at which a task was scheduled is up, the task is awoken, i.e., its ``awake`` method is evaluated.
In case of a [Function](sec-functions) ``awake`` calls ``value`` and in case of a [Routine](https://doc.sccode.org/Classes/Routine.html) it calls ``next``.
If the value returned by this method is a number, the task is automatically **rescheduled** for the time equal to its last scheduled time plus the return value (in beats).

Clocks gives the user the ability to schedule certain events at a specific time.
If a clock is started, it ticks endlessly in the background.
There are three different type of clocks: 

+ [SystemClock](https://doc.sccode.org/Classes/SystemClock.html),
+ [AppClock](https://doc.sccode.org/Classes/AppClock.html), and
+ [TempClock](https://doc.sccode.org/Classes/TempoClock.html).

A ``SystemClock`` is more accurate than ``AppClock``, but it cannot call GUI primitives.
``TempoClock``, on the other hand, does not work in seconds but in beats per second (bps).

Let us define ``TempoClock`` that runs at 120 bpm, i.e., 2 beats per seconds, and prints out ``'Hello!'`` every beat:

```isc
(
t = TempoClock(2);
t.sched(0, {'Hello'.postln; 1}); // return 1 to continuously schedule.
)
```

Let us play some melody using a *clock*:

```isc
(
SynthDef(\beep, {
    var env = Env.perc().ar(doneAction: Done.freeSelf);
    var sig = SinOsc.ar(\freq.kr(440));
    sig = sig * env * \amp.kr(0.7);
    Out.ar(0, sig);
}).add;
)

(
t = TempoClock(2);
t.sched(0, {Synth(\beep, [\freq, rrand(40, 80).midicps]); 1})
)
```

## Routines & Tasks

A [Routine](https://doc.sccode.org/Classes/Routine.html) is like a function that you can evaluate a bit at a time, and in fact you can use one almost anywhere you'd use a function.
Within a routine, you use the ``yield`` method to return a value and pause execution.
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
If we ``play`` the routine, it will be automatically scheduled on a clock.

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