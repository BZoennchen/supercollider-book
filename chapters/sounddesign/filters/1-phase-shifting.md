# Phase Shifting

Before we can talk about filters let us talk about phases.
As we will see we can filter a signal by using a simple oscillator.
Therefore, the term *filter* is a very general term.

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
In ``sclang`` this filter is called ``DelayX`` where ``X`` stands for different interpolation techniques.

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

I will discuss these *delays* in section [Delays](sec-delays).