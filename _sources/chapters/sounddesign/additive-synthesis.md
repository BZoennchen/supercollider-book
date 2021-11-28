(sec-additive-synthesis)=
# Additive Synthesis

In *additive synthesis* we start by very simple wave forms, for example, a bunch of sine waves.
To create more complex signals and therefore sounds we add them together.

The beauty of *additive synthesis* is that we have full and direct control over each frequency and its amplitude within the final result.
We can even change each component (frequency, amplitude pair) over time.

This advantage consequently leads to a weakness of *additive synthesis*: it is computational expensive!
Instead of building a complex function before evaluation we evaluate each component and sum everything up.
For a complex and interesting sound we need a lot of oscillators.
For this reason, *additive synthesis* is hard to realize on analog synthesizer and even digital synthesizer can reach their limit quite fast.

Computers are getting faster and faster, therefore, *additive synthesis* might become more and more attractive.
Let us first start with a short introductory of the fundamental waveforms we might wanna combine.

## Fundamental Waveforms

Jean-Baptise Joseph Fourier discovered that every *signal* can be represented as a Fourier series.
A signal $y(t)$ is a function with some special conditions:

1. piecewise continuous and
2. bounded.

Functions that describe an amplitude $y(t)$ over the time $t$ are audio signals and have those two qualities.
The signal is also periodic but that is not a necessary condition for the existence of a Fourier series of the signal.

To understand the effect of a signal it is essential to understand its Fourier series.
In fact, the *stethoscope* displays the frequencies of the functions that are the components of the Fourier series.

For audio synthesis, there are very important signals analog as well as digital synthesizer offers as a starting point.
They are our basic oscillators and we have to understand their nature by looking at their Fourier series.

(sec-sine-wave)=
### The Sine Wave

The sine wave 

```{math}
:label: eq:sine
    y_\text{sine}(t) = A \cdot \sin(2\pi \cdot f \cdot t)
```

is the most pure most basic and most simple signal or wave form there is.
Its Fourier series is equivalent to Eq. {eq}`eq:sine`. 
It consists of only the fundamental frequency $f$ and is theoretically the basis for all other signals.

```{figure} ../../figs/sounddesign/sine.png
---
width: 400px
name: fig-sine
---
The sine wave with a frequency and amplitude of 1.
```

However, in practice one does not model something as complex as noise by using a Fourier series consisting of sine waves.
It would be too computational expensive and, since our resources are finite but the Fourier series consist infinite amount of terms, it can never be perfect.


(sec-sawtooth-wave)=
### The Sawtooth Wave

The first more complicated and important function I want to discuss is the so called [sawtooth wave](sec-sawtooth-wave)

```{math}
:label: eq:saw
    y_\text{saw}(t) = A \cdot 2 \left( f \cdot t -  \left \lfloor{ \frac{1}{2} + f \cdot t} \right \rfloor  \right),
```

where $A$ is the amplitude and $f$ is the frequency of the wave.


```{figure} ../../figs/sounddesign/sawtooth.png
---
width: 400px
name: fig-sawtooth
---
The sawtooth wave with a frequency and amplitude of 1.
```

I generated this plot using ``Python`` but we can do the same in **sclang** however, the $x$-axis will be always the number of the sample.
Let us generate the plot in {numref}`Fig. {number} <fig-sawtooth>` using **sclang**:

```isc
(
var trifunc = {
	arg t;
	var freq = 1, amp;
	amp = (freq*t - floor(1/2 + (freq*t)));
};

var t = Array.interpolation(100, 0, 1);
var y = t.collect({arg t; trifunc.value(t);});

y.plot();
)
```

To understand the [sawtooth wave](sec-sawtooth-wave) musically, we have to look at its Fourier series:

```{math}
:label: eq:saw:fourier
    y_\text{saw}(t) = A \left( \frac{1}{2} - \frac{1}{\pi} \sum_{k=1}^{\infty} (-1)^k \frac{\sin(2\pi k f t)}{k} \right).
```

We can approximate the series by only summing up the first $n$ terms:

```{math}
:label: eq:saw:fourier:n
    y_{\text{saw},n}(t) = A \left( \frac{1}{2} - \frac{1}{\pi} \sum_{k=1}^{n} (-1)^k \frac{\sin(2\pi k f t)}{k} \right).
```

