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

(sec-synths)=
# SC Synthesizers

The concept of synth definitions and synth is central to SuperCollider.
Everything is built around this fundamental concept.
It can be confusing for beginners because there is a big difference between a synth as we know it in the real world and an instance of [Synth](https://doc.sccode.org/Classes/Synth.html).

## Definition

In the real world, a synth is an instrument that can be played.
However, in ``sclang``, we distinguish between the instrument (as a potential/thing) and the played instrument (as a process).
While the thing is an instance of [SynthDef](https://doc.sccode.org/Classes/SynthDef.html), the process (an executed [signal-flow graph (SFG)](https://en.wikipedia.org/wiki/Signal-flow_graph)) is an instance of [Synth](https://doc.sccode.org/Classes/Synth.html).
If we instanciate a [Synth](https://doc.sccode.org/Classes/Synth.html), defined by a specific [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) and its arguments, the signal processing begins and if we destroy the [Synth](https://doc.sccode.org/Classes/Synth.html) it stops.

Instead of introducing a new class for each new instrument which would lead to thousand of classes, each instrument is represented by a function, more precisely by *a unit generator graph function* that realizes *a signal-flow-graph (SFG)*.
``sclang`` borrows this concept from functional programming languages.
The SFG ultimately defines the instrument.
At the same time, the synth definition provides an interface to play it.
We generate synths by calling the defining function with different arguments.

```{admonition} SynthDef
:name: def-synth-def
:class: definition
An instance of [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) represents a factory of a parameterizable signal-flow-graph.
The graph can be executed (as [Synth](https://doc.sccode.org/Classes/Synth.html) with different arguments) on the audio server.
```

From the perspective of a musician, a synth definition is a parameterizable description of a piece of sound.
A synth, on the other hand, is the process of playing that piece of sound with specific possibly modulated arguments (frequency, loudness, velocity, etc.).
From a software developer's perspective, a synth definition is a factory that generates synths following its internal description defined by a function representing a signal-flow graph.

A [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) object encapsulates the server-side representation of a synth definition and provides methods for creating new [Synth](https://doc.sccode.org/Classes/Synth.html) objects on the server.
It abstracts away all the low level communication (via [OSC](sec-osc)) between the client and the audio server.
Furthermore, a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) object can be serialized to the disk and streamed via the network to distant audio servers.
[SynthDefs](https://doc.sccode.org/Classes/SynthDef.html) are nothing more than compact representations of signal-flow graphs written down in text.

```{admonition} Synth
:name: def-synth
:class: definition
A [Synth](https://doc.sccode.org/Classes/Synth.html) is a representation of an executed signal-flow-graph.
It is the process that generates sound via the audio server.
```

## Workflow

We use ``sclang`` to define a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html).
It is defined on the client, and we must send it to the audio server.
To generate sound, we have to tell the server to create a synth of one of its known [SynthDefs](https://doc.sccode.org/Classes/SynthDef.html).

The normal workflow goes as follows:

1. define (all) your [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) via ``sclang``
2. add them (all) to the audio sever **scsynth**
3. create one or multiple synth on the server
4. remove your synths from the server

```isc
(
// (1) define the SynthDef
var synthdef = SynthDef(\sine_beep, {
    arg freq = 440, amp = 0.5;
    var sig, env;
    env = Env([0,1,0], [0.01, 0.4], [5,-5]).ar(doneAction: Done.freeSelf);
    sig = SinOsc.ar(freq: freq, mul: amp) * env!2;
    Out.ar(0, sig);
});

// (2) add it to the audio server scsynth
synthdef.add;
)

// (3) use it by creating Synth of the SynthDef
Synth(\sine_beep, [freq: 800, amp: 0.4]);

// (4) the synth removes itself because we specied doneAction: Done.freeSelf
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/sine-beep.mp3'
ipd.Audio(audio_path)
```

Note that adding a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) to the server takes time.
Therefore, we can not execute the last line immediately after adding the definition because it is an asynchronous, non-blocking call.
If you want to perform, adding all your synth definitions beforehand is good practice.
There is also the possibility to wait for the audio sever programmatically.

By calling ``SynthDef.new()`` or just ``SynthDef()``, we generate a new factory object that produces synth according to the [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) blueprint.
On behalf of the perspective of the audio server **scsynth**, this factory object produces ``Synth`` objects!
A [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) encapsulates the client-side representation of a synth definition and provides methods for creating new [Synth](https://doc.sccode.org/Classes/Synth.html), writing them to disk, and streaming them to a server.

Each [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) has a name which we have to use if we want to generate a ``Synth`` produced by [SynthDef](https://doc.sccode.org/Classes/SynthDef.html).
The name can either be a ``String`` ``"sine_beep"`` or a symbol ``\sine_beep``.

By calling ``synthDef.add()``, we add our [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) to the server.
From then on, we can create [Synth](https://doc.sccode.org/Classes/Synth.html) of this definition.
Note that if we terminate the server, the [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) is lost.

The second argument of the [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) is a function that has to be a *unit generator graph function* representing a *signal-flow graph*.
It is an instance of [Function](https://doc.sccode.org/Reference/Functions.html) which details how the unit generators are interconnected, their inputs and outputs, and what parameters are available for external control.

Let us explore the ``\sine_beep`` synth defined by *unit generator graph function*:
We declare two arguments ``freq`` and ``amp`` with default values of ``440`` and ``0.5``, respectively.
Then we create an [envelope](sec-envelope) which has a percussive shape.
The envelope controls the amplitude of our sine wave over time.
It goes from 0 to 1 to 0 within 0.41 seconds.
We use [multichannel expension](sec-mce) to duplicate the signal.
Finally, we send the audio signal ``sig`` to the output bus at channel ``0``.
Note that ``Out`` will automatically put the second signal to the second output bus, i.e. ``sig[1]``.

In the last executable line, the server **scsynth** executes a ``Synth`` defined by a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) identified by its name ``\sine_beep`` or ``"sine_beep"``.
After 0.41 seconds, our envelope ends, and garbage collection is triggered.
The ``doneAction`` tells the server to remove the played synth.

```{admonition} Cleaning up Synth
:name: hint-free-synths
:class: remark
The audio server does not know when to cleanup your synth.
You have to tell the server explicitly---there is no automatic garbage collection.
```

We can also **store** the [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) permanently on our hard drive by calling ``store()`` instead of ``add()``.
This call will create the file ``sineWave.scsyndef`` in the ``synthdefs`` directory which can be found in your [SuperCollider](https://supercollider.github.io/) application directory.
If you restart [SuperCollider](https://supercollider.github.io/) all [SynthDefs](https://doc.sccode.org/Classes/SynthDef.html) in the ``snythdefs`` directory are added to the server automatically.

## Sever vs Client

To understand [UGens](https://doc.sccode.org/Classes/UGen.html) we must understand the concept of client-side and server-side code evaluation.
Only the client-side code of a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) is executed when we add the [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) to the server.
Playing the synth by creating a [Synth](https://doc.sccode.org/Classes/Synth.html) executes only the server-side code!

Some of the ``sclang`` code can only be excuted on the server (e.g. playing sound) while other parts can only be executed on the client (e.g. the definition of the signal-flow graph).
The relationship between server- and client-side code becomes more evident if we compare server- and client-side randomness.

```isc
(
SynthDef(\crndsine, {
    var sig = SinOsc.ar(rrand(55, 75).poll.midicps) * 0.25!2;
    Out.ar(0, sig);
}).add;
)

(
SynthDef(\srndsine, {
    var sig = SinOsc.ar(Rand(55, 75).poll.round.midicps) * 0.25!2;
    Out.ar(0, sig);
}).add;
)

Synth(\crndsine);
Synth(\srndsine);
```

Both [SynthDefs](https://doc.sccode.org/Classes/SynthDef.html) look similar but ``\crndsine`` uses a client-side random generator, whereas ``\srndsine`` uses a server-side one, that is, the ``UGen`` called [Rand](https://doc.sccode.org/Classes/Rand.html).
There is no such thing as a server-side ``rrand`` function!
Its evaluation is part of the definition of the signal-flow graph.
Since ``rrand`` is evaluated when we add the [SynthDef](https://doc.sccode.org/Classes/SynthDef.html), each synth of this [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) will generate a randomly chosen sound which is the same for **all** synths constructed by this added [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) object.
Therefore, if we want a [Synth](https://doc.sccode.org/Classes/Synth.html) that generates a random sound whenever it is created, we need server-side randomness using a suitable [UGen](https://doc.sccode.org/Classes/UGen.html), in this case, [Rand](https://doc.sccode.org/Classes/Rand.html).

In the example above we use the ``poll`` functions which polls frequently values from unit generators to the client and post them to the post window.
This can be helpful to see what is going on, i.e., to debug server-side code.
Whenever we play ``\crndsine`` the exact same number gets posted.
But when we play the second synth, i.e. ``\srndsine`` multiple times, numbers change.

```{admonition} Server-side Debugging
:name: hint-server-side-debugging
:class: remark
You can ``poll`` any unit generator.
It will frequently print the values of the generator to the post windows.
```

## Named Controls

Arguments of a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) can be defined in different ways.
Similar to functions, we can either use the signal word ``arg`` 

```isc
(
SynthDef(\beep, {
  arg freq=440, amp=1.0;
  ...
}).add;
)
```

or we can rely on the bar ``|..|``

```isc
(
SynthDef(\mysynth, {
  |freq=440, amp=1.0|
}).add;
)
```

However, there exists an alternate approach.
Instead of employing "standard" variables, we have the option to utilize [NamedControls](https://doc.sccode.org/Classes/NamedControl.html).
Essentially, these are variables that can be controlled via [OSC messages](sec-osc).
Given the syntax shortcuts that create [NamedControls](https://doc.sccode.org/Classes/NamedControl.html) from a name or symbol, they are extremely convenient to use.
You can define such a control in the following manner:

```isc
\name.ar(values, lags, spec)
\name.kr(values, lags, fixedLag, spec)
\name.ir(values, lags, spec)
\name.tr(values, lags, spec)
```

The two characters after the ``.`` determine the rate and type of the [NamedControls](https://doc.sccode.org/Classes/NamedControl.html).
Using ``ar`` adds a new instance of [AudioControl](https://doc.sccode.org/Classes/AudioControl.html) at *audio rate*, ``kr`` or ``ir`` adds a new instance of [Control](https://doc.sccode.org/Classes/Control.html), either with continuous *control rate* signal ``kr`` or a static value ``ir`` and using ``tr`` adds a new instance of [TrigControl](https://doc.sccode.org/Classes/TrigControl.html).
The static value of ``ir`` is set at the time the synth starts up, and is subsequently unchangeable.
A [Control](https://doc.sccode.org/Classes/Control.html) is a [unit generator](sec-ugens) that can be set and routed externally to interact with a running synth.

```{admonition} Named Control
:class: remark
If one uses the same [NamedControls](https://doc.sccode.org/Classes/NamedControl.html) in a [SynthDef](https://doc.sccode.org/Classes/SynthDef.html) multiple times, its ``value`` and all other arguments have to be identical
```

If ``lags`` is given, the [Lag](https://doc.sccode.org/Classes/Lag.html) unit generator is applied and if ``fixedLag`` is set to be ``true`` a [LagControl](https://doc.sccode.org/Classes/LagControl.html) is used, meaning that ``lags`` can not be modulated at the advantage that fewer unit generators are required.
I already discussed the lagging of a signal in section [Signal Lagging](sec-signal-lagging).

Note that ``\freq.ir(440)`` appears twice in the following code.

```isc
(
SynthDef(\beep, {
  var sig, env;

  sig = Saw.ar(\freq.ir(440)!2);
  env = Env.perc.ar(doneAction: Done.freeSelf);
  sig = LPF.ar(sig, \freq.ir(440) * 3);
  Out.ar(0, sig * env * \amp.ir(1.0));
}).add;
)

~synth = Synth(\beep, [\freq: 300]) // works just fine
~synth.set(\freq, 500)              // has no effect!!!
```

Using ``ir`` is less powerful than using "standard" arguments because we can not change the value of a static named control after the synth has started.

```isc
(
SynthDef(\beep, {
  var sig, env;

  sig = Saw.ar(\freq.kr(440)!2);
  env = Env.perc.ar(doneAction: Done.freeSelf);
  sig = LPF.ar(sig, \freq.kr(440) * 3);
  Out.ar(0, sig * env * \amp.kr(1.0));
}).add;
)

~synth = Synth(\beep, [\freq: 300]) // works just fine
~synth.set(\freq, 500)              // works just fine
```

Named controls in control rate, i.e. ``kr``, are like knops and buttons of a MIDI device.
When we want to play around with the named controls of our synth we can utilize a graphical user interface ``gui`` that immitates the control components of such a MIDI device.
To do so we have to utilize [Ndef](https://doc.sccode.org/Classes/Ndef.html) instead of [SynthDef](https://doc.sccode.org/Classes/SynthDef.html).
Furthermore, we can define the range of possible values using ``specs``.

```isc
(
Spec.add(\freq, [100, 2000, \exp]);
Ndef(\beep, {
  var sig, env;

  sig = Saw.ar(\freq.kr(440)!2);
  env = Env.perc.ar(doneAction: Done.freeSelf);
  sig = LPF.ar(sig, \freq.kr(440) * 3);
  sig = sig * \amp.kr(1.0) * env;
}).gui;
)
```

Since we use ``\exp`` the range of the values for ``\freq`` is exponentially mapped on the slider.
In {numref}`Fig. {number} <fig-ndef-gui>` you can see that the slider's position is way to the right but the frequency value is only ``659.43``.

```{figure} ../../../figs/supercollider/synths/ndef-gui.png
---
width: 800px
name: fig-ndef-gui
---
After executing the code on the left, the popup window on the right will show up.
Pressing "play" initializes all required ingredients. Pressing "send" will actually create the sound.
```