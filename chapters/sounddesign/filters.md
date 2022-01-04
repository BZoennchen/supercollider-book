(sec-filters)=
# Filters

The very basic understanding of filters might be that they just make parts of the signal quieter -- which is wrong.
They do far more than just attenuate some frequencies.
We have to understand phase relationships to really understand whats going on.

## Phases

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

What is happing if we combine two sawtooth waves such that the fundamental frequencies of these two signals cancel each other out?
Since ``Saw`` has no parameter for the phase, we reconstruct the wave by using 25 sine waves:

```isc

({
    arg freq = 300, fundAmp = 0.2;
    var numHarmonics = 25;
    var sig = [0, 0];
    for(1, numHarmonics, { |n|
        var hFreq = freq * n;
        var phase = pi * hFreq / freq;
        sig = sig + SinOsc.ar(hFreq ! 2, phase, fundAmp/n) + SinOsc.ar(hFreq ! 2, 0, fundAmp/n)
    });
    sig ! 2 * 0.5;
}.play;
)
```

Compare this to the sound of a regular sawtooth wave:

```isc
{Saw.ar(300!2)}.play
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
This filter is called *comb filter*.
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
    var sig = Saw.ar(200 ! 2);
    sig = sig + DelayL.ar(sig, maxdelaytime: 0.2, delaytime: 1/(2*200)) * 0.5;
    sig;
}.play;
)
```

## Phasing & Filtering

If we speak of filters we often man low pass or high pass filters, that is, filters that filter frequencies above or below some cutoff frequency.
For example the low pass filter ``LPF`` in **sclang** is a 2nd order Butterworth lowpass filter.

```{figure} ../../figs/sounddesign/butterworth-filter.png
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
    var sig = Saw.ar(500) ! 2 * 0.5;
    sig = HPF.ar(sig, 200);
    sig = LPF.ar(sig, 300);
    sig
}.play;)

({
    var sig = Saw.ar(500) ! 2 * 0.5;
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
    var sig = Saw.ar(500) ! 2 * 0.5;
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
How a musical instrument resonate has a great effect on the color of its sound.

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