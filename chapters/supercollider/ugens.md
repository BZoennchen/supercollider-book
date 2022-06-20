(sec-ugens)=
# Unit Generators

The defining function of a ``SynthDef``, i.e. the [signal-flow graph (SFG)](https://en.wikipedia.org/wiki/Signal-flow_graph), consists of a network of so called *unit generators* ([UGens](https://doc.sccode.org/Classes/UGen.html)).
Unit generators are the smallest building blocks of our sound generation architecture.
They are used for generatingad processing sigals with the SuperCollider synthesis audio server.

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

A *unit generator* is the signal-generating and -processing workhorse for the SuperCollider synthesis environment.
They provide an efficient modular system for creating complicated *audio networks*, which we will refer to *unit generator graphs* or *unit generator graph function*.
*Unit generators* are defined within libraries, which are are written in the ``C++`` programming language and compiled before use.
The libraries (*plug-ins*) are loaded into an instance of SuperCollider's audio server *scsynth* when it is booted and persist until the server quits.
Any sound produced by *scsynth* is the result of a *unit generator*, and *unit generators* are used only inside scsynth.
``UGens`` are represented in the Supercollider language's class system.
Therefore, a *unit generator* is realized by a combination of ``C++`` and ``sclang`` code.

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

+ sources (periodic, aperiodic)
+ filters (low pass, high pass, ...)
+ distortion (tanh, clipping, ...)
+ panning 
+ reverbs 
+ delays
+ buffers
+ granular synthesis
+ control (envelopes, trigger, counters, gates, lags, decays)
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