(sec-ugens)=
# Unit Generators

The server **scsynth** executes ``Synth`` defined by a ``SynthDef`` which consists of so called [UGens](https://doc.sccode.org/Classes/UGen.html) (Unit Generators).
``UGens`` are used to analyse, synthesize, and process signals at audio ``ar`` and control ``kr`` (or initialization only ``ir``) rate.

```{admonition} UGen
:name: def-ugen
A ``UGen`` represent calculations with a signal.
They are the basic building blocks of synth definitions on the server, and are used to generate or process both audio and control signals.
```

[SuperCollider (SC)](https://supercollider.github.io/) provides us with many different ``UGen``-classes which are client-side representations of the unit generators.

```{admonition} UGen execution
:class: important
A ``UGen`` runs on the server!
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

I had a hard time to understand whats going on here, especially how one should deal with the arguments ``attackTime`` and ``releaseTime``.
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
    sig * (Amplitude.ar(sig) > 0.1);
}.play
)
```

If ``Amplitude.ar(sig) > 0.1`` is true, it returns (on the server-side) not true but 1.
Otherwise the expression is evaluated to 0.

(sec-onezero)=
## OneZero

[OneZero](https://doc.sccode.org/Classes/OneZero.html) extends from [Filter](https://doc.sccode.org/Classes/Filter.html) thus it is a filter.
I had a hard time understanding what this filter actually does to its input signal $\text{in}$, since the documentation is very minimal.
But I think I could reverse engineer its behaviour.

The documentation states that a one zero filter implements the formula:

\begin{equation}
\text{out}[i] \leftarrow (1 - |\alpha|) \cdot \text{in}[i] + \alpha \cdot \text{in}[i-1]
\end{equation}

with $-1 \leq \alpha \leq 1$.
$\text{in}[i]$ is actually the $i$-th sample of the discrete input signal.
Therefore, ``OneZero`` as well as ``OnePole`` depend on the sample rate / audio rate!

Let us use $\alpha = -0.5$ and we a differentiator!
Let $y(t)$ be our signal, then we basically compute

\begin{equation}
    \frac{y(t) - y(t - h)}{2}.
\end{equation}

To compute the difference quotient, we have to figure out what $h$ is.
In other words, what is the time between $\text{in}[i]$ and $\text{in}[i-1]$.
The answer is $1/a_\text{rate}$ where $a_\text{rate}$ is the audio rate.

To compute the difference quotient we use the following formula:

\begin{equation}
    \frac{y(t) - y(t - h)}{2} \cdot \frac{2}{h}.
\end{equation}

Using the discrete input signal $\text{in}$ gives us:

\begin{equation}
    \frac{\text{in}[i] - \text{in}[i-1]}{2} \cdot \frac{2}{a_\text{rate}}.
\end{equation}

To test this result, let us compute the cosine using ``SinOsc`` and a ``OneZero``.
Remember

\begin{equation}
    \frac{d\sin(2\pi \cdot f \cdot t)}{dt} = 2 \pi \cdot f \cdot \cos(2\pi \cdot f \cdot t) 
\end{equation}

```isc
({
    var freq = 220;
    var sample_rate = 48000;
    var dt = sample_rate.reciprocal;
    [OneZero.ar(SinOsc.ar(freq), -0.5) * 2 / dt / (2 * pi * freq), SinOsc.ar(freq)]
}.plot(1/220)
)
```

```{figure} ../../figs/supercollider/ugens/sin_deviation.png
---
width: 400px
name: fig-all-sin_deviation
---
At the top the cosine generated by the bottom signal and a ``OneZero``-``UGen``.
```

````{admonition} Slope UGen
:class: hint
The [Slope](https://doc.sccode.org/Classes/Slope.html)-``UGen`` can also be used to compute the slope of a signal.

```isc
Slope.ar(SinOsc.ar(freq)) / (2 * pi * freq);
```

gives us the cosine.
````

If we use $\alpha = 1.0$ we generate a single sample delay and for -1.0 we additionally mirror the signal at the $x$-axis.

## OnePole

Another ``UGen`` I have a hard time get my head around is ``OnePole``.
The documentation states that a one pole filter implements the formula:

```{math}
:label: eq:onepole
    \text{out}[i] \leftarrow (1 - |\alpha|) \cdot \text{in}[i] + \alpha \cdot \text{out}[i-1]
```

with $-1 \leq \alpha \leq 1$.
I assume 

\begin{equation}
\text{out}[0] \leftarrow (1 - |\alpha|) \cdot \text{in}[0]
\end{equation}

holds. $\text{out}$ is the resulting signal and $\text{in}$ the input signal of ``OnePole``.
Let us assume $1 \geq \alpha \geq 0$, then we can rearrange Eq. {eq}`eq:onepole`:

```{math}
:label: eq:onepole2
    \text{out}[i] \leftarrow \text{in}[i] + \alpha \cdot (\text{out}[i-1] - \text{in}[i])
```

or 

```{math}
:label: eq:onepole3
    \text{out}[i] \leftarrow \text{out}[i-1] + \beta \cdot (\text{in}[i] - \text{out}[i-1])
```

with $\beta = 1-\alpha$.
If $\beta$ is small, ($\alpha$ is large respectively), then output samples $\text{out}[0], \ldots \text{out}[n]$ respond more slowly to a change in the input samples $\text{in}[0], \ldots \text{in}[n]$. For example,

\begin{equation}
\begin{split}
\text{out}[2] & \leftarrow \text{out}[1] + \beta \cdot (\text{in}[2] - \text{out}[1]) \\
  & = \text{in}[2] \cdot \beta + \text{in}[1] \cdot (\beta - \beta^2) + \text{in}[0] \cdot (\beta - 2\beta^2 + \beta^3)\\
  & = \beta \cdot (\text{in}[2] + \text{in}[1] \cdot (1 - \beta) + \text{in}[0] \cdot (1 - \beta)^2) \\
  & = (1-\alpha) \cdot (\text{in}[2] + \text{in}[1] \cdot \alpha + \text{in}[0] \cdot \alpha^2)
\end{split}
\end{equation}

and in general we get

\begin{equation}
\begin{split}
\text{out}[i] \leftarrow (1-\alpha) \cdot \sum\limits_{k=0}^{i} \alpha^{i-k} \cdot \text{in}[k].
\end{split}
\end{equation}

The change from one filter output to the next is proportional to the difference between the previous output and the next input.
Therefore, the signal is smoothen exponentially, which matches the exponential decay seen in the continuous-time system.
``OnePole`` is a low-pass filter.

Compare the following similar sounding signals of a [sawtooth wave](sec-sawtooth-wave), first filtered by the low-pass filter ``LPF`` and then filtered by ``OnePole`` using a large $\alpha$:

```isc
{LPF.ar(Saw.ar(440), 400) * 0.25;}.play
{OnePole.ar(Saw.ar(440), coef: 0.98) * 0.25;}.play
```

In the [Wikipedia article](https://en.wikipedia.org/wiki/Low-pass_filter) about low-pass filters, one can find some additional explanations.

## Lag and VarLag

The ``Lag`` ``UGen`` is similar to ``OnePole`` but it has a more meaningful parameter, called ``lagTime``.
I do not yet fully understand what it means but basically it is the time frame for which the signal should be smoothen.

The following code plots a the signal of a noise generator which generates a random value every ``1/freq`` seconds.
We smoothen the noise by a ``OnePole`` and by ``Lag``.
Our frequency is 10 Hz and our ``lagTime`` is 0.1 seconds.

```isc
({
    var freq = 10;
    var noise = LFNoise0.ar(freq);
    [noise, OnePole.ar(noise, coef: 0.999), Lag.ar(noise, lagTime: freq.reciprocal)];
}.plot(2.0))
```

This gives us the following plot.

```{figure} ../../figs/supercollider/ugens/lag-and-onepole.png
---
width: 800px
name: fig-lag-and-onepole
---
A filtered random signal. First we apply ``OnePole`` and ``Lag`` which gives us roughly the same result.
```

Since ``Lag`` is often used to smoothen changing parameters, for example in a performance, SC supports a syntactical shorthand:

```isc
LFNoise0.ar(freq).lag(0.1);
```

``VarLag`` is similar to ``Lag`` but with other curve shapes than exponential but it works only on control rate signals ``kr``!
Compare the different shapes of the lag:

```isc
({
    var freq = 10;
    var noise = LFNoise0.kr(freq);
    [
        noise, 
        VarLag.kr(noise, time: freq.reciprocal, warp: \sine), 
        VarLag.kr(noise, time: freq.reciprocal, warp: \linear), 
        Lag.kr(noise, lagTime: freq.reciprocal)
    ];
}.plot(2.0))
```

```{figure} ../../figs/supercollider/ugens/var-lag.png
---
width: 800px
name: fig-var-lag
---
A filtered random signal. First we apply ``OnePole`` and ``Lag`` which gives us roughly the same result.
```