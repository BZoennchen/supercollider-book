---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Drones

In this section, we try to create an ambient drone sound.
Drones are great building blocks.
They can stand on their own or be part of the background texture of our sound.
They can be stale or slowly moving using modulation at control rate.
Due to multichannel expansion and *unit generator argument modulation*, SuperCollider is a powerful tool for creating all kinds of drones with a view lines of code.
I find it much more challenging to create an exciting melody than to construct interesting drones.

## Basics

A fundamental building block of drones is the *beating effect*.
If we combine two *waveforms* of slightly detuned frequency, we can clearly hear the difference in frequency.
The result is a *beating effect* where the frequency of the beating is the difference of the two detuned frequencies.
Take, for example, two slightly detune [sine waves](sec-sine-wave):

```isc
{SinOsc.ar(90 * [1, 1.01]) * 0.8}.play;
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/sine-low-freq.mp3'
ipd.Audio(audio_path)
```

The frequency difference is 1%.
We hear a *beating* of frequency $(1.01-1.0) \cdot 90 = 0.9$ Hz.
Switching to a sawtooth wave makes the sound more drone-like because there is a multiple frequency beating.
The beating frequencies are 
$f_{\Delta} \cdot k,$
where
$k \in \mathbf{N}$ and $f_{\Delta}$
is the difference between the two fundamental detuned frequencies.

```isc
{LPF.ar(Saw.ar(90 * [1, 1.01]), 90*2)}.play;
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/saw-simple-drone.mp3'
ipd.Audio(audio_path)
```

One way to improve the movement within the sound we can try to modulate the beating frequencies.

```isc
{LPF.ar(Saw.ar(90 * [1, 1.0+LFNoise1.kr(0.1).bipolar(0.5)]), 90*2)}.play;
```

```{code-cell} python3
:tags: [remove-input]
import IPython.display as ipd
audio_path = '../../../sounds/saw-simple-drone-noise.mp3'
ipd.Audio(audio_path)
```

## Sawtooth Waves

Ok, this drone becomes boring pretty fast, but it is still astonishing how easy it is to create a basic drone.
Let's try multiple detuned harmonics using a combination of [sawtooth waves](sec-sawtooth-wave).
In the following I use sawtooth waves with frequencies $f_1, \ldots f_n$, where

$$f_i(t) \approx f \cdot \frac{1}{i} \cdot (1+\epsilon(t))$$

with $f$ being the fundamental frequency and $\epsilon(t) \in [-0.06;0.06]$.
The sawtooth resonates at frequency 

$$f \cdot i.$$

