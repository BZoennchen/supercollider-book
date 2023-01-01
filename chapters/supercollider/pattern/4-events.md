(sec-playing-events)=
# Musical Event

[Pbind](https://doc.sccode.org/Classes/Pbind.html) is an important ``Pattern``.
It models the process of playing an instrument by discrete events in time, realizing a discrete event simulation (DES).
It streams (musical) [Events](https://doc.sccode.org/Classes/Event.html). 

```{admonition} Combining Streams
:name: remark-pbind
:class: remark
[Pbind](https://doc.sccode.org/Classes/Pbind.html) combines several *value streams* into *one event stream*.
```

We define a duration ``dur``, the frequency ``freq``, note ``note`` or ``midinote`` and the ``instrument`` we wanna play, i.e., the synth.
A ``Pbind`` can then be played by calling ``play`` on it.
The method returns an [EventStreamPlayer](https://doc.sccode.org/Classes/EventStreamPlayer.html).

``Events`` extend [Environments](https://doc.sccode.org/Classes/Environment.html).
``Environments`` manage namespaces.
They are similar to hash maps, hash tables, or a ``Python`` dictionary, i.e., a collection where you can access its elements by name.
For example, calling a function will create a new local function environment.
Environments map names to variables and functions.

```supercollider
(
var env = Environment.make({
    ~a = 100;
    ~b = 200;
    ~c = 300;
    ~add = {arg x, y; x + y;};
});
env.postln;
env[\a]; // 100
env[\add].(3,13); // 16
)
```

Here we define an *environment* with three variables ``a``, ``b``, ``c`` and a function ``add``.
``~a`` is in fact an abbreviation for ``currentEnvironment.at(\a)`` and `` ~a = 100`` for ``currentEnvironment.put(\a, 100)``.
As you can see we already worked with *environments* without knowing them.

We are not so much interested in *environments* but their subclass ``Event``.
*Events* can be defined using a far more compact syntax.
We just use round brackets:

```isc
(
var event = (\dur: 1, \freq: 600); // define an event
event[\dur].postln; // 1
event.play; // play the event
)
```

What is going on here?
We actually can hear a sound!
Well, if you look at the post window, you can see all the predefined variables/symbols of the *environment/event*.
In my case, this is equal to:

```isc
'instrument': default, 
'msgFunc': {}, 
'dur': 1, 
'amp': 0.1, 
'server': localhost, 
'sustain': 0.8, 
'isPlaying': true, 
'freq': 600.0, 
'hasGate': true, 
'id': [ 1869 ]
```

Everything we have to define to play a sound, such as, ``amp``, ``instrument``, ``server`` is predefined.
The ``play`` method uses predefined values if they are missing in the event we want to play.
The predefined values are stored in class variables, i.e., variables that are shared by all events.
They are split into partial events:

```isc
Event.partialEvents.postln;
```

(sec-default-instrument)=
## The Default Instrument

The ``instrument`` is a *default* instrument called ``\default`` that is built into SuperCollider.
We can find it in the source code of the [Event](https://doc.sccode.org/Classes/Event.html) class.
Let us have a look:

```isc
SynthDef(\default, {
    arg out=0, freq=440, amp=0.1, pan=0, gate=1;
    var z;
    z = LPF.ar(
        Mix.new(
            VarSaw.ar(
                freq + [0, Rand(-0.4,0.0), Rand(0.0,0.4)], // freq
                0, // iphase
                0.3, // width
                0.3) // mul
        ),
        XLine.kr(Rand(4000,5000), Rand(2500,3200), 1) // cutoff
    ) * Linen.kr(gate, 0.01, 0.7, 0.3, 2); // * envelope
    OffsetOut.ar(out, Pan2.ar(z, pan, amp));
}
```

It is a filtered randomly distorted [sawtooth wave](sec-sawtooth-wave) with variable duty multiplied by a percussive envelope.
Two slightly detuned waves are generated and mixed a single channel which is then panned into both speakers.

The cutoff frequency of the [low pass filter](sec-lowpass-filter) decreases over the time span of 1 second and is initialized with random values.
By decreasing the cutoff frequency over time, high frequencies die out faster which is natural.

(sec-value-conversion)=
## Value Conversions

In the [Event](https://doc.sccode.org/Classes/Event.html) class, we can also find the code that actually ``plays`` an event.
The method of interest is called ``makeParentEvents``.
It is very lengthy, and you do not have to understand it.
But if you are interested in what is precisely happening, it is a good starting point.
Furthermore, it gives us information about all the default values.
These values are also discussed in the official [pattern guide](https://doc.sccode.org/Tutorials/A-Practical-Guide/PG_07_Value_Conversions.html).

SuperCollider provides the specification of the different parameters that influence the scheduling and the play of a single synth.
But it provides different ways to express the same thing and converts it to a specific item.
For example, a synth only knows frequencies, but you do not have to think in terms of frequencies.
Instead, you can think in terms of midi notes, and the event player will transform your midi note into the respective frequency.
Of course, defining midi note and simultaneously frequency does not really make sense.
SuperCollider will always take the most substantial value, e.g., frequency over the midi note.

### Timing

First of all, time is measured in beats per second (bps), and events are scheduled on a specific [TempoClock](https://doc.sccode.org/Tutorials/Getting-Started/14-Scheduling-Events.html) that runs at a particular bps.
The default clock runs at 60 beats per second.
We will discuss later how we can change this.

Let us look at the parameters determining the timing of an event.
Let $t_e$ be the start time of the event $e$ (scheduled on our clock).
Then $t_e + \Delta t_e$ is the end time of $e$, i.e., the start time of the next scheduled event.

Furthermore, at $t_e + \Delta t_{e_s}$ the sustain ends and the decay of the sound begins.
$\Delta t_e$ is equal to ``delta = dur * stretch`` and $\Delta t_{e_s}$ is equal to ``sustain``.
The duration ``dur`` is stretched by a factor ``stretch``.
Of course, the sound of the event $e$ can last longer than $\Delta t_e$, i.e.,

\begin{equation*}
   \Delta t_{e_s} >\Delta t_e
\end{equation*}

is feasible.
We have the following parameters with their respective default values:

```isc
'tempo': nil,
'dur': 1.0,
'stretch': 1.0,
'legato': 0.8,
'sustain': { ~dur * ~legato * ~stretch },
'lag': 0.0,
'strum': 0.0,
'strumEndsTogether': false
```

```{admonition} Scheduling Influencer
:name: remark-scheduling-influencer
:class: remark
``dur``, ``stretch``, ``delta`` and ``lag`` do not influence the sound generated by the event but influences the scheduling of events!
```

We can set either ``sustain`` or ``legato`` but it does not really make sense to define them both because if we set ``sustain``, then ``legato`` has no effect.
This is not true for the duration ``dur``, since it is not only used to compute ``sustain``.

```{admonition} Sound Influencer
:name: remark-sound-influencer
:class: remark
``legato`` and ``sustain`` do not influence the scheduling but the sound generated by the event!
```

What does ``lag`` mean?
Well, ``lag`` ($\Delta t_l$) is a delay for the scheduler, i.e., scheduled events *lag* behind.
The effect is that the sound generated by consecutive events will just start *lag* bps later.

```{figure} ../../../figs/supercollider/pattern/event-timing.png
---
width: 400px
name: fig-event-timing
---
Example of the timings of three scheduled events.
```

Let $e_1, \ldots, e_m$ be the $m$ scheduled events.
Then for all $1 \leq i < m$

\begin{equation*}
    t_{e_{i+1}} = t_{e_i} + \Delta t_{e_i} = t_l + \Delta t_{e_1} + \ldots + \Delta t_{e_{i}}
\end{equation*}

holds.

```isc
//2-second pause before the event is played
(\instrument: \default, \dur: 0.2, \freq: 300, \lag: 2).play;
```

We will see the effect of the different timing parameters later on when we actually play a stream of events.

### Pitch

As already mentioned, we do not have to work with frequencies.
In fact, there are many ways to define the pitch of the event, i.e., the played synth, and many of them are more relevant for musicians who are used to them.
I am not entirely familiar with all the concepts, so I will not provide a complete picture.

One of the concepts is the so-called midi notes.
This system assigns ascending numbers to the keys of a piano.

```isc
(\instrument: \default, \dur: 0.2, \amp: 0.5, \midinote: 60).play;
```

The function/message ``midicps`` transforms a midi note into its frequency.

```isc
60.midicps // 261.6255653006
(\instrument: \default, \dur: 0.2, \amp: 0.5, \freq: 60.midicps).play;
```

We can also work with a scale and construct from it a note using its degree and its octave.

```isc
(\instrument: \default, \dur: 0.2, \amp: 0.5, \scale: Scale.major, \degree: 3, \octave: 4).play;
```

``stepsPerOctave`` defines how many ``note`` units map onto the octave. 
It supports non-12ET temperaments.
For the default of 12 ``stepsPerOctave`` (western music).

```isc
(
(\instrument: \default, \dur: 0.2, \amp: 0.5, 
    \scale: [0, 3, 6, 8, 11, 14, 17], 
    \degree: 1, 
    \octave: 4,
    \stepsPerOctave: 12,
    \mtranspose: 3
).play
)
```

we can compute the midi note by the following formula

```isc
\stepsPerOctave * \octave + \scale.at(\degree + \mtranspose)
```

i.e.

\begin{equation*}
    12 \cdot 4 + 11 = 59
\end{equation*}

This does not work if we introduce other values for ``stepsPerOctave`` or manipulate the ``octaveRatio``.
If you are interested in the exact computation, have a look at the source code of the ``Event`` class.

### Amplitude

The amplitude can be defined by either ``amp`` or ``db`` (decibel).
``amp`` has a higher prioritization.

Both of the following code lines generate a sound of equal amplitude.

```isc
(\dur: 0.1, \freq: 600, \amp: -3.dbamp).play;
(\dur: 0.1, \freq: 600, \db: -3).play;
```

```{admonition} Amplitude in Decibel
:name: remark-amp-in-db
:class: remark
``\db: 0`` equals ``\amp: 1.0``.
```

## Custom Instrument

Of course, we can use our own ``SynthDef``, i.e., custom instrument.
To use all the excellent predefined parameters, our ``SynthDef`` has to use the correct arguments, and we have to name them as intended.
For the rest of this section, we work with the following synth:

```isc
(
SynthDef(\snare,{arg hcutoff = 9000, lcutoff = 5000, amp = 1.4;
    var env, hat, bass, sig, cutoff = 5000;
    env = Env.perc(0.01, 0.15).kr(doneAction: Done.freeSelf);
    hat = {PinkNoise.ar()}!2;
    hat = HPF.ar(hat, XLine.ar(lcutoff/4, lcutoff, 0.2));
    hat = LPF.ar(hat, hcutoff);
    bass = LFTri.ar(XLine.kr(150, 10, 0.21))*0.2;
    sig = (hat + bass) * env * amp;
    Out.ar(0, sig);
}).add;

SynthDef(\saw, {arg freq = 600, amp = 0.8, gate = 1;
    var sig, env;
    env = EnvGen.kr(
        Env.asr(attackTime: 0.01, sustainLevel: 1.0, releaseTime: 1.4), 
        gate: gate, 
        doneAction: Done.freeSelf);
	sig = LPF.ar(LFSaw.ar([freq, freq*1.004]), XLine.ar(freq*2, freq/4, 0.2) + LFNoise2.kr(90).bipolar(freq/10));
    sig = sig * env * amp;
    Out.ar(0, sig);
}).add;
)

Synth(\snare)
~snare = Synth(\saw)
~snare.set(\gate, 0)
```

Note that the frequency argument should be called ``freq``, the amplitude argument should be called ``amp, `` and the gate should be called ``gate``.
This is crucial.
Otherwise, we can not make use of the full potential of SuperCollider's pattern library.

```isc
(
var event = (\instrument: \saw, \dur: 0.2, \freq: 300);
event.play;
)
```

First, we add a very simple synth, then we play it for a duration of ``0.2`` beats per second (bps).

If we look closely, we can observe that there is a ``sustain`` argument that is set to 80 percent of the duration, i.e. to ``0.16`` beats per seconds.
This is because the default values of our arguments are defined as follows.

```isc
'dur': 1.0,
'stretch': 1.0,
'legato': 0.8,
'sustain': { ~dur * ~legato * ~stretch },
```

As already mentioned, ``sustain`` is the time after the ``gate`` within our synth is triggered!
We can change this default behavior by setting our own ``sustain`` value which overrides ``legato``.

```isc
(
var event = (\instrument: \saw, \sustain: 0.1, \dur: 0.2, \freq: 300);
event.play;
)
```

```{admonition} Difference between Duration and Sustain
:name: remark-overlapping-sound
:class: remark
The duration ``dur`` is the elapsed time after the next event is scheduled while ``sustain`` is the time after the ``gate`` of the synth is triggered. If the sound sustains longer than ``dur`` we get overlapping sounds.
```

This seems to make the ``dur`` argument irrelevant.
However, we need ``dur`` if we not only play one event but a ``Stream`` of events!
Remember, ``dur`` influences the scheduler of our musical events.
We can see the effect if we play a stream of events.
