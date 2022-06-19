(sec-synths)=
# Synth & SynthDefs

The concept of synth definitions and synth is central to SuperCollider.
Everything is build around this fundamental concept.
For beginners it can be quite confusing because there is a big difference between a synth as we know it from the real world and an instance of ``Synth``.

## Definition

A synth in the real world is an instrument that can be played.
However, in **sclang** we distinguish between the instrument (as a potential/thing) and the played instrument (as a process).
While the thing is an instance of ``SynthDef``, the process (an executed [signal-flow graph (SFG)](https://en.wikipedia.org/wiki/Signal-flow_graph)) is an instance of ``Synth``.

We do not introduce a new class for each new intrument.
Instead, each intrument is represented by a function, more precisely by a function realizing a signal-flow-graph (SFG).
The SFG completely defines the instrument.
At the same time the synth definition provides an interface to play it.
To do so we generate synths calling the defining function with different arguments.

```{admonition} SynthDef
:name: def-synth-def
:class: definition
An instance of ``SynthDef`` represents a factory of a parameterizable signal-flow-graph.
The graph can be executed (as ``Synth``) on the audio server.
```

From the perspective of a musician, a synth definition is a parameterizable description of a short peace of sound.
A synth on the other hand is the process of playing that peace of sound with specific parameters (frequency, loudness, velocity, etc.).
From a software developer perspective, a synth definition is a factory that generates synths following its internal description.

A ``SynthDef`` object encapsulates the server-side representation of a synth definition and provides methods for creating new ``Synths`` objects on the server.
Furthermore a ``SynthDef`` object can be serialized to the disk, and streamd via the network to distant audio servers.
``SynthDefs`` are nothing more than compact representations of signal-flow graphs written down in text.

```{admonition} Synth
:name: def-synth
:class: definition
A ``Synth`` is a representation of a signal-flow-graph executed in the audio server.
It is the process that generates sound.
```

## Workflow

We can use ``sclang`` to define a ``SynthDef``.
It is defined on the client and we have to send it to the audio server.
To generate sound we have to tell the server to generate a synth via one of its known ``SynthDefs``.

The normal workflow goes as follows:

1. define (all) your ``SynthDef`` via ``sclang``
2. add them (all) it to the audio sever **scsynth**
3. create a synth on the server
4. remove the synth from the server

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
Synth(\sine_beep, [freq: 200, amp: 0.4]);

// (4) the synth removes itself because we specied doneAction: Done.freeSelf
```

Note that adding a ``SynthDef`` to the server takes time.
Therefore, we can not execute the last line immediately after adding the definition because it is an asynchronous non-blocking process.
If you want to perform, it is good practice to add all your synth definition beforehand.

Let us explore the ``\sine_beep`` synth defined by the above ``SynthDef``:
The second argument of the ``SynthDef`` is a function.
We define two arguments ``freq`` and ``amp`` for the frequency and the amplitude of the beep sound.
Then we use a ``SineOsc``-[UGen](def-ugen) as *source signal* and we multiply it by an [envelope](sec-envelope).
The envelope goes from 0 to 1 to 0 within 0.41 seconds.
We use [multichannel expension](sec-mce) to duplicate the signal.
Finnally, we put our array of two signals ``sig`` at the zero bus of the output.
Note that ``Out`` will automatically put the second signal, i.e. ``sig[1]`` to the second output bus.

In the last executable line, the server **scsynth** executes a ``Synth`` defined by a ``SynthDef`` identified by its name ``\sine_beep`` or ``"sine_beep"``.
After 0.41 seconds our envelope ends and garbage collection is triggered.
The ``doneAction`` tells the server to remove the played synth.

```{admonition} Cleaning up Synth
:name: hint-free-synths
:class: remark
The audio server does not know when to cleanup the synth in general.
We have to tell it explicitly -- there is no automatic garbage collection.
```

## Sever vs Client

To understand ``UGens`` we have to understand the concept of client-side and server-side code evaluation.
Only the client-side code of a ``SynthDef`` is executed when we add the ``SynthDef`` to the server.
Playing the synth by creating a ``Synth`` executes only the server-side code!

The relationship between server- and client-side code becomes more obvious if we compare server- and client-side randomness.

```isc
(
SynthDef(\crndsine, {
    var sig = SinOsc.ar(rrand(55, 75).midicps) * 0.25!2;
    Out.ar(0, sig);
}).add;
)

(
SynthDef(\srndsine, {
    var sig = SinOsc.ar(Rand(55, 75).round.midicps) * 0.25!2;
    Out.ar(0, sig);
}).add;
)

Synth(\crndsine);
Synth(\srndsine);
```

Both ``SythDefs`` look similar but ``\crndsine`` uses a client-side random generator, where ``\srndsine`` uses a server-side one, that is, the ``UGen`` called ``Random``.
Since ``rrand`` is evaluated when the we add the ``SynthDef``, each synth of this ``SynthDef`` will generate a randomly chosen sound which is the same for all synths.
Therefore, if we want a ``Synth`` that generates a random sound whenever it is created we need server-side randomness using a suitable ``UGen``.