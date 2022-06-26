# Percussive Sound

A vibrating string is one of the main examples of a harmonic oscillator.
Many many instruments can be modelled by using and manipulating the harmonic series.
However, there is an important class of musical oscillators that do not fit the simple harmonic model.
These *non-harmonic* or *inharmonic* oscillators are just as important as their harmonic cousins, but they do not conform to the same set of rules.
Examples of these include drums, timpani, and many of the ethnic instruments now used as sound effects to spice up western music.
So why do these sound different and, more importantly, how can we imitate them?

## The Physics of a Drum

Imagine a drum skin fixed at all points around its circumference.
Let's assume a perfect world in which the tension at all points on the surface of the skin is equal.
This drum skin or membrane can be interpreted as an oscillator.

The most important difference (with respect to the acoustic nature) between a string and a membrane is that a membrane is a two-dimensional object while the string is one-dimensional!
It is a surface rather than a line.

Let us imagine we hit the circular membrane at its center.
Clearly, at the points where the membrane is fixed it can not move up and down, i.e., it can not oscillate there.
If we look at a perpendicular slice (we reduce the dimension to one) of the membrane we would see a very similar motion compared to a string.

However, we can not just placing our finger one-third of the way from the center to the rim to create an overtone of exactly three times the frequency of the fundamental.
It is not that simple!
Instead, the so called *Bessel function* tells us that the first zero point is 42.6 percent of the distance from the center to the rim.
The next odd harmonic of the vibrating string has five equally spaced sections, and oscillates at exactly five times the fundamental frequency.
The equivalence for the circular drum skin has zero points at 27.8 percent and 63.8 percent of distance from the center to the rim, and it oscillates at a frequency 3.6 times that of the fundamental.

If, for some reason, we do not hit the drum exactly in the center -- how dare we are -- it vibrates in completely different ways.
Hitting a drum will result in a number of simultaneously different oscillation modes.
However, they will all have different amplitudes and decay rates.
This makes the drum's sound enormously complex and **impossible to emulate using the types of waveforms produced by a simple harmonic oscillator**.

To make things even more difficult, a real drum skin will have slight variations in tension across its surface.
Hitting a drum harder will result in a higher pitch.
Therefore, the fundamental frequency is in some way related to the displacement of the membrane!

So what shall we do?
Admit defeat and concede?
Well, yes and no!
We can not emulate a drum by recreating each of its harmonics, for example by using [additive synthesis](sec-additive-synthesis), that would be impossible because it would be too computational expensive.
What we need is noise!

## Noise

If we define richness by the number of sine waves that are represented in a sound, then arguable the richest is pure noise.
Interestingly this corresponds to the *theory of information* where a random message will eliminate the most amount of uncertainty thus has a high *entropy*.
In section [Additive Synthesis](sec-additive-synthesis) we have noticed that the greater the number of enharmonic spectral elements there were, the more the sound approaches noise.
In other words, if add more and more sine waves, each with a random frequency, we will eventually and up with noise -- the richest signal possible.

Noise is often defined as all possible frequencies having equal representation.
We can also define it as a wave with no pattern or maybe as a series of numbers of which we can not recognize its pattern.

In a more general sense, noise is a random signal having intensity at a wide range of frequencies.

### White Noise

*White noise* has equal intensity at different frequencies, giving it a constant power spectral density.
Let us listen to *white noise* using ``WhiteNoise``.

```isc
{WhiteNoise.ar(0.25!2)}.play;
```

Note that we can not define the frequency since noise consist of a wide range of frequencies.
*White noise* sounds similar to a FM radio while searching for a channel.

```{figure} ../../figs/sounddesign/whitenoise.png
---
width: 600px
name: fig-whitenoise
---
A plot of ``WhiteNoise`` over a duration of 2 milliseconds.
```

If we look at the frequency analyser, we can see almost a line, i.e., all frequency have roughly equal power.
Compared to other noises, the sound is rather of harsh because of the power in high frequencies.

(sec-pink-noise)=
### Pink Noise

To achieve a softer sound we can use ``PinkNoise``.
*Pink noise* is exponentially biased towards lower frequencies.
It has equal energy per octave band (musical octaves are exponential).

```isc
{PinkNoise.ar(0.25!2)}.play;
```

For *pink noise* the spectrum falls off in power by 3 dB per octave.
It sounds more natural and full than *white noise* because it corresponds with the way we hear musical octaves.
White noise appears brighter and thinner.
Pink noise appears in nature at many places.

### Brown Noise

The spectrum of *brown noise* ``BrownNoise`` falls even faster, that is, 6 dB in power per octave.

### Clip Noise

The so called *clip noise* ``ClipNoise`` is even a little more harsh than ``WhiteNoise``.
It generates a high frequency stream of 1, -1 with equal probability.

```{figure} ../../figs/sounddesign/clipnoise.png
---
width: 600px
name: fig-clipnoise
---
A plot of ``ClipNoise`` over a duration of 2 milliseconds.
```

### Gray Noise

