(sec-ugens)=
# Unit Generators

The server **scsynth** executes so called ``UGens`` (Unit Generators) for analysis, synthesis, and processing of audio ``ar`` and control signals ``kr``.

```{admonition} UGen
:name: def-ugen
A ``UGen`` represent calculations with a signal.

```

## Amplitude

In the description of the ``UGen`` called ``Amplitude`` we find the following statement:

>Tracks the peak amplitude of a signal.

I had a hard time to understand whats going on here, especially how one should deal with the arguments ``attackTime`` and ``releaseTime``.
Why this ``UGen`` is even helpful?
Isn't the amplitude of a signal $y(t)$ defined by $|y(t)|$?

Well THE amplitude is not defined instead we are dealing with different kinds of amplitudes.
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

What we actually mean is the maximum amplitude of the signal:

\begin{equation}
\max\limits_{t \in ]-\infty; +\infty[ } |y(t)|.
\end{equation}

Ok, but there is more.
What about the perceived amplitude of a signal.
In the example above, we can perceive that the sound gets louder over a time of 0.1 seconds and decays away in 0.2 seconds.

For a increasing and decaying signal we could compute each local maxima and minima, take the absolute value and interpolate in between.
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

If ``Amplitude.ar(sig) > 0.1`` is true, it returns (on the server side) not true but 1.
Otherwise the expression is evaluated to 0.

## OneZero

I had a hard time understanding the filters operating and convoluting the input signal $\text{in}$, since the documentation is very minimal.
But I think I could reverse engineer the behaviour of these filters.
And the best way to start is by explaining the ``OneZero``-``UGen``.

The documentation states that a one zero filter implements the formula:

\begin{equation}
\text{out}[i] \leftarrow (1 - |\alpha|) \cdot \text{in}[i] + \alpha \cdot \text{in}[i-1]
\end{equation}

with $-1 \leq \alpha \leq 1$.
\text{in}[i] is actually the $i$-th sample of the discrete input signal.
Therefore, these filters depend on the sample rate / audio rate!

Let us use $\alpha = -0.5$ and we a differentiator!
Let $y(t)$ our signal, then we basically compute

\begin{equation}
    \frac{y(t) - y(t - h)}{2}
\end{equation}

To compute the difference quotient, we have to figure out what $h$ is.
In other words, what is the time between \text{in}[i] and \text{in}[i-1].
The answer is $1/a_\text{rate}$ where $a_\text{rate}$ is the audio rate.

To compute the difference quotient we use the following formula:

\begin{equation}
    \frac{y(t) - y(t - h)}{2} \cdot \frac{2}{h}.
\end{equation}

Using the discrete input signal $\text{in}$ this gives us:

\begin{equation}
    \frac{\text{in}[i] - \text{in}[i-1]}{2} \cdot \frac{2}{/a_\text{rate}}.
\end{equation}

To test this result, let us compute the cosine using ``SinOsc`` and a ``OneZero``.
Remember

\begin{equation}
    d\sin(2\pi \cdot f \cdot t)/dt = \cos(2\pi \cdot f \cdot t) \cdot 2 \pi \cdot f
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
```

## OnePole

Another ``UGen`` I have a hard time get my head around is ``OnePole``.
The documentation states that a one pole filter implements the formula:

\begin{equation}
\text{out}[i] \leftarrow (1 - |\alpha|) \cdot \text{in}[i] + \alpha \cdot \text{out}[i-1]
\end{equation}

with $-1 \leq \alpha \leq 1$.
$\text{out}$ is the resulting signal and $\text{in}$ the input signal of ``OnePole``.
For example,

\begin{equation}
\begin{split}
\text{out}[2] \leftarrow \ & (1 - |\alpha|) \cdot \text{in}[2] + \alpha \cdot \text{out}[1]\\
= & \ (1 - |\alpha|) \cdot \text{in}[2] + \alpha \cdot ((1 - |\alpha|) \cdot \text{in}[1] + \alpha \cdot \text{out}[0])\\
= & \ (1 - |\alpha|) \cdot \text{in}[2] + \alpha \cdot ((1 - |\alpha|) \cdot \text{in}[1] + \alpha \cdot \alpha \cdot \text{in}[0]).
\end{split}
\end{equation}

For $\alpha = 0.6$ we get

\begin{equation}
\begin{split}
\text{out}[2] \leftarrow 0.4 \cdot \text{in}[2] + 0.6 \cdot 0.4 \cdot \text{in}[1] + 0.6^2 \cdot \text{in}[0],
\end{split}
\end{equation}

For a negative $\alpha = -0.6$ we get

\begin{equation}
\begin{split}
\text{out}[2] \leftarrow 0.4 \cdot \text{in}[2] + (-0.6) \cdot 0.4 \cdot \text{in}[1] + (-0.6)^2 \cdot \text{in}[0].
\end{split}
\end{equation}

The general formula is given by 

\begin{equation}
\begin{split}
\text{out}[i] \leftarrow \alpha^i \cdot \text{in}[0] + \sum\limits_{k=1}^{i} (1-|\alpha|) \cdot \alpha^{i-k} \cdot \text{in}[k].
\end{split}
\end{equation}

I guess that the result depends on the sample rate, i.e. on the size of $\text{in}$ and $\text{out}$.
But in general a positive $\alpha$ will average a signal.
In other words, it will decrease the rate of change of the signal.
The larger $\alpha$ the smaller will be the rate of change of the result $\text{out}$.

A negative $\alpha$ will basically compute the an averaged deviation of the signal.
Therefore, any signal with a constant deviation will result in a signal of lower amplitude and if $\alpha$ is close to -1 there will be silence.
