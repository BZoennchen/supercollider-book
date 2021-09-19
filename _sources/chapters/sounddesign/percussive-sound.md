# Percussive Sound

A vibrating string is one of the main examples of a harmonic oscillator.
Many many instruments can be modelled by using and manipulating the harmonic series.

## The Physics of a Drum

However, there is an important class of musical oscillators that do not fit the simple harmonic model.
These 'non-harmonic' oscillators are just as important as their harmonic cousins, but they do not conform to the same set of rules.
Examples of these include drums, timpani, and many of the ethnic instruments now used as sound effects to spice up western music.
So why do these sound different and, more importantly, how can we imitate them?

Imagine a drum skin fixed at all points around its circumference.
Let's assume a perfect world in which the tension at all points on the surface of the skin is equal.
This drum skin or membrane can be interpreted as an oscillator.

The most important difference (with respect to the acoustic nature) between a string and a membrane is that a membrane is a two-dimensional object while the string is one-dimensional!
It is a surface rather than a line.

Let us imagine we hit the circular membrane at its center.
Clearly, at the points where the membrane is fixed it can not move up and down, that is, it can not oscillate.
If we look at a perpendicular slice (we reduce the dimension to one) of the membrane we would see a very similar motion compared to a string.

However, we can not just placing our finger one-third of the way from the center to the rim to create an overtone of exactly three times the frequency of the fundamental.
It is not that simple!
Instead the so called *Bessel function* tells us that the first zero point is 42.6 percent of the distance from the center to the rim.
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

Noise is a random signal having intensity at a wide range of frequencies.
For example, *white noise* has equal intensity at different frequencies, giving it a constant power spectral density.
Let us listen to *white noise* using ``WhiteNoise``.

```isc
{WhiteNoise.ar(0.25!2)}.play;
```

Note that we can not define the frequency since noise consist of a wide range of frequencies.
This sounds similar to a FM radio while searching for a channel.

```{figure} ../../figs/sounddesign/whitenoise.png
---
width: 600px
name: fig-whitenoise
---
A plot of ``WhiteNoise`` over a duration of 2 milliseconds.
```

If we look at the frequency analyser, we can see almost a line, that is, all frequency have roughly equal power.
Therefore, the sound is kind of harsh.
To achieve a softer sound we can use ``PinkNoise``

```isc
{PinkNoise.ar(0.25!2)}.play;
```

For *pink noise* the spectrum falls off in power by 3 dB per octave.
The spectrum of *brown noise* ``BrownNoise`` falls even faster, that is, 6 dB in power per octave.
The so called *clip noise* ``ClipNoise`` is even a little more harsh than ``WhiteNoise``.
It generates a high frequency stream of 1, -1 with equal probability.

```{figure} ../../figs/sounddesign/clipnoise.png
---
width: 600px
name: fig-clipnoise
---
A plot of ``ClipNoise`` over a duration of 2 milliseconds.
```

The last available noise offered by the default **sclang** is ``GrayNoise`` which sounds very deep, like a heavy rain.

Using ``GraySound`` combined with a low frequency ``SinOsc`` controlled by an percussive envelope, we already achieve a quite convincing sound of a drum:

```isc
(
Ndef(\drum, {
    var sig, amp, n, env;
    env = EnvGen.kr(Env.perc(0.01, 0.5, 1.0, -8.0), doneAction: Done.freeSelf);
    sig = SinOsc.ar(140!2) * 1.2;
    sig = GrayNoise.ar(0.15!2) + sig;	
    sig = sig * env;
}).play;
)
```

Compare this to the ``WhiteNoise``:

```isc
(
Ndef(\drum, {
    var sig, amp, n, env;
    env = EnvGen.kr(Env.perc(0.01, 0.5, 1.0, -8.0), doneAction: Done.freeSelf);
    sig = SinOsc.ar(140!2) * 1.2;
    sig = WhiteNoise.ar(0.15!2) + sig;	
    sig = sig * env;
}).play;
)
```

## Bells

Very different from string and wind instruments, bells consists of many inharmonic 'partials'.
So let us try a bunch of ``SinOsc`` using random frequencies between some range.

```isc
(
Ndef(\bell, {
    var freq, sig, env, amp;
    amp = 0.2;

    Mix.ar(
    {
        freq = rrand(100, 5000);
        env = EnvGen.kr(envelope: Env.perc(0.001, 500/freq), gate: Dust.kr(0.05));
        sig = SinOsc.ar(freq) * env;
        sig = sig * amp;
        sig = Pan2.ar(sig, rrand(-1.0, 1.0));
    }.dup(100));
}).play;
)
```