The last available noise offered by the default **sclang** is ``GrayNoise`` which sounds very deep, like a heavy rain.

### Reconstruction of Noises

We can create noise using [additive synthesis](sec-additive-synthesis).
Let us use 1000 oscillators, that is, ``UGens``.
For pink noise we need an exponential distribution of frequencies while for white noise a linear distribution is required.

```isc
(
Ndef(\pink_noise, {
    var sig;
    sig = Mix.fill(1000, {SinOsc.ar(exprand(1.0, 20000))})*0.001;
    sig;
}).play;
)
```

```isc
(
Ndef(\white_noise, {
    var sig;
	sig = (Mix.fill(1000, {SinOsc.ar(rrand(1.0, 20000))})*0.001)!2;
	sig
}).play;
)
```

On my machine, the CPU is at 20 percent.
Using ``WhiteNoise`` or ``PinkNoise`` leads to almost no CPU workload.

## Examples

### Drums

To generate a drum like sound we start with two components:

1. a noise generator, and
2. a sine wave.

The noise generator approximates the complex sound of the wobbling drum membrane while the sine wave adds the typical *base of impact*.
Using *gray noise* combined with a low frequency ``SinOsc`` controlled by an percussive envelope, we already achieve a quite convincing sound of a drum:

```isc
(
Ndef(\drum1, {
    var sig, amp, n, env;
    env = EnvGen.kr(Env.perc(0.01, 0.5, 1.0, -8.0), doneAction: Done.freeSelf);
    sig = SinOsc.ar(140!2) * 1.2;
    sig = GrayNoise.ar(0.15!2) + sig;	
    sig = sig * env;
}).play;
)
```

Changing the noise generator leads to a different timbre.
For example, compare this to the ``WhiteNoise``:

```isc
(
Ndef(\drum2, {
    var sig, amp, n, env;
    env = EnvGen.kr(Env.perc(0.01, 0.5, 1.0, -8.0), doneAction: Done.freeSelf);
    sig = SinOsc.ar(140!2) * 1.2;
    sig = WhiteNoise.ar(0.15!2) + sig;	
    sig = sig * env;
}).play;
)
```

### A Stormy Night

The natural way to work with noise is to apply filters.
In the following, I use a resonant low pass filter ``RLPF`` to filter *pink noise*.
The cutoff frequency and the quality of the resonance is controlled via ``LFNoise2`` at a low frequency.
The result sounds like a stormy night:

```isc
// Storm simulation
(
Ndef(\breeze, {
    var sig, cut, res;
    sig = PinkNoise.ar() * 0.7;
    cut = LFNoise2.kr(1).range(600, 1200);
    res = LFNoise2.kr(1).range(0.001, 1.0);
    sig = RLPF.ar(sig, cut, res);
    sig = Pan2.ar(sig, LFNoise2.ar(0.5).range(-0.5, 0.5));
}).play;
)
```

### Bells

Very different from string and wind instruments, bells consists of many inharmonic partials.
In the section [additive synthesis](sec-additive-synthesis), we already constructed the sound of a bell using the sum of multiple sine waves ``SinOsc``:

```isc
(
Ndef(\bell_additive, {
    var sig, inharmonics, env, partials = 10;
    env = EnvGen.ar(Env.perc(
        attackTime: 0,
        releaseTime: {rrand(1.0, 3.0)}!partials,
        level: {rrand(0.3, 1.0)}!partials),
    gate: Impulse.kr(1)
    );

    inharmonics = Array.fill(partials, {rrand(100, 1200)});
    sig = SinOsc.ar(inharmonics) * partials.reciprocal * env;
    sig = Splay.ar(sig);
    sig;
}).play;
)
```

We can achieve the same by using a special *unit generator* that is built to generate the sum of sine waves.
[Klang](http://doc.sccode.org/Classes/Klang.html) is a bank of sine oscillators that takes arrays of frequencies, amplitudes and phase as arguments.
It allows us to specify a set of frequencies to be filtered and **resonated**, matching amplitudes, and decay rates.
This is part of *physical modelling* where we try not to replicate the sound directly but indirectly by modelling the bodies that generate it.


```isc
(
Ndef(\bell_physical, {
    var chime, freqSpecs, sig, sigBurst, totalHarm = 10;
    var envBurst, burstLength = 0.0001;

    envBurst = EnvGen.kr(Env.perc(attackTime: 0, releaseTime: burstLength), gate: Impulse.kr(1));
    sigBurst = PinkNoise.ar() * envBurst; // scale factor multipied by all frequencies at init time

    freqSpecs = `[
        {rrand(100, 1200)}.dup(totalHarm),                         // freqs
        {rrand(0.3, 1.0)}.dup(totalHarm).normalizeSum.round(0.01), // amps
        {rrand(1.0, 3.0)}.dup(totalHarm)];                         // ring times (decaying)

    sig = Klank.ar(freqSpecs, sigBurst) * totalHarm.reciprocal;
    sig;
}).play;
)
```

Both versions sound quite similar.