---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(sec-clocks)=
# Clocks

A *clock* is a timed scheduler.
It gives the user the ability to schedule certain events at a specific time.
If a clock is started, it ticks endlessly in the background.
There are three different types of clocks: 

+ [SystemClock](https://doc.sccode.org/Classes/SystemClock.html),
+ [AppClock](https://doc.sccode.org/Classes/AppClock.html), and
+ [TempClock](https://doc.sccode.org/Classes/TempoClock.html).

A [SystemClock](https://doc.sccode.org/Classes/SystemClock.html) is more accurate than [AppClock](https://doc.sccode.org/Classes/AppClock.html), but it cannot call GUI primitives.
[TempClock](https://doc.sccode.org/Classes/TempoClock.html), on the other hand, does not work in seconds but in beats per second (bps).
It is the clock that is supposed to be used to schedule musical events.

## Basics

Let us define [TempClock](https://doc.sccode.org/Classes/TempoClock.html) that runs at 120 bpm, i.e., 2 beats per seconds, and lets post ``'Hello!'`` at every beat:

```isc
(
t = TempoClock(2);

// return 1 to continuously re-schedule the function.
t.sched(0, {'Hello'.postln; 1}); 
)
```

[TempClock](https://doc.sccode.org/Classes/TempoClock.html) keeps track of time and allows tasks to be scheduled at some point in time in the future (``sched``, ``schedAbs`` or ``play``).
``sched`` schedules relative to the time of calling while ``schedAbs`` schedules at an absolute time.
We can get its current beat by calling ``t.beats`` and its next bar by calling ``t.nextBar``.
By default a clock uses 4 beats per bar.
When the time at which a task was scheduled is up, the task is awoken, i.e., its ``awake`` method is evaluated.
In case of a [Function](sec-functions), ``awake`` calls ``value`` and in case of a [Routine](https://doc.sccode.org/Classes/Routine.html) it calls ``next``.
If the value returned by the function is a number, the task is automatically **re-scheduled** at the time equal to its last scheduled time plus the return value (in beats).

## Scheduling Synths

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

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/clock-schedule-rand.mp3'
ipd.Audio(audio_path)
```

## Scheduling Pbinds

Using a *gated* envelope makes it difficult to use a plain scheduler since we have to set the gate of the synth to ``0`` manually, i.e. by another scheduled function.
For example, the ``default`` instrument is consists of a gated envelople.
The following ugly code plays it buy using a [TempClock](https://doc.sccode.org/Classes/TempoClock.html).

```isc
(
t = TempoClock(2);
~synth = nil;
~dur = 1;

// schedule the synth
t.sched(0, {~synth = Synth(\default, [\freq, rrand(40, 80).midicps]); 1});

// and ~dur beats afterwards its termination
t.sched(~dur, {~synth.set(\gate, 0); 1});
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/clock-gated-rand.mp3'
ipd.Audio(audio_path)
```

But as we know from section [Playing Pattern](sec-playing-pattern), we can use a [Pbind](https://doc.sccode.org/Classes/Pbind.html) to play an event pattern.
In fact we can play it on a specific clock!

The following code should generate the same result.
Play around with the ``tempo`` of the [TempClock](https://doc.sccode.org/Classes/TempoClock.html) and listen how the sound changes.
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

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/clock-pbind-rand.mp3'
ipd.Audio(audio_path)
```

We can also change the tempo of the default clock which is used whenever we do not specify a certain clock.

```isc
// default clock set to 120 beats per minute (bpm)
TempoClock.default.tempo = 120/60;
```

## Quantizing Pbinds

Now let's assume we want a type of music with a different number of beats per bar.
Furthermore, we want multiple [Pbinds](https://doc.sccode.org/Classes/Pbind.html) to be played synchroniously.
If we naively do this, we most likely will not achieve the desired result:

```isc
(
p = Pbind(
    \instrument, \default,
    \dur, 0.5,
    \degree, Pseq([5, 7, 8, 9], inf),
);
)

(
q = Pbind(
    \instrument, \default,
    \dur, 0.25,
    \degree, Pseq([1, 5, 7, 9], inf),
);
)

x = p.play;
x.stop;

y = q.play;
y.stop;
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/sched-async.mp3'
ipd.Audio(audio_path)
```

However, we can use the a [TempoClock](https://doc.sccode.org/Classes/TempoClock.html) to manage the **quantized** scheduling!
Let us assume we want 120 beats per second and 3 beats per bar and a clock that is permanent, i.e. does not die when we press ``CMD + .``, the following works:

```isc
t = TempoClock(120/60).permanent_(true).schedAbs(0, {t.beatsPerBar_(3)} );
```

To schedule our event players on the clock, we use [Quant](https://doc.sccode.org/Classes/Quant.html) for quantization. 
The parameter ``quant`` determines when the pattern or routine will start. 
Specifically, it begins at the next integer multiple of this number. 
If the ``quant`` value is negative, it indicates scheduling a certain number of bars into the future.
The ``phase`` parameter serves as an offset to adjust the scheduling time, typically within the bar. 
A value of +1 means the event will be scheduled one beat later, while -1 schedules it one beat earlier.
There's also a third argument, ``timeingOffset``, which I'm not using here. 
This parameter allows patterns to run slightly ahead of their actual sounding time on the clock. This feature is particularly useful for controlling the execution order of different threads. 
By computing values slightly ahead of time, ``timeingOffset`` can be beneficial, especially when one pattern is dependent on the data from another pattern. 
This anticipatory calculation ensures smooth and coordinated pattern execution.

```isc
t = TempoClock(120/60).permanent_(true).schedAbs(0, {t.beatsPerBar_(3)} );

x = p.play(t, quant: Quant(quant: 4, phase: -1));
x.stop;

y = q.play(t, quant: Quant(quant: 4, phase: 1.5));
y.stop;
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/sched-sync.mp3'
ipd.Audio(audio_path)
```

As you can hear both event players are in sync and run at 120 bpm. Instead of writing 

```isc
quant: Quant(quant: 4, phase: 1.5)
```

we can use the following shorthand

```isc
quant: [4, 1.5]
```
If one wants to change the beats per bar during a performance, we can do it also via the scheduling:

```isc
t.sched(t.nextBar, { t.beatsPerBar_(4) });
```

Remember, the ``\dur`` parameter in this context is defined in terms of beats, not seconds. 
Additionally, it's possible to manipulate the clock while a pattern is playing. 
For example, if we want to increase the tempo during a performance, we can achieve this by using a function. 
This function takes a few arguments: a clock, a new tempo, and the number of beats over which the change should occur.
In this particular scenario, I'm opting to use ``schedAbs``  instead of ``sched``. 
Therefore, I have to provide the beats of the next bar, allowing for a more precise and timely adjustment of the tempo. 
This technique is an effective way to dynamically alter the pace of the music, adding an element of flexibility and responsiveness to the performance.

```isc
t = TempoClock(120/60).permanent_(true).schedAbs(0, {t.beatsPerBar_(3)} );

x = p.play(t, quant: Quant(quant: 4, phase: -1));
x.stop;

y = q.play(t, quant: Quant(quant: 4, phase: 1.5));
y.stop;

(
~changeTempo = {
    arg newTempo, numBeats, clock;
    var tempos = Array.interpolation(numBeats, clock.tempo, newTempo);
    var i = 0;
    clock.schedAbs(clock.nextBar, {
        clock.tempo_(tempos[i]);
        i = i + 1; 
        if(i < numBeats){1}{\done};
    });	
};
)

~changeTempo.(60/60, 8, t);
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/sched-dynamic-bpm.mp3'
ipd.Audio(audio_path)
```