A *resonance low pass filter* is used to filter out high frequencies.
Moreover, I added additional movement to the sound using low frequency modulation, noise, distortion, and panning.
[Balance2](https://doc.sccode.org/Classes/Balance2.html) is similar to a panning ([Pan2](https://doc.sccode.org/Classes/Pan2.html)) but for a *stereo signal*.
I let the stereo signal move from left to right.

```isc
(
SynthDef(\drone_saws, {
    arg freq = 75;
    var sig, detuner, env;
    sig = Array.fill(8, {arg i;
        var freqNoise = LFNoise1.kr(Rand(0.05, 0.2)).bipolar(1.0).midiratio;
        RLPF.ar(
            in: Saw.ar(freq * (i+1).reciprocal * freqNoise * [1.0, 1.01]).distort,
            freq: freq*(i+1),
            rq: SinOsc.kr(Rand(0.05, 0.2)).range(0.4, 1.0),
            mul: SinOsc.kr(0.11).range(0.5, 0.9) * (i+1).reciprocal
        );
    }).sum;

    env = EnvGen.kr(Env(
        levels: [0, 1, 1, 0],
        times: [\atk.kr(6.0), \sus.kr(4.0), \rel.kr(6.0)]), doneAction: Done.freeSelf);

    sig = Balance2.ar(sig[0], sig[1], pos: LFNoise1.kr(0.1).bipolar(0.85));
    sig = sig * env * \amp.kr(1.0);
    Out.ar(0, sig);
}).add;
)

Synth(\drone_saws, [\freq, 200, \amp: 1.2]);
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/drone-saws.mp3'
ipd.Audio(audio_path)
```

## Triangle Waves

Other waveforms can also help us to construct a nice drone sound.
The following example, which I found on the [sccode website](https://sccode.org/1-4SS), uses four (low-frequency) [triangle waves](sec-triangle-wave), i.e., [LFTri](https://doc.sccode.org/Classes/LFTri.html).

```isc
(
{
    FreeVerb.ar(
        (1-LFTri.ar(Line.ar(147,5147,1200,1,0,2)))
        * (1-LFTri.ar(Line.ar(1117,17,1200,1,0,2)))
        * (1-LFTri.ar(100))
        * (1-LFTri.ar([55,55.1]))
        *0.05
        ,0.7
        ,1
    );
}.play
)
```

Since there is a lot of duplicated code we can simplify its implementation:

```isc
({
    h={|f| 1-LFTri.ar(f)};
    l={|s,e| Line.ar(s,e,1200,1,0,2)};
    FreeVerb.ar(h.(l.(147,5147))*h.(l.(1117,17))*h.(100)*h.([55,55.1])*0.05,0.7,1);
}.play;
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/drones-tri-waves.mp3'
ipd.Audio(audio_path)
```

The function $h(f)$ generates a signal $h(f)(t)$ that oscillates in a linear fashion, ascending from 0 to 2 and then descending back to 0, and so on.
$l(s,e)(t)$ on the other hand is a line that goes from $s$ to $e$ in 1200 seconds, i.e, 20 minutes.
Let us reduce this duration to 30 seconds and listen again:

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/drone-tri-wave-short.mp3'
ipd.Audio(audio_path)
```

## Wavetable Morphing

Let us try something different.
Let's use different [wavetables](sec-wavetable) and let us morph from one wavefrom into another but slowly.
First we create mutiple signals.
To do so lets define a function that returns a random wavetable.

```isc
(
~funcRandSignal = {
    arg nLevels=12;
    var levels = [0]++ {
        var levs, peak;
        levs = {rrand(-1.0,1.0)}!(nLevels-2);
        peak = levs.abs.maxItem;
        levs = levs * peak.reciprocal;
    }.value ++ [0];

    Env(
        levels, 
        {exprand(0.01,1)}!(nLevels-1), 
        {exprand(0.1,4)}!(nLevels-1)
    )
}
)
```

Now we can create ``n`` wavetables and fill them into ``n`` consecutive buffers.
I use a [Routine](sec-routines-tasks) such that if we compute the code multiple times, buffers will be cleared.

```isc
(
n = 4;
fork {
    Buffer.freeAll(s);
    s.sync;
    ~buffers = Buffer.allocConsecutive(n, s, 1024);
    ~buffers.do({
        arg buf, i;
        buf.loadCollection(~funcRandSignal.());
    });
}.play;
)
```

Using [VOsc]() we can interpolate between multiple wavetable buffers if they are aligned consecutive and are all of the same size.
Here I use a simple synth definition with a fade-in and fade-out envelope, multiple detuned frequencies and multiple buffer positions randomly moving within ``[0;numBufs-1]``.
Note that if, for example, [LFNoise1](https://doc.sccode.org/Classes/LFNoise1.html) goes from ``0`` to ``3`` we sweep across 4 different wavetables in the same period another [LFNoise1](https://doc.sccode.org/Classes/LFNoise1.html) might goes from ``1`` to ``2``.
The more wavetables we use, the faster will sweep over them.

```isc
(
SynthDef(\vosc, {
    arg out=0, buf=0, numBufs=2, freq=60, amp=0.2;
    var sig, bufpos, detuneSig;

    detuneSig = LFNoise1.kr(0.2!8).bipolar(0.2).midiratio;
    bufpos = buf + LFNoise1.kr(0.5).range(0, numBufs-1);
    sig = VOsc.ar(bufpos, freq*detuneSig);
    sig = Splay.ar(sig);
    sig = LeakDC.ar(sig);
    sig = sig * amp * Env([0,1,1,0], [3,30,3]).ar(doneAction: Done.freeSelf);

    Out.ar(out, sig);
}).add;
)
```

Now let's use everything by starting multiple ``\vosc`` synth one after the other.

```isc
(
fork {
    s.sync;
    [50, 70, 65, 150, 200].do {|freq|
        Synth(\vosc, [\freq: freq, \buf: ~buffers[0].bufnum, \numBufs: n]);
        5.wait;
    }
}
)
```

```{code-cell} python3
:tags: [remove-input]
audio_path = '../../../sounds/drone-wavetable.mp3'
ipd.Audio(audio_path)
```