```{figure} ../../figs/sounddesign/sawtooth_20.png
---
width: 400px
name: fig-sawtooth-20
---
An approximation for the Fourier series of the sawtooth wave with a frequency and amplitude of 1 using $n=20$.
```

The evaluation of many sine functions is computational more expensive than evaluating Eq. {eq}`eq:saw`.
However, we learn from Eq. {eq}`eq:saw:fourier` that

1. each harmonic of $k \cdot f$ with $k \in \mathbb{N}$ of the fundamental $f$ is present and
2. the amplitude decreases by $1/k$.

Furthermore, we can compute an approximation of the [sawtooth wave](sec-sawtooth-wave) by the technique of additive synthesis using Eq. {eq}`eq:saw:fourier:n`!

In **sclang** we can generate the sound of a [sawtooth wave](sec-sawtooth-wave) using the [UGen](sec-ugens) ``Saw``:

```isc
{Saw.ar(220!2)*0.25}.play;
```

(sec-square-wave)=
### The Square Wave

Another important wave is the [square wave](sec-square-wave) which is a special case of the pulse wave:


```{math}
:label: eq:square
    y_\text{square}(t) = A \cdot \text{sign}\left( \sin\left( 2\pi \cdot f \cdot t \right) \right)
```

where $\text{sign}(\cdot)$ is defined by

```{math}
:label: eq:sign
    \text{sign}(x) = \begin{cases}
    +1 & \text{ if } x \geq 0\\
    -1 & \text{ else.}
    \end{cases}
```

```{figure} ../../figs/sounddesign/square.png
---
width: 400px
name: fig-square
---
The square wave with a frequency and amplitude of 1.
```

Let's look at its Fourier series:

```{math}
:label: eq:square:fourier
    y(_\text{square}t) = A \cdot \frac{4}{\pi} \cdot \sum_{k=1}^{\infty} \frac{\sin( 2\pi \left[ 2k-1 \right] \cdot f \cdot t)}{2k - 1}
```

Again we learn from the Fourier series (Eq. {eq}`eq:square:fourier`) that

1. each odd harmonic $(2k-1)f$ with $k \in \mathbb{N}$ of the fundamental $f$ is present and
2. the amplitude decreases with $4/(2k - 1)$

The amplitudes also decrease linearly with increasing frequencies.

```{figure} ../../figs/sounddesign/square_20.png
---
width: 400px
name: fig-square-20
---
An approximation for the Fourier series of the square wave with a frequency and amplitude of 1 using $n=20$.
```

In **sclang** we can generate the sound of a [square wave](sec-square-wave) using the [UGen](sec-ugens) ``Pulse``:

```isc
{Pulse.ar(220!2) * 0.25;}.play;
```

(sec-triangle-wave)=
### The Triangle Wave

The next important wave is the [triangle wave](sec-triangle-wave):


```{math}
:label: eq:triangle
    y_\text{tri}(t) = A \cdot \left( 4 \cdot \left| f \cdot (t+1/4) -  \left \lfloor{ \frac{1}{2} + f \cdot (t+1/4)} \right \rfloor \right| - 1 \right),
```

where $\left| \cdot \right|$ is defined by

```{math}
:label: eq:abs
    \left| x \right| = \begin{cases}
    +x & \text{ if } x \geq 0\\
    -x & \text{ else.}
    \end{cases}
```

```{figure} ../../figs/sounddesign/triangle.png
---
width: 400px
name: fig-triangle
---
The triangle wave with a frequency and amplitude of 1.
```

Let's look at its Fourier series:

```{math}
:label: eq:triangle:fourier
    y_\text{tri}(t) = A \cdot \frac{8}{\pi^2} \cdot \sum_{k=0}^{\infty} (-1)^k \frac{\sin(2\pi \cdot f \cdot (2k+1) \cdot t)}{(2k+1)^2}
```

Again we learn from the Fourier series (Eq. {eq}`eq:triangle:fourier`) that

1. each odd harmonic $(2k+1)f$ with $k \in \mathbb{N}_0$ of the fundamental $f$ is present and
2. the amplitude decreases with $8\pi/(2k - 1)^2$

The amplitudes decrease **quadratically** with increasing frequencies.

