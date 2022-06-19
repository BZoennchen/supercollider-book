(sec-ugens)=
# Unit Generators

The defining function of a ``SynthDef``, i.e. the [signal-flow graph (SFG)](https://en.wikipedia.org/wiki/Signal-flow_graph), consists of so called [UGens](https://doc.sccode.org/Classes/UGen.html) (unit generators).
It is a *unit genertor graph function*.
Unit generators are the smallest building blocks of our sound generation architecture.

## Definition

A unit generator is a component for the synthesis server, defined in a plug-in, which can receive a number of floating-point inputs (audio- or control-rate signal or constant values) and produce a number of floating-point data outputs, as well as *side effects* such as wrting to the post window, accessing a buffer, or seinding a message over a network.
The server can incorporate the unit generators into a synthesis graph, passing data from one unit generator to another.

```{figure} ../../figs/supercollider/ugens/sfg-example.png
---
width: 800px
name: fig-sfg-example
---
SFG of the example above which consist of three ``UGen``. The envelope converts the mono signal into a stereo signal.
``SinOsc`` is our source.
```

Each node of the graph represents a unit generator.
There are osillators, called *sources* that have no signal input.
They build the starting points, e.g. ``SinOsc``.

```{admonition} Unit Generator (UGen)
:name: def-ugen
:class: definition
A *unit generator* ``UGen`` represent calculations with a signal.
They are the basic building blocks of a synth definition, and are used to generate or process both *audio* and *control signals*.
```

When using ``sclang``, we need to have available a representation of each UGen which provides information about its inputs and outputs (the number, type etc.).
These representations allow us to define synthesis graphs in ``sclang``, i.e. ``SynthDefs``.
Therefore, each unit generator also comes with a SC class; these classes are always derived from a base class, appropriately called ``UGen``.
Later we will discuss how to write our own brand new unit generator.

```{admonition} Unit Generator Execution
:class: remark
A unit generator, i.e. an instance of ``UGen``, is executed on the server!
```

## Sample Rates

``UGens`` are used to analyse, synthesize, and process signals at audio ``ar``, control ``kr`` or initialization only ``ir`` rate.
The audio rate is much higher than the control rate.
This is reflected in the code since it is rather easy to spot a unit generator in SuperCollider code.
We just have to look for the message ``.ar`` or ``.kr``.

A unit generator runs at a specific rate, i.e. the rate it can spit out or process floating point numbers.
If your machine runs at 44100 Hz sample rate, a ``SinOsc.ar`` will generate 44100 samples per second.
Using ``kr`` will generate only 44100 / 64 = 700 samples per second.

```{admonition} Usage of Control Rate
:name: remark-control-rate
:class: remark
If precision is not important (e.g. in case of [low frequency oscillators (LFOs)](sec-lfo)) one should use the control rate ``kr`` to save CPU resources.
```

UGens are these incredibly fast generators of numbers.
Some of these numbers become sound signals; others become control signals.
We can use the ``.poll`` message to print 10 numbers per second to the post window:

```isc
{SinOsc.kr(1).poll}.play
```

## Categories

[SuperCollider (SC)](https://supercollider.github.io/) provides us with over 250 different ``UGen``-classes which are client-side representations of the unit generators.
They can be categorized into:

+ sources: periodic, aperiodic
+ filters
+ distortion
+ panning
+ reverbs
+ delays and buffer ugens
+ granular synthesis
+ control: envelopes, trigger, counters, gates, lags, decays
+ spectral

Instead of discussing these different UGens by listing them all at one place, I try to explain them under practical motivation.
For example, I will explain the [fundamental wavesforms](sec-fundamental-waveforms) in the context of [additive synthesis](sec-additive-synthesis).
We will explore many different UGens discussing [filters](sec-filters), [subtractive synthesis](sec-subtractive-synthesis) and many more concepts.

(sec-mce)=
## Multichannel Expension

When an [array](sec-array) is given as an input to a *unit generator* it causes an array of multiple copies of that unit generator to be made, each with a different value from the input array.
This behaviour is called multichannel expension.
All but a few special unit generators perform multichannel expension.
**Only** arrays are expanded, no other type of collection, not even subclasses of Array.

```isc
{ Blip.ar(500, 8, 0.1) }.play // one channel

// the array in the freq input causes an Array of 2 Blips to be created :
{ Blip.ar([499, 600], 8, 0.1) }.play // two channels

Blip.ar(500, 8, 0.1).postln // one unit generator created.

Blip.ar([500, 601], 8, 0.1).postln // two unit generators created.
```








## Special Unit Generators

In the following, I discuss certain ``UGens`` which I had difficulties to understand.
For all the well documented ``UGens`` such as [SinOsc](https://doc.sccode.org/Classes/SinOsc.html), [LFSaw](https://doc.sccode.org/Classes/LFSaw.html), [Saw](https://doc.sccode.org/Classes/Saw.html), [LFTri](https://doc.sccode.org/Classes/LFTri.html), I refer to the [official documentation](https://doc.sccode.org/Guides/Tour_of_UGens.html).

### Amplitude

In the description of the ``UGen`` called [Amplitude](https://doc.sccode.org/Classes/Amplitude.html) we find the following statement:

>Tracks the peak amplitude of a signal.

I had a hard time to understand what is going on here, especially how one should deal with the arguments ``attackTime`` and ``releaseTime``.
Why is this ``UGen`` even helpful?
Isn't the amplitude of a signal $y(t)$ defined by $|y(t)|$?

Well THE amplitude is not clearly defined at all.
Instead we are dealing with different kinds of amplitudes.
For example, we say that the following signal 

```isc
({
    var freg = 400;
    var attackTime = 0.1;
    var releaseTime = 0.2;
    var env = EnvGen.ar(Env.perc(attackTime: attackTime, releaseTime: releaseTime));
    var sig = SinOsc.ar(freg) * env;
    sig
}.plot(0.4);
)
```

has an amplitude of ``1.0``.

```{figure} ../../figs/supercollider/ugens/amplitude-sine.png
---
width: 800px
name: fig-amplitude-sine
---
A modulated amplitude of a sine wave. We say that this signal has an amplitude of 1.0.
```

What we actually mean is the **maximum amplitude of the signal**:

\begin{equation}
\max\limits_{t \in ]-\infty; +\infty[ } |y(t)|.
\end{equation}

Ok, but there is more.
What about the perceived amplitude of a signal.
In the example above, we can perceive that the sound gets louder over a time of 0.1 seconds and decays away in 0.2 seconds.

For an increasing and decaying signal we could compute each local maxima and minima, take the absolute value and interpolate in between.
That is basically what ``Amplitude`` does.
It computes the perceive loudness, i.e., local amplitude of a signal!

The following code generates another plot, that shows the difference.

```isc
({
    var freg = 400;
    var attackTime = 0.1;
    var releaseTime = 0.2;
    var env = EnvGen.ar(Env.perc(attackTime: attackTime, releaseTime: releaseTime));
    var sig = SinOsc.ar(freg) * env;
    [Amplitude.ar(sig, attackTime: attackTime, releaseTime: attackTime), sig, abs(sig)]
}.plot(0.4);
)
```

```{figure} ../../figs/supercollider/ugens/all-amplitude-sine.png
---
width: 800px
name: fig-all-amplitude-sine
---
A modulated amplitude of a sine wave. At the top the measured perceive loudness using ``Amplitude``. In the middle the actual signal $y(t)$ and at the bottom $|y(t)|$.
```

Somehow ``Amplitude`` underestimates the perceive loudness quite a bit.

Futhermore, we have to tell ``Amplitude`` the time period the signal loudness increases ``attackTime`` and the time period the amplitude decreases ``releaseTime``.
If we don't know these values or we are looking at a signal without an envelope, we have to choose a decently short time periods.
``Amplitude`` seems to analyse each chunk of the signal of size ``attackTime`` + ``releaseTime`` and computes an amplitude value for this time period.
Therefore, if we choose ``attackTime`` + ``releaseTime`` $\approx 1/(c \cdot f)$, where $f$ is the frequency of the signal and $c > 1$, we almost get $|y(t)|$.
I conclude that these values should be greater than $1/f$.

**Note** that we are talking about a discrete signal even if we write $y(t)$.

The default values are ``attackTime: 0.01`` and ``releaseTime: 0.01``, so for a signal with a frequency close to $100$ Hz, we should increase these values.

Let's end with an example.
Here we cut the noisy sound if its amplitude measured by ``Amplitude`` is below 0.2.

```isc
({ 
    var sig = WhiteNoise.ar(0.5!2) * 0.5 * SinOsc.kr(1);
    sig * (Amplitude.ar(sig) > 0.2);
}.play
)
```

As longas ``Amplitude.ar(sig) > 0.2`` is true, it returns (on the server-side) not true but 1.
Otherwise the expression is evaluated to 0.