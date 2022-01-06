(sec-filters)=
# Filters

The very basic understanding of filters might be that they just make parts of the signal quieter -- which is wrong.
They do far more than just attenuate some frequencies.
Because filters often use some kind of feedback cycle, I find them difficult to understand. 

## Phases
Before we can talk about filters let us talk about phases.
As we will see we can filter a signal by using a simple oscillator.

Let us first combine two sine waves.
The first two identical ones

\begin{equation}
y_1(t) = \sin(2\pi f t) + \sin(2\pi f t) = 2 \sin(2\pi f t)
\end{equation}

```isc
{SinOsc.ar(200) + SinOsc.ar(200)}.play
```

and then two where the second one is phase shifted by $\pi$ that is

\begin{equation}
y_1(t) = \sin(2\pi f t) + \sin(2\pi f t + \pi) = \sin(2\pi f t) - \sin(2\pi f t + \pi) = 0
\end{equation}

```isc
{SinOsc.ar(200) + SinOsc.ar(200, pi)}.play
```

Because we shift the phase by $\pi$ the resulting sound is silence!
This demonstrate the high impact of the relationships between signals with different phases.
Of course, we can not hear any difference between a sine wave and the same sine wave with some different phase.
Only in combination the phase plays a role!

Combining any number of signals, the maximal loudness of the sum of all signal lies within the sum of absolute maximum loudness of each signal and silence.

A phase of $\pi$ (one half cycle) for an oscillator with a frequency of $200$ Hz ($200$ cycles per second) results in a shift of 

\begin{equation}
\frac{1}{200} \cdot \frac{1}{2} = \frac{1}{400} = 0.0025
\end{equation}

seconds. 
For an oscillator with a frequency of $100$ Hz a phase shift of $\pi$ would imply a delay of ony $0.005$ seconds.

What is happing if we combine two [sawtooth waves](sec-sawtooth-wave) such that the fundamental frequencies of these two signals cancel each other out?

```isc
{LFSaw.ar(300!2, 0) + LFSaw.ar(300!2, 1) * 0.25}.play;
```

Compare this to the sound of a regular sawtooth wave:

```isc
{LFSaw.ar(300!2, 0) * 0.5}.play;
```

We clearly hear some differences and if we do the math we can see why!
As before, the fundamentals of frequency $f$ Hz of combining two sawtooth one shifted by $1/(2f)$ seconds, cancel each other out.
However the next harmonic with frequency $2f$ Hz is reinforced, that is, its amplitude is doubled.
This is because after $1/(2f)$ seconds this harmonic has gone through $(2f)/(2f) = 1$ cycle.

In the fact, amplitude of each even harmonic is reinforced since

\begin{equation}
\frac{2nf}{2f} = n 
\end{equation}

is a whole number but each odd harmonic gets canceled out since

\begin{equation}
\frac{nf}{2f} = \frac{n}{2} = k + \frac{1}{2}
\end{equation}

where $n$ is an odd number and $k = \mathbb{N}_0$ (one odd harmonic starts at the beginning of a cycle while the second one half way through).

This dual character (canceling or doubling) can be much more complex, that is, some frequencies might get a bit louder some a bit reinforced, few doubled and few canceled.

Cancelation is equivalent to filtering!
So our examples of using two oscillators one shifted by $\pi$ can be seen as filtering one oscillator by the other.
The second one acts like a filter.
This filter is called [Comb Filter](sec-comb-filter).
In **sclang** this filter is called ``DelayX`` where ``X`` stands for different interpolation techniques.

The following code is equivalent to the two sine waves that cancel each other out:

```isc
({
    var sig = SinOsc.ar(200);
    sig = sig + DelayL.ar(sig, maxdelaytime: 0.2, delaytime: 1/(2*200));
}.play;
)
```

Note that ``CombX`` is a delay line **with feedback**.
With ``DelayL`` we can achieve the filtering of the sawthoth wave without combining the sine waves by using multiple [UGens](def-ugen).

```isc
({
    var sig = LFSaw.ar(200 ! 2);
    sig = sig + DelayL.ar(sig, maxdelaytime: 0.2, delaytime: 1/(2*200)) * 0.5;
    sig;
}.play;
)
```

## Smoothening

A signal can also be filtered by smoothening it.
For example, let $\text{in}[0], \ldots, \text{in}[n]$ be the discrete (input) signal of a [sawtooth waves](sec-sawtooth-wave) and $\text{out}[0], \ldots \text{out}[n]$ be the filtered (output) signal.
If 
\begin{equation}
    \begin{split}
    \text{out}[0] &\leftarrow 0.5 \cdot \text{in}[0]\\
    \text{out}[i] &\leftarrow 0.5 \cdot \text{in}[i] - 0.5 \cdot \text{in}[i-1]
    \end{split}
