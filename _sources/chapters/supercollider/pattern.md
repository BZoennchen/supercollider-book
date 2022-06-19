(sec-pattern)=
# Playing Pattern

[UGens](sec-ugens) are the basic building blocks for our synth, i.e., instruments, i.e., sound.
But having instruments is not enough, we also want to play them!
We want to create rhythms, textures, and melodies.

There are different ways to do this.
First of all, as mentioned in [The Ecosystem](sec-ecosystem), there are other software packages such as [Sonic Pi](https://sonic-pi.net/), [TidalCycle](https://tidalcycles.org/) or [FoxDot](https://foxdot.org/) which are designed to play synths and samples.
[Sonic Pi](https://sonic-pi.net/) goes the imperative way combining iteration and threading in a single concept called ``live_loops``.
These threaded loops can be sync with other loops and they follow a strickt timing concept.
[FoxDot](https://foxdot.org/) uses the concept of players.
Each player can play a synth on repeat and is synchronized to a clock.
[TidalCycle](https://tidalcycles.org/) went the functional route.
It also uses players but lets the user manipulate a signal in a functional way.
Each of these tools offer a distinct language and therefore a way of thinking.

However, [SuperCollider (SC)](https://supercollider.github.io/) offers its own amazing and powerful interface to compose a musical piece.
Within the language we can use plain iteration and threading.
Secondly we can use so called [Pattern](https://doc.sccode.org/Classes/Pattern.html), [Streams](https://doc.sccode.org/Classes/Stream.html) and [Events](https://doc.sccode.org/Classes/Event.html) to abstract most of the technical burden away!

Later we will see how we can use the live programming interface to further enhance our ability to create rythms and melodic textures on the fly.

## The Instrument and its Artist

In my opinion, there is no clear separation between the world of ideas and the world of materials and tools.
Philosophically speaking, the tools we use, influence how we think about the world.
And our thoughts lead to new tools, new technologies.
Tools, like pen and paper, instruments, a hammer, programming languages or frameworks, and even our hands, act as interpreters.
They translate our thoughts into actions that change the physical world around us.

However, this interaction is not a one-way street where we, the artist, enforce ideas onto the instrument.
Instead, the instrument influences our ideas by limiting our space of possibilities.
In fact, our brain does the same!
It limits what we can perceive such that structure can build up within our minds.
Our brain is a complexity reducing organ that generates reality by differentiation and abstraction.
The overwhelming stream of the concrete is filtered and enriched with meaning.
But all this happens automatically.
And before we start thinking about our brain, we use it.

In the realm of (other) tools, it seems to be similar.
Before we think about the being of a hammer, we use it.
Furthermore, a hammer is always connected to other things, for example, a nail or a wooden chair.

A tool or an instrument provides us with the means of expression. 
It defines the space of possibilities.
By limitations, it paradoxically opens up our imagination.

I think limitation is one the most unterestimated requirements for artistic creation.
If everything is possible nothing will be accomplished.
Too much freedom can be a burden for the artist.
Without boundaries, the complexity of the concrete, the language of the instrument, can not be conquered.
If we can create everything, we become unable to express anything.

On the other hand, too strict limitations lead to repetition.
If the space of possibilities is too narrow, the artist becomes superfluous.
We encounter the great enemy of any creative process: boredom!

Consequently, there is no clear optimal amount of limitations, i.e., space of possibilities.
But changing the space from time to time can be a great source of inspiration.

Therefore, to find out what space of possibilities you are looking for, I highly recommend that you check out all available tools and if none suits your needs you may want to build your own! 
Building instruments to express ourselves is one of those wonderful acts a programmer can do!
Of course, we will always stay in some limited super-space of possibilities defined by the underlying machine we are working on.
Our machines are able to compute anything that is *Turing-computable*, i.e., (up to this day) everything that we can compute in general.
However, we are limited by time and space.
On the computer, this translates to computational time and space complexities.
If a computation consumes our lifetime it is unpractical.

Now let us talk about the space of possibilities that ``sclang`` offers.

## Pattern and Streams

### Streams

A [Stream](https://doc.sccode.org/Classes/Stream.html) is basically a series of elements that you can obtain in a **lazy** fashion.
It is very similar to an ``Array`` with the difference that it is **lazy**.
Laziness means that instead of holding all values of the ``Stream`` in-memory (like an ``Array`` does) values are generated on demand by a function.
Therefore, a ``Stream`` can offer infinitely many values which is impossible for an ``Array``!
For example, we can define a function that gives us all integers.

```isc
~val = 0;
f = {~val = ~val + 1; ~val;};
f.();
```

If we evaluate the last line multiple times, we get 1, 2, 3, and so on.
This is basically an infinite stream of values.
We can use [FuncStream](https://doc.sccode.org/Classes/FuncStream.html) to create a ``Stream`` of integers.
Then we can call ``next`` on the ``Stream`` to get the next value of it.

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

If a ``Stream`` runs out of values, it returns ``nil``.

In ``sclang`` everything is an [Object](https://doc.sccode.org/Classes/Object.html) and the class ``Object`` defines ``next`` to return the object itself.
Thus every object can be viewed as a ``Stream`` that streams itself.
Consequently, almost everything can be viewed as a ``Stream``.

```isc
// a number is a stream returning itself
5.next();  // 5
```

### Pattern

[Pattern](https://doc.sccode.org/Classes/Pattern.html) is an abstract class that is the base for the patterns library. 
The classes of this library form a rich and concise score language for music.
Patterns are the stateless blueprint of streams.
Calling ``asStream`` on a ``Pattern`` transforms it into a ``Stream``.
As already mentioned, all simple objects respond to this interface, by returning themselves.
Consequently, most objects are ``Pattern`` that define a ``Stream`` that represents an infinite sequence of that object.

```{admonition} Pattern and Streams
:name: remark-pattern-and-streams
:class: remark
Similar to classes and objects, ``Pattern`` is a blueprint for ``Streams``.
```

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
``Prand`` chooses from an ``Array`` a random element.
In the above example, we combine both ``Pattern``.
``Pseq`` gets an ``Array`` consisting of two ``Prand``-pattern.
By the parameter ``repeats: 2`` we configure ``Pseq`` to go over ``list`` twice.

Calling ``next`` on a ``Stream`` defined by ``Pattern`` consisting of ``Pattern``, will lead to a recursive evaluation, that is, ``next`` is called as long as the return value is another ``Stream``.
Here is another example where we generate three melodies noted by midi notes which are randomly but weighted chosen and transformed into frequencies.

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
Well, they can be combined and they can be manipulated by all regular math functions if they return numbers.
In the above example, we multiply the ``Pseq``-pattern by 10 (which by calling ``asStream`` returns a ``BinaryOpStream``).
They are really powerful to build complex ``Streams``.
Therefore, they offer us a very comfortable way of building melodies without dealing with threads directly.
The ``Pattern`` library abstracts the task of thread creation, synchronization, joining, termination and clean up away.

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

The difference between ``Pattern`` and (its) ``Stream`` becomes clear if we think in musical terms.
A composition is a specific ``Pattern`` and a performance is a ``Stream`` of that ``Pattern``. 
Playing a piano can be seen as a ``Stream`` of specific [Events](https://doc.sccode.org/Classes/Event.html).
We press some keys, with some velocity, for some duration, then we might wait for some amount of time and press the next keys.

(sec-playing-events)=
### Playing Events

[Pbind](https://doc.sccode.org/Classes/Pbind.html) is an important ``Pattern``.
Its streams, stream (musical) ``Events``. 
It models this process by discrete events.

```{admonition} Combining Streams
:name: remark-pbind
:class: remark
``Pbind`` combines several *value streams* into *one event stream*.
```

We define a duration ``dur``, and the parameters of our instrument and the instrument itself, i.e., the synth.
A ``Pbind`` can then be played by calling ``play`` on it.
The method returns an [EventStreamPlayer](https://doc.sccode.org/Classes/EventStreamPlayer.html).

``Events`` extend [Environments](https://doc.sccode.org/Classes/Environment.html).
``Environments`` manage namespaces.
They are very similar to hash maps, hash tables, or a ``Python`` dictionary.
For example, calling a function will create a new local function-``Environment``.
``Environments`` map names to variables and functions.

```isc
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

Here we define an ``Environment`` with three variables ``a``, ``b``, ``c`` and a function ``add``.
``~a`` is in fact an abbreviation for ``currentEnvironment.at(\a)`` and `` ~a = 100`` for ``currentEnvironment.put(\a, 100)``.
As you can see we already worked with ``Environments`` without knowing them.

We are not so much interested in ``Environments`` but ``Events`` and they can be defined using a far more compact syntax, i.e., we just use round brackets:

```isc
(
var event = (\dur: 1, \freq: 600);
event[\dur].postln; // 1
event.play;
)
```

## Playing Events

What is going on here?
We actually can hear a sound???
Well if you look at the print window, you can see all the predefined variables/symbols of the ``Environment``/``Event``.
In my case, this is equal to

```isc
'instrument': default, 
'msgFunc': a Function, 
'dur': 1, 
'amp': 0.1, 
'server': localhost, 
'sustain': 0.8, 
'isPlaying': true, 
'freq': 600.0, 
'hasGate': true, 
'id': [ 1869 ]
```

Everything that we have to define to play a sound, such as, ``amp``, ``instrument``, ``server`` is predefined.
The method ``play`` uses predefined values if they are missing in the event we want to play.
The predefined values are stored in class variables, that is, variables that are shared by all events.
They are split into partial events:

```isc
Event.partialEvents.postln;
```

### The Default Instrument

The ``instrument`` is a ``default`` instrument that is built into SuperCollider.
We can find it in the source code of the class [Event](https://doc.sccode.org/Classes/Event.html).
Let us have a look.

```isc
SynthDef(\default, { 
    arg out=0, freq=440, amp=0.1, pan=0, gate=1;
    var z;
    z = LPF.ar(
        Mix.new(VarSaw.ar(freq + [0, Rand(-0.4,0.0), Rand(0.0,0.4)], 0, 0.3, 0.3)),
        XLine.kr(Rand(4000,5000), Rand(2500,3200), 1)
    ) * Linen.kr(gate, 0.01, 0.7, 0.3, 2);
    OffsetOut.ar(out, Pan2.ar(z, pan, amp));
}
```

It is a filtered randomly distorted [sawtooth wave](sec-sawtooth-wave) with a percussive envelope.
The cutoff frequency of the low pass filter decreases over the time span of 1 second and is initialized with random values.

### Value Conversions

In the [Event](https://doc.sccode.org/Classes/Event.html) class, we can also find the code that actually ``plays`` an event.
The method of interest is called ``makeParentEvents``.
It is very lengthy and you do not have to understand it.
But if you are interested in what is exactly happening, it is a good starting point.
Furthermore, it gives us information about all the default values.
These values are also discussed in the official [pattern guide](https://doc.sccode.org/Tutorials/A-Practical-Guide/PG_07_Value_Conversions.html).

SuperCollider provides the specification of the different parameters that influence the scheduling and the play of a single synth.
But it provides different ways to express the same thing and converts it to a specific thing.
For example, a synth only knows frequencies but you do not have to think in terms of frequencies.
Instead, you can think in terms of midi notes and the event player will transform your midi note into the respective frequency.
Of course, defining midi note and frequency does not really make sense.
SuperCollider will always take the most concrete value, i.e., frequency over the midi note.

#### Timing

First of all, time is measured in beats per second (bps), and events are scheduled on a specific [TempoClock](https://doc.sccode.org/Tutorials/Getting-Started/14-Scheduling-Events.html) that runs at a specific bps.
The default clock runs at 60 beats per second.
We will discuss later how we can change this.

Let us look at the parameters determining the timing of an event.
Let $t_e$ be the start time of the event $e$ (scheduled on our clock).
Then $t_e + \Delta t_e$ is the end time of $e$, i.e., the start time of the next scheduled event.

Furthermore, at $t_e + \Delta t_{e_s}$ the sustain ends and the decay of the sound begins.
$\Delta t_e$ is equal to ``delta = dur * stretch`` and $\Delta t_{e_s}$ is equal to ``sustain``.
The duration ``dur`` is stretched by a factor ``stretch``.
Of course, the sound of the event $e$ can last longer than $\Delta t_e$, that is,

\begin{equation*}
   \Delta t_{e_s} >\Delta t_e
\end{equation*}

is feasible.

We have the following parameters with their respective default values:

```isc
tempo: nil,
dur: 1.0,
stretch: 1.0,
legato: 0.8,
sustain: { ~dur * ~legato * ~stretch },
lag: 0.0,
strum: 0.0,
strumEndsTogether: false
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

```{figure} ../../figs/supercollider/pattern/event-timing.png
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

#### Pitch

As already mentioned, we do not have to work with frequencies.
In fact, there are many ways to define the pitch of the event, i.e., the played synth and many of them are more relevant for musicians who are used to them.
I am not completely familiar with all the concepts so I will not provide a full picture.

One of the concepts are the so-called midi notes.
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

#### Amplitude

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

### Custom Instrument

Of course, we can use our own ``SynthDef``, i.e., synth.
To use all the nice predefined parameters, our ``SynthDef`` has to use the correct arguments and we have to name them as intended.

For the rest of this section we work with the following synth:

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


For example, the frequency should be called ``freq``, if we want to be able to sustain the sound we should use a sustaining envelope with a gate argument called ``gate`` and the amplitude should be defined by ``amp``.

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
dur: 1.0,
stretch: 1.0,
legato: 0.8,
sustain: { ~dur * ~legato * ~stretch },
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

## Playing Pbinds
Let us have a look.

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

### Playing EventStreams

``Pbind`` is a special ``Pattern`` that generates a ``Stream`` that spits out ``Events``.
By using the ``play`` method on the ``Pbind`` pattern, we play all the events the event stream gives us.
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

Now you might ask: how do the events actually look like?
As already mentioned each event is filled with default arguments if they are not defined.
For each defined argument, in our case ``instrument``, ``freq``, ``dur``, and ``legato`` the method ``next`` is called on the value referenced by the corresponding name.
As we learned, if this value is a number, the number itself is returned.
If it is a pattern, it was already transformed into a stream when ``play`` was called and will return what the recursive evaluation of ``next`` gives us.

### Argument Dependence

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

### Cascading Pbinds

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

Ok, so we can define a pattern of events, i.e. a ``Pbind`` and play it.
But would it not be nice to change the pattern while playing it?
SuperCollider supports live programming via its powerful [Just In Time programming library (JITLib)](https://doc.sccode.org/Overviews/JITLib.html).
I will discuss live programming in detail in section [Live Coding](sec-live-coding) but here I want to mention the [Pbindef](https://doc.sccode.org/Classes/Pbindef.html) class.

``Pbindef`` keeps a reference to a ``Pbind`` in which single keys can be replaced.
It plays on when the old stream ended and a new stream is set and schedules the changes to the beat.
Basically this means that we can:

1. change our pattern
2. re-evaluate the code 

and the change will appear soon after without ever stopping the pattern.
The only difference to ``Pbind`` is that a ``Pbindef`` requires a unique name.
Use the following ``Pbindef``, change the frequencies and re-evaluate the code.
Listen what happens!

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

Behind the scenes SuperCollider's event player helps us transforming different values into other values.
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

I use two ``SynthDefs`` for the following examples.
One simple beep generated by a sine wave and a percussive drum-like synth.
TODO!