```{figure} ../../figs/sounddesign/triangle_5.png
---
width: 400px
name: fig-triangle-20
---
An approximation for the Fourier series of the triangle wave with a frequency and amplitude of 1 using $n=5$.
```

In **sclang** we can generate the sound of a [square wave](sec-triangle-wave) using the [UGen](sec-ugens) ``LFTri``:

```isc
{LFTri.ar(220!2) * 0.25;}.play;
```

## Reconstruction of the Sawtooth Wave

Let us first recreate the [sawtooth wave](sec-square-wave) without ``LFSaw`` but instead only a bunch of ``SinOsc`` oscillators.
The following code generates the sound of the Fourier series approximation.
I implemented Eq. {eq}`eq:saw:fourier:n`.
You can change ``n`` to increase the number of harmonics.

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n;
    amp = 0.5;
    n = 10;
    sig = 0;

    n.do({
        arg index;
        var k = index+1;
        sig = sig + ((-1).pow(k) * SinOsc.ar(\freq.kr(220)*k) / k);
    });

    sig = (1/2) - ((1/pi) * sig);
    sig = sig!2 * amp;
}).play;
)
```

```{admonition} SCLang and the Server
:name: invalid-synthdef-arguments
:class: important
We are tempted to convert the variable ``n`` into an argument that we can change while the synth is playing!
Here we enter the limits of a synth or in other words the difference between **sclang** and the code that is actually running on the audio server.

**sclang** is executed on the client.
Therefore, the ``do``-construct is executed on the client before the synth is sent to the server.
In some sense, the synth is compiled and ``n`` is a variable which is fixed at run time.
Consequently, changing ``n`` while the synth is playing will not change anything.
```

My machine has no problem of running over hundred oscillators (``n=100``).
The CPU workload is at about 8-9 percent.
If we only use the first ten harmonics, the sound is clearly much more doll and it becomes crispier by adding more and more harmonics.
However, for me at least, at some point it is hard to perceive any difference if I add even more harmonics.

Ok, so far so good.
Of course, it makes no real sense to recreate the 'pure' [sawtooth wave](sec-square-wave) by multiple oscillators because it is much more computational expensive.
But if we introduce modulation we can create many different sounds that can not be produced by only one [sawtooth wave](sec-square-wave).
Even with filters this can be quite challenging or impossible.

For example, a string of a 'perfect' violin makes a sound that can be described by a [sawtooth wave](sec-square-wave) -- each harmonic of the fundamental is present.
However there is no globally determining envelope.
Instead each frequency changes its power over time independently.
Therefore, a real violin sounds completely different than a [sawtooth wave](sec-square-wave) combined with an [envelope](sec-envelope).
Furthermore, the world is imperfect and so is the violin -- there is always some distortion also within the frequencies.
Fortunately, our ears like this slight imperfection.
By introducing slight imperfections the sound becomes more gentle.
In summary, for a real violin

1. the amplitudes of the harmonics deviate from Eq. {eq}`eq:saw:fourier:n`,
2. they slightly deviate over time each in a different way,
3. and their power (amplitude) is a unique function of time.

### Global envelope

Let is first try a percussive envelope:

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n=20, env;
    amp = 0.5;
    sig = 0;

    env = EnvGen.ar(Env.perc(
        attackTime: \attk.kr(0.1),
        releaseTime: \rel.kr(1.0),
        curve: \curve.kr(-4)),
    doneAction: Done.freeSelf
    );

    n.do({
        arg index;
        var k = index+1;
        sig = sig + ((-1).pow(k) * SinOsc.ar(\freq.kr(220)*k) / k);
    });

    sig = (1/2) - ((1/pi) * sig);
    sig = sig!2 * amp * env;
}).play;
)
```

The sound is quite boring because nothing changes over time.
There is no dynamic thus we lose interest immediately.
Let us introduce some change over time.

### Noisy detuning of partials over time

My starting point is the introduction of detune but a detune that changes over time!
I introduce a variable ``vibrato`` that lies in between $[1-\epsilon; 1+\epsilon]$.
$\epsilon$ is the percentage of maximal detune, that is, a harmonic with a frequency of $f$ will have an actual frequency of $f \pm \epsilon f$.
In the code below, I call $\epsilon$ ``detune``.
The detune changes over time.