\end{equation}

the result is the difference quotient divided by sample rate.
All values of $\text{out}$ are almost zero except at the parts which are not differentiable.

To achieve this effect we can use the [OneZero](sec-onezero)-filter.

```isc
{[LFSaw.ar(10), OneZero.ar(LFSaw.ar(10), -0.5)]}.plot(2/10)
```

```{figure} ../../figs/sounddesign/filters/canceled-saw-onezero-filter.png
---
width: 600px
name: fig-canceled-saw-onezero-filter
---
Canceling a sawtooth wave by applying a ``OneZero``-filter. You can see peaks at values where the sawtooth is not differentiable.
```

This works so well because the rate of change of a sawtooth wave is constant almost everywhere.

The integral of one phase of a sine wave is zero.
Consequently, by averaging the discrete signal to accomplish the respective sum will cancel out the sine wave, i.e., a specific frequency.
[OnePole](sec-onepole) computes an (weighted) average via a feedback cycle resulting in an exponential drop of weights.

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

```{figure} ../../figs/sounddesign/filters/sin_deviation.png
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

(sec-onepole)=
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
The exponential decay is depicted in {numref}`Fig. {number} <fig-lag-and-onepole>`.

``OnePole`` is a low-pass filter.
Compare. for example, the following similar sounding signals of a [sawtooth wave](sec-sawtooth-wave), first filtered by the low-pass filter ``LPF`` and then filtered by ``OnePole`` using a large $\alpha$:

```isc
{LPF.ar(Saw.ar(440), 400) * 0.25;}.play
{OnePole.ar(Saw.ar(440), coef: 0.98) * 0.25;}.play
```

``OnePole`` simulates a simple (analog/electrical) RC-filter (resistance, capacity).
In the [Wikipedia article](https://en.wikipedia.org/wiki/Low-pass_filter) about low-pass filters, you can find some additional explanations regarding the relationship between the continuous electrical and discrete digital filter.

(sec-lag)=
## Lag

The ``Lag``-``UGen`` is similar to ``OnePole`` but it has a more meaningful parameter, called ``lagTime``.
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

```{figure} ../../figs/sounddesign/filters/lag-and-onepole.png
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

Let us try to the 440 Hz part of a signal consisting of 440 and 40 Hz.

```isc
{SinOsc.ar(440)+SinOsc.ar(40) * 0.25;}.plot(2/40)
{3.8*Lag.ar(SinOsc.ar(440)+SinOsc.ar(40), lagTime: 300/440) * 0.25;}.plot(2/40)
```

```{figure} ../../figs/sounddesign/filters/lag-filtering.png
---
width: 800px
name: fig-lag-filtering
---
A signal consisting of 440 HZ and 40 Hz partial (left) filtered by ``Lag`` (right).
```

As we increase the ``lagTime`` we have to boost the amplitude of the signal.

(sec-varlag)=
## VarLag

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

```{figure} ../../figs/sounddesign/filters/var-lag.png
---
width: 800px
name: fig-var-lag
---
A filtered random signal. First we apply ``OnePole`` and ``Lag`` which gives us roughly the same result.
```

## Phasing & Filtering

If we speak of filters we often man low pass or high pass filters, that is, filters that filter frequencies above or below some cutoff frequency.
For example the low pass filter ``LPF`` in **sclang** is a 2nd order Butterworth lowpass filter.

```{figure} ../../figs/sounddesign/filters/butterworth-filter.png
---
width: 600px
name: fig-butterworth-filter
---
By Alejo2083 - Own work, CC BY-SA 3.0, [link](https://commons.wikimedia.org/w/index.php?curid=735081).
```

The filter reduces the gain (amplitude) for frequencies above the cutoff frequency and shifts their phases.
Well, that is not completely true because the cutoff frequency is also reduced by 3 [decibel (dB)](sec-intensity), so the reduction starts a little bit below the cutoff frequency.
Reducing the loudness by 3 dB means that the perceived level is reduced by a factor of 2.
The top plot of {numref}`Fig. {number} <fig-butterworth-filter>` shows the reduction in amplitude.

The second effect of the filter is a shift in phase, compare the bottom plot of {numref}`Fig. {number} <fig-butterworth-filter>`.
This effect is important if we want to combine multiple filters because they interact!
In other words: we can not just combine a high pass and low pass filter to get the same result of a band pass filter!

The following code is an example for a band pass filter.
First we use a low pass and high pass filter, then a band pass filter.
The results sound very similar but not identical.

