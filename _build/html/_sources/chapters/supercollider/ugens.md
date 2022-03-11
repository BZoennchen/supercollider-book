(sec-ugens)=
# Unit Generators

In [Basics](sec-basics) we already talked about ``SynthDefs`` and ``Synths``.
Let us recall.
A ``SynthDef`` encapsulates the client-side representation of a synth definition and provides methods for creating new ``Synths`` on the server, writing itself (i.e. the definition / blueprint) to the disk, and streaming them to a server.
The normal workflow goes as follows:

1. define (all) our ``SynthDef`` via ``sclang``
2. we them (all) it to the audio sever **scsynth**
3. create a synth on the server

```
(
// (1) define the SynthDef
var synthdef = SynthDef(\sine_beep, {
	arg freq = 440, amp = 0.5;
	var sig;
	sig = SinOsc.ar(freq) * amp * Env([0,1,0], [0.01, 0.4], [5,-5]).ar(doneAction: Done.freeSelf);
	Out.ar(0, sig);
});

// (2) add it to the audio server scsynth
synthdef.add;
)

// (3) use it by creating Synth of the SynthDef
Synth(\sine_beep, [freq: 200, amp: 0.4]);
```

If we put the last line within the namespace of the rest above, the evaluation will cause an error because adding a ``SynthDef`` to the server takes time and is an asynchronous non-blocking process.
If you want to perform, it is good practice to add all your synth definition beforehand.

In the last line, the server **scsynth** executes a ``Synth`` defined by a ``SynthDef`` identified by its name ``\sine_beep`` or ``"sine_beep"``.
The ``SynthDef`` consists of so called [UGens](https://doc.sccode.org/Classes/UGen.html) (unit generators).
A ``SynthDef`` represents a directed signal graph where each node is a ``UGen`` and each edge is the signal output of one ``UGen`` and the signal input of another ``UGen``.
There are osillators that have no signal input.
They build the starting points!

```{admonition} UGen
:name: def-ugen
A ``UGen`` represent calculations with a signal.
They are the basic building blocks of synth definitions on the server, and are used to generate or process both audio and control signals.
```

``UGens`` are used to analyse, synthesize, and process signals at audio ``ar`` and control ``kr`` (or initialization only ``ir``) rate.
[SuperCollider (SC)](https://supercollider.github.io/) provides us with many different ``UGen``-classes which are client-side representations of the unit generators.

```{admonition} UGen execution
:class: important
A ``UGen`` is executed on the server!
```

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

In the following, I discuss certain ``UGens`` which I had difficulties to understand.

## Amplitude

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