I make use of ``LFNoise1`` which chooses a value between 1 and -1 every $1/f$ seconds where $f$ is its frequency.
In between of these times, values are linearly interpolated.
Note that for each speaker the noises are different!
It is hard to explain what exactly happens with our ``vibrato`` over time so let us plot an example

```isc
{LFNoise1.ar(100!2).range(1-0.015, 1+0.015)}.plot(1.01)
```

gives us the following plot:

```{figure} ../../figs/sounddesign/add-synth-single-noise.png
---
width: 800px
name: fig-add-synth-single-noise
---
```

The updated version of ``\sine_sum`` looks like the following:

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n=20, env;
    var detuneFreq = 100;
    var detune = 0.015;

    amp = 0.5;
    sig = 0;

    env = EnvGen.ar(Env.perc(
        attackTime: \attk.kr(0.01),
        releaseTime: \rel.kr(1.0),
        curve: \curve.kr(-4)),
    doneAction: Done.freeSelf
    );

    n.do({
        arg index;
        var k = index+1;
        var vibrato = LFNoise1.ar(detuneFreq!2).range(1-detune, 1+detune);
        var harmonicFreq = \freq.kr(220) * vibrato * k;
        var harmonic = ((-1).pow(k) * SinOsc.ar(harmonicFreq) / k);
        sig = sig + harmonic;
    });

    sig = (1/2) - ((1/pi) * sig);
    sig = sig * amp * env;
}).play;
)
```

In my opinion, this already sounds much more interesting.
Of course, we went beyond *additive synthesis* and used *frequency modulation* but those go hand in hand especially if the modulation frequency is low.

### Separated partial envelopes

What can we do in addition?
Well, at the moment we have one global envelope for all frequencies.
What about ``n`` independent envelopes?
We could, for example, imitate nature and decrease the amplitudes of high frequencies faster than those of low frequencies.
We could make this relation randomly such that only the expected decrease in amplitude behaves like that.

```isc
(
Ndef(\sine_sum, {
    var sig, amp, n=20;
    var detuneFreq = 100;
    var detune = 0.015;

    amp = 0.5;
    sig = 0;

    n.do({
        arg index;
        var k = index+1;

        var env = EnvGen.ar(Env.perc(
            attackTime: \attk.kr(0.01) * Rand(0.8,1.2),
            releaseTime: \rel.kr(5.0) * Rand(0.9,1.1),
            curve: \curve.kr(-4))
        );

        var vibrato = LFNoise1.ar(detuneFreq!2).range(1-detune, 1+detune);
        var harmonicFreq = \freq.kr(220) * vibrato * k;
        var harmonic = ((1/2) - ((1/pi) * ((-1).pow(k) * SinOsc.ar(harmonicFreq) / k))) * env.pow(1+((k-1)/3));
        sig = sig + harmonic;
    });

    sig = sig * amp;
    DetectSilence.ar(sig, doneAction: Done.freeSelf);
    sig;
}).play;
)
```

Ok, this looks complicated.
However, I did not change too much.
First, I have rewritten the series such that the sum is the most outer operation.
Secondly, I generate for each frequency one independent envelope with a random attack and release.
Thirdly, I take the power to decrease the envelope for high frequencies faster:

```{math}
:label: eq:env:amplified
    x \leftarrow x^{1 + \frac{k-1}{3}}
```

where $x$ is a value of the envelope (a series of numbers) of the $k^\text{th}$-harmonic.
Compare the following two plots.

```{figure} ../../figs/sounddesign/add-synth-env_2.png
---
width: 400px
name: fig-add-synth-env_2
---
The effect of Eq. {eq}`eq:env:amplified` for $k = 2$.
```

```{figure} ../../figs/sounddesign/add-synth-env_10.png
---
width: 400px
name: fig-add-synth-env_10
---
The effect of Eq. {eq}`eq:env:amplified` for $k = 10$.
```

Fourthly, I remove the ``doneAction: Done.freeSelf`` from the envelopes because this would shut down the synth as soon as the first envelope reaches its end.
The sound would abruptly end too early.
To clean up the audio server, I instead use ``DetectSilence``-[UGen](sec-ugens).
It executes the cleanup, that is, the action ``freeSelf`` if the signal ``sig`` indicates silence for a small period of time, which is very handy.