```isc
({
    var sig = LFSaw.ar(500) ! 2 * 0.5;
    sig = HPF.ar(sig, 200);
    sig = LPF.ar(sig, 300);
    sig
}.play;)

({
    var sig = LFSaw.ar(500) ! 2 * 0.5;
    var bandwidth = 100;
    var cuttoffFeq = 200;
    sig = BPF.ar(sig, 250, rq: bandwidth / cuttoffFeq);
    sig
}.play;)
```

For completeness I also want to mention the inverse filter of a band pass filter: the band reject filter ``BRF``.

The following example rejects frequencies between 200 and 300 Hz, i.e., the inverse operation as before.

```isc
({
    var sig = LFSaw.ar(500) ! 2 * 0.5;
    var bandwidth = 100;
    var cuttoffFeq = 200;
    sig = BRF.ar(sig, 250, rq: bandwidth / cuttoffFeq);
    sig
}.play;)
```

## Responses and Resonance

To bring dynamic into the sound by a filter, we can do the obvious: change the cuttoff frequency over time!
Let us try this with a low pass filter:

```isc
(
Spec.add(\modfreq, [0, 1000]);
Spec.add(\freq, [0, 1000]);
Spec.add(\mincutoff, [5, 1000]);
Spec.add(\maxcutoff, [5, 1000]);

Ndef(\filtering, {
    var sig = Saw.ar(\freq.kr(400)) ! 2 * 0.5;
    var cuttoff = SinOsc.ar(\modfreq.kr(10)).range(\mincutoff.kr(100), \maxcutoff.kr(1000));
    sig = LPF.ar(sig, cuttoff);
}).play;
)

Ndef(\filtering).gui;
```

Almost all physical objects resonate.
Or, to put it another way, almost all objects will vibrate naturally at certain frequencies.
What happens to musical objects such as a string when we do not play/pluck them but they are in an environment where sound is generated.
In other words: how does such an object interact with vibrations of other objects?

What we observe in that case is **resonance**!
If the musical object is excited by frequencies that coincide with its natural resonant frequencies, then it will vibrate in sympathy with the source oscillator.
Otherwise it will approximately 'stand still'. 
How a musical instrument resonate has a great effect on the color of its sound ([timbre](sec-timbre)).

Resonance filters boost certain frequencies, making the harmonics at those frequencies louder than they were in the input signal.
The effect is sounds like resonance. 
Therefore, resonance filters emulate resonance.

Which frequencies are boosted?
For most resonance filters, the frequencies near the cutoff frequency are boosted.
In **sclang** the [UGens](def-ugen) resonance filter start with an ``R``, for example, ``RLPF`` is the resonance low pass filter.

```isc
(
Spec.add(\modfreq, [0, 1000]);
Spec.add(\freq, [0, 1000]);
Spec.add(\mincutoff, [5, 1000]);
Spec.add(\maxcutoff, [5, 1000]);
Spec.add(\bandwidth, [5, 100]);

Ndef(\filtering, {
    var sig = Saw.ar(\freq.kr(400)) ! 2 * 0.5;
    var cuttoff = SinOsc.ar(\modfreq.kr(10)).range(\mincutoff.kr(100), \maxcutoff.kr(1000));
    sig = RLPF.ar(sig, cuttoff, rq: \bandwidth.kr(100) / cuttoff);
}).play;
)
Ndef(\filtering).gui;
```

Try different values especially for the bandwidth.
A small bandwidth will result in a strong effect.

In fact, if the bandwidth is very small, the effect becomes so pronounced that the high and low frequencies disappear from the signal and another effect occurs: the filter begins to oscillate at its cutoff frequency.
The result is a powerful unnatural sound unique to the electronic synthesizer.

## Summary

Filters are essential for *subtractive synthesis*.
Filters do not only change the level of certain frequencies but apply a phase shift.
Many of the filters only apply such a shift and we often do not think of them as filters.

Let me summarize some of the applications of filters:

+ We can use static filters to emphasis certain frequencies.
+ We can use static filters to create formants in a sound, and imitate the characteristics of the human voice or traditional acoustic instruments.
+ A *resonance filter* with a moderate *resonance bandwidth* with a cuttoff frequency that tracks the pitch, can create a characteristic quality that remains tonally consistent as we play the keyboard.
+ For some *resonance filters*, if we decrease the *resonance bandwidth* we enter an area where the filter is at the brick of self-oscillation. This creates a distinctive distortion that can be a very good starting point.
+ If we decrease the *resonance bandwidth* even further, the filter will become a sine wave generator in its own right. In theory, no input signal is passed at this point, but few filters completely remove all the signal, and the result is a tortured sound that has extensive uses in modern music.

In analogue synthesis, filters are the defining element of a synthesizer!
They are crucial, also in digital synthesis, and if you are into creative synthesis, your sound generation will depend upon what you have got and what you do with it