# Clocks

A *clock* is a timed scheduler.
It gives the user the ability to schedule certain events at a specific time.
If a clock is started, it ticks endlessly in the background.
There are three different types of clocks: 

+ [SystemClock](https://doc.sccode.org/Classes/SystemClock.html),
+ [AppClock](https://doc.sccode.org/Classes/AppClock.html), and
+ [TempClock](https://doc.sccode.org/Classes/TempoClock.html).

A ``SystemClock`` is more accurate than ``AppClock``, but it cannot call GUI primitives.
``TempoClock``, on the other hand, does not work in seconds but in beats per second (bps).
It is the clock that is supposed to be used to schedule musical events.

Let us define ``TempoClock`` that runs at 120 bpm, i.e., 2 beats per seconds, and lets post ``'Hello!'`` at every beat:

```isc
(
t = TempoClock(2);

// return 1 to continuously re-schedule the function.
t.sched(0, {'Hello'.postln; 1}); 
)
```

``TempoClock`` keeps track of time and allows tasks to be scheduled at some point in time in the future (``sched``, ``schedAbs`` or ``play``).
When the time at which a task was scheduled is up, the task is awoken, i.e., its ``awake`` method is evaluated.
In case of a [Function](sec-functions), ``awake`` calls ``value`` and in case of a [Routine](https://doc.sccode.org/Classes/Routine.html) it calls ``next``.
If the value returned by the function is a number, the task is automatically **re-scheduled** at the time equal to its last scheduled time plus the return value (in beats).

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

Using a *gated* envelope makes it difficult to use a plain scheduler since we have to set the gate of the synth to ``0`` manually, i.e. by another scheduled function.
For example, the ``default`` instrument is consists of a gated envelople.
The following ugly code plays it buy using a ``TempClock``.

```isc
(
t = TempoClock(2);
~synth = nil;

// schedule the synth
t.sched(0, {~synth = Synth(\default, [\freq, rrand(40, 80).midicps]); 1});

// and ~dur beats afterwards its termination
t.sched(~dur, {~synth.set(\gate, 0); 1});
)
```

But as we know from section [Playing Pattern](sec-playing-pattern), we can use a ``Pbind`` to play an event pattern.
In fact we can play it on a specific clock!

The following code should generate the same result.
Play around with the ``tempo`` of the ``TempClock`` and listen how the sound changes.
You can change the ``tempo`` by evaluating the last line.

```isc
(
t = TempoClock(2);

Pbind( 
    \instrument, \default,
    \dur, 1,
    \sustain, 0.2,
    \freq, Pwhite(40, 80, inf).midicps,
).play(t);
)

t.tempo = 5
```