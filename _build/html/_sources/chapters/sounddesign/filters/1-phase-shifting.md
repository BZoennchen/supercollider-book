# Filtering by Delays

Delays are one of the building blocks of music synthesis and musical performances.
In the digital world and in its basic form, it comes down to playing a signal $x$ again after a certain amount of time, s.t. the result $y$ is defined by

\begin{equation}
y[n] = \begin{cases} x[n] + \alpha \cdot x[n-k], & \text{ for } n \geq k\\ x[n], & \text{ else } \end{cases}
\end{equation}

for some $k \in \mathbb{N}$.
This kind of delay is called *feedforward comb filter* and $\alpha$ is the *feedforward coefficient*.

In SuperCollider we can use the most basic delay called [DelayN](https://doc.sccode.org/Classes/DelayN.html).
However, this unit generator will output $\alpha \cdot x[n-k]$ without the original signal which we have to add manually. 
Do not confuse [Comb](https://doc.sccode.org/Classes/Comb.html) with a *feedforward comb filter* since it is a **feedback** *comb filter*!

Delays are the building block for two other central contects in digital signal processing:

1. filters, and 
2. [reverbs](sec-reverb)

In this section we focus on filtering.
But before we do so let us also talk about phases and let me show how we can filter by adding another signal to the input signal which happens to have a different phase.
As we will see, we can filter a signal by using a simple oscillator.
Which shows that the term *filter* is a very general term.

## Phase Shifting

Let us combine two (analog) sine waves.
First two identical ones

\begin{equation}
y_1(t) = \sin(2\pi f t) + \sin(2\pi f t) = 2 \sin(2\pi f t),
\end{equation}

```isc
{SinOsc.ar(200) + SinOsc.ar(200)}.play
```

and then two where the second one is phase-shifted by $\pi$ that is

\begin{equation}
y_1(t) = \sin(2\pi f t) + \sin(2\pi f t + \pi) = \sin(2\pi f t) - \sin(2\pi f t + \pi) = 0.
\end{equation}

```isc
{SinOsc.ar(200) + SinOsc.ar(200, pi)}.play
```

Because we shift the phase by $\pi$, the resulting sound of the second code snippet is silence!
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
What is happens if we combine two [sawtooth waves](sec-sawtooth-wave) such that the fundamental frequencies of these two signals cancel each other out?

```isc
{LFSaw.ar(300!2, 0) + LFSaw.ar(300!2, 1) * 0.25}.play;
```

Compare this to the sound of a regular sawtooth wave:

```isc
{LFSaw.ar(300!2, 0) * 0.5}.play;
```

We clearly hear some differences, and if we do the math, we can see why!
As before, the fundamentals of frequency $f$ Hz cancel each other out.
However, the next harmonic with frequency $2f$ Hz is reinforced, i.e., its amplitude is doubled.
This is because after $1/(2f)$ seconds this harmonic has gone through $(2f)/(2f) = 1$ cycle.
In the fact, the amplitude of each even harmonic is reinforced since

\begin{equation}
\frac{2nf}{2f} = n 
\end{equation}

is a whole number but each odd harmonic gets canceled out since

\begin{equation}
\frac{nf}{2f} = \frac{n}{2} = k + \frac{1}{2},
\end{equation}

where $n$ is an odd number and $k \in \mathbb{N}_0$ (one odd harmonic starts at the beginning of a cycle while the second one half way through).

This dual character (canceling or doubling / lowering or boosting) can be much more complex.
Some frequencies might get a bit louder, some might be reinforced, a few doubled, and a few canceled.

Our examples of using two oscillators, one shifted by $\pi$ can be seen as filtering one oscillator by the other.
The second one acts as a filter.

## Feedforward Comb Filter

In ``sclang``, we can achieve such shift of any signal a *delay* e.g. [DelayL](https://doc.sccode.org/Classes/DelayL.html).
Other than, e.g. [OneZero](sec-onezero), most of the delay unit generators in SuperCollider are controlled through time in seconds.
This is much more convinient since it is independent of the sample rate which depends on the system.
Furthermore, it is far easier to think in time instead of number of samples.
Given some delay time $\tau$ and sample rate $f_s$, the delay in samples can be computed as $\tau \cdot f_s$. Note though that $\tau \cdot f_s$ is not guaranteed to be a natural number.
Therefore, different interpolation strategies are used.
The ``L`` in ``DelayL`` stands for linear interpolation.

The following code is equivalent to the two sine waves that cancel each other out:

```isc
({
    var freq = 200;
    var sig = SinOsc.ar(freq);
    sig = sig + DelayL.ar(
        sig, 
        maxdelaytime: 0.2, 
        delaytime: 1/(2*freq));
}.play;
)
```

We delay the second signal by half the period of the first signal.
``maxdelaytime`` is a parameter that SuperCollider uses to determine the amount of memory (buffer size) required for the delay.
It has no audible effect but has to be larger than ``delaytime`` ever is (we can modulate this argument).
With ``DelayL`` we can achieve the filtering of the sawthoth wave without combining the sine waves by using multiple [UGens](def-ugen).

```isc
({
    var sig = LFSaw.ar(200 ! 2);
    sig = sig + DelayL.ar(
        sig, 
        maxdelaytime: 0.2, 
        delaytime: 1/(2*200)) * 0.5;
    sig;
}.play;
)
```

Since the delay has the same effect as adding a phase shifted signal, it also amplifies/attenuate certain frequencies.
Therfore, a *feedforward comb filter* is a *filter*!
It has an *amplitude response* (which is one part of the [frequency response](sec-frequency-response)) that expresses the ratio of that amplification as a function of frequency.
A *feedforward comb filter* is also a [finite impuse response filter](def-fir-filter).

## Feedback Comb Filter

A *feedback comb filter* fulfills the following equation:

\begin{equation}
y[n] = \begin{cases} x[n] + \beta \cdot y[n-k], & \text{ for } n \geq k\\ x[n], & \text{ else. } \end{cases}
\end{equation}

The [impulse response](sec-impulse-response) of this type of delay gives us infinite peaks.
If the *feedback coefficient* $\beta < 1.0$ consecutive peaks decrease (stable network), if $\beta > 1.0$ (unstable) they increase, and if $\beta = 1$ (also considered as unstable) they stay at a constant amplutide.

Again, since the comb filter amplifies/attenuate certain frequencies.
Therfore, a *feedback comb filter* is a *filter*!
A *feedback comb filter* is an [infinite impuse response filter](def-iir-filter).

In SuperCollider the unit generator [CombN](https://doc.sccode.org/Classes/CombN.html) realizes a *feedback comb filter*.
Again, instead of providing the *feedback coefficient* directly it is computed.
We instead provide a ``decayTime`` which is the time for the echoes to decay by 60 decibels.
If this time is negative, then the *feedback coefficient* will be negative, thus emphasizing only odd harmonics at an octave lower.
Note that infinite decay times are permitted. 
A ``decayTime`` of ``inf`` leads to a *feedback coefficient* of 1, and a decay time of ``-inf`` leads to a *feedback coefficient* of -1.

```isc
(
SynthDef(\fbComb, {
    arg out = 0, delayTime = 0.2, decayTime = 1, in;
    var sig, sigCombed;
    sig = Impulse.ar(1);
    sigCombed = CombN.ar(sig, 2, delayTime, decayTime);
    Out.ar(out, sigCombed);
}).add;
)
```

TODO Comb with noise examples

```{admonition} Relation between Filters and Delay
:name: def-delay-filter-relationship
:class: remark

*Delays* and *filtering* are intimately tied together.
Creating one almost always invariably creates the other!
```