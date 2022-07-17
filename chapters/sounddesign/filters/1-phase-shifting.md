# Phase Shifting

Before we can talk about filters let us talk about phases.
As we will see we can filter a signal by using a simple oscillator.
Therefore, the term *filter* is a very general term.

Let us combine two sine waves.
First two identical ones

\begin{equation}
y_1(t) = \sin(2\pi \omega t) + \sin(2\pi \omega t) = 2 \sin(2\pi \omega t),
\end{equation}

```isc
{SinOsc.ar(200) + SinOsc.ar(200)}.play
```

and then two where the second one is phase-shifted by $\pi$ that is

\begin{equation}
y_1(t) = \sin(2\pi \omega t) + \sin(2\pi \omega t + \pi) = \sin(2\pi \omega t) - \sin(2\pi \omega t + \pi) = 0.
\end{equation}

```isc
{SinOsc.ar(200) + SinOsc.ar(200, pi)}.play
```

Because we shift the phase by $\pi$, the resulting sound is silence!
This demonstrates the high impact of the relationships between signals with different phases.
Of course, we can not hear any difference between a sine wave and shifted sine wave.
Only in combination, the phase plays a role!

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

We clearly hear some differences, and if we do the math, we can see why!
As before, the fundamentals of frequency $\omega$ Hz cancel each other out.
However, the next harmonic with frequency $2\omega$ Hz is reinforced, i.e., its amplitude is doubled.
This is because after $1/(2\omega)$ seconds this harmonic has gone through $(2\omega)/(2\omega) = 1$ cycle.

In the fact, the amplitude of each even harmonic is reinforced since

\begin{equation}
\frac{2n\omega}{2\omega} = n 
\end{equation}

is a whole number but each odd harmonic gets canceled out since

\begin{equation}
\frac{n\omega}{2\omega} = \frac{n}{2} = k + \frac{1}{2}
\end{equation}

where $n$ is an odd number and $k \in \mathbb{N}_0$ (one odd harmonic starts at the beginning of a cycle while the second one half way through).

This dual character (canceling or doubling) can be much more complex.
Some frequencies might get a bit louder, some might be reinforced, a few doubled, and a few canceled.

Cancelation is equivalent to filtering!
So our examples of using two oscillators, one shifted by $\pi$ can be seen as filtering one oscillator by the other.
The second one acts as a filter.
This filter is called [Comb Filter](sec-comb-allpass-filter).
In ``sclang``, this filter is called ``DelayX`` where ``X`` stands for different interpolation techniques.
Note that ``CombX`` is a delay line **with feedback** (a little confusing).

The following code is equivalent to the two sine waves that cancel each other out:

```isc
({
    var sig = SinOsc.ar(200);
    sig = sig + DelayL.ar(sig, maxdelaytime: 0.2, delaytime: 1/(2*200));
}.play;
)
```

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