(sec-fm)=
# Frequency Modulation (FM)

As the name indicates, applying frequency modulation means to modulate the frequency of a signal.
In other words, we change the frequency of a signal over time.

FM for sound design was discovered by John Chowning by accident in the mid-'60s.
He wanted to generate vibrato effects but noticed that when he increased the modulating frequency, a new complex sound appears.
FM is the most common encoding technique for public radio transmission (hence 'FM' radio) by using frequencies which out of the limits of human hearing.
Chowning pushed for commercial use but none of the American manufacturers saw the potential of FM.
In desperation, Stanford turned to the Japanese manufacturer Yamaha.
As a consequence of the success of FM synthesis, the company sold millions of FM synthesizers, organs and home keyboards.

## Introduction

Let us start with the very basic equation of a sine wave.

\begin{equation}
y(t) = A \cdot \sin(2\pi f(t) \cdot t),
\end{equation}

where $t$ is the time, $f(t)$ is the frequency and $A$ the (maximal) amplitude.
$f(t)$ is not a constant but a function over time which looks like the following

\begin{equation}
f(t) = \left[ f_\text{car} + A_{\text{mod}} \cdot \sin(2\pi f_{\text{mod}} \cdot t) \right].
\end{equation}

In summary we get

\begin{equation}
y(t) = A_{\text{car}} \cdot \sin(2\pi \left[ f_\text{car} + A_{\text{mod}} \cdot \sin(2\pi f_{\text{mod}} \cdot t) \right] \cdot t),
\end{equation}

which looks very intimidating but don't worry and just experiment with it!

$f_\text{car}$ is called carrier frequency, $f_{\text{mod}}$ modulator frequency and $A_{\text{car}}$, $A_{\text{mod}}$ are the respective amplitudes.
Those numbers and their relation influence the generated sound fundamentally.
We can also use different oscillators and modulate the frequency of the most outer oscillator by multiple modulators!

FM is a very powerful technique to generate a rich spectrum in a very computational efficient way.
Above we only use two oscillators but as you will see, we already achieve a quite complex spectrum.

## Vibrato

If the frequency of the modulator $f_{\text{mod}}$ is small, than we achieve a so called vibrato effect.
Try the following code snippet!

```isc
(
Ndef(\fm_low_mod, {
    var freq = 300;
    var mod = SinOsc.ar(freq/100)*5;
    SinOsc.ar(freq + mod) * 0.5 ! 2;
}).play;
)
```

Here we use 

\begin{equation}
f_{\text{mod}} = f_\text{car} \cdot 10^{-2}
\end{equation}

such that the $f_{\text{mod}}$ is two magnitudes smaller than the carrier frequency.
The effect is a cyclical squeezing and stretching of the carrier waveform.
It is astonishing how sensitive the human hearing is.
We recognize the low frequency within the overall sine wave, that is, we hear the slowly changing wave shape even if the change is very small.
Those small changes result in a vibration similar to the effect of a violinist moving her or his finger positioned on the string in slightly different positions.

```isc
(
Spec.add(\modfreq, [1, 600]);
Ndef(\fm_low_mod, {
    var mod = SinOsc.ar(\modfreq.kr(2)) * 5;
    SinOsc.ar(\freq.kr(200) + mod) * 0.5 ! 2;
}).play;
)
Ndef(\fm_low_mod).gui;
```

## Sirens

If we increase the modulation frequency $f_{\text{mod}}$ further and further such that it approaches, or even exceeds the carrier frequency $f_\text{car}$, we get a different effect.
At some point, the modulation becomes a form of distortion within the individual cycle of the carrier waveform.
To make the distortion more prominent, we have to increase the amplitude of the modulator -- a portion of the carrier frequency $f_{\text{car}}$ is a good starting point.

```isc
(
Spec.add(\modfreq, [1, 600]);
Ndef(\fm_low_mod, {
    var mod = SinOsc.ar(\modfreq.kr(2)) * \freq.kr(200);
    SinOsc.ar(\freq.kr(200) + mod) * 0.5 ! 2;
}).play;
)
Ndef(\fm_low_mod).gui;
```

In this case, the vibration becomes a wobbling effect or siren-type sound.

## Harmonic Relation

Let us look at this distortion by plotting $y(t)$ for $f_{\text{car}} = f_{\text{mod}} = \beta = 200$:

```isc
(
({
    var freq, mod, sig;
    freq = 200;
    mod = SinOsc.ar(freq) * freq;
    sig = SinOsc.ar(freq + mod);
    sig;
}).plot(1/(200));
)
```

```{figure} ../../figs/sounddesign/fm-cycle-high-freq.png
---
width: 400px
name: fig-fm-cycle-high-freq
---
One cycle of $y(t)$ for a high frequency modulation frequency.
```

If we look at the stethoscope we observe multiple side-bands, that is, there are multiple frequencies apart from the fundamental frequency (which is equals to the carrier frequency) present.
How many frequencies are present?
Well, in theory infinite amount!
Fortunately, there is a formula for the frequencies $f_{\text{sb},n^{\pm}}$ of the side-bands

\begin{equation}
f_{\text{sb},n^{\pm}} = f_{\text{car}} \pm n \cdot f_{\text{mod}},
\end{equation}

with $n \in \mathbb{N}$.

```{figure} ../../figs/sounddesign/fm-side-band-frequencies.png
---
width: 200px
name: fig-fm-side-band-frequencies
---
Snapshot of the stethoscope using a logarithmic frequency scale ($x$-axis).
```

If we want to keep the same side band relation for different carrier frequencies, we have to compute the modulation frequency based on the carrier frequency.
Therefore, it is useful to introduce a ratio:

\begin{equation}
r_{\text{mod}} = \frac{f_\text{car}}{f_\text{mod}}
\end{equation}

such that

\begin{equation}
f_\text{mod} = f_\text{car} \cdot r^{-1}_{\text{mod}}.
\end{equation}

## Side Band Amplitudes

The question now is: what about the amplitudes of the side bands?
We already observed what happens if the modulation frequency is low and we increase the modulator amplitude.
For low amplitudes we achieved a gently vibrato effect but for large amplitudes this transforms into a siren-type sound.

For high modulation frequencies we can transfer this phenomena.
The amplitude of the modulator will determine the amplitude of the side bands.
This implies that we can not control the amplitude of each individual side band.
We can only control their amplitudes as a whole!

Also, the amplitude of the modulator is not solely responsible for this effect but the relationship between it and the modulation frequency $f_{\text{mod}}$!
The so called *modulation index* gives us this relationship.
It is equal to the ratio of frequency deviation of $y(t)$ and the modulation frequency $f_{\text{mod}}$:

\begin{equation}
\beta(t) = A_{\text{mod}} \frac{d \sin(2\pi f_{\text{mod}} \cdot t)}{dt} \cdot f_{\text{mod}}^{-1}
\end{equation}

We can compute the *maximum modulation index* $\beta_{\text{max}}$ by

\begin{equation}
\beta_{ \text{max} } = \frac{ A_{\text{mod}} }{ f_{\text{mod}} }.
\end{equation}

If we want to have the approximately the same harmonic relationship for all keys on the keyboard, we have to change both $f_{\text{car}}$ and $f_{\text{mod}}$ accordingly while playing.
However, if we also want the same tone, we also have to adapt $A_{\text{mod}}$ such that $\beta_{ \text{max} }$ stays approximately constant, that is, we compute $A_{\text{mod}}$ by

\begin{equation}
A_{\text{mod}} = \beta_{\text{max}} \cdot f_{\text{mod}},
\end{equation}

and fix $\beta_{\text{max}}$ as we desire.

Ok, but wait, we still have no formula for the amplitude of each pair of sidebands with frequency $f_{\text{sb},n^{\pm}}$.
This amplitude is given by the *Bessel function (of first kind)*:

\begin{equation}
A_{ \text{sb},n^{\pm} } = J_n(\beta_\text{max}) = \sum^{\infty}_{k=0} \frac{ (-1)^k \cdot \left(\frac{\beta_\text{max}}{2}\right)^{n+2k} }{k! \cdot (n+k)!}.
\end{equation}

The series is a converging series and especially in our case where $\beta_\text{max}$ is not too large, the values of each term become very small very quick.

```{figure} ../../figs/sounddesign/bessel-function.png
---
width: 400px
name: fig-bessel-function
---
Plot of Bessel function of the first kind, $J_n(x)$, for integer orders $n = 0, 1, 2$. 
Figure made by Inductiveload - Own work, made with Inkscape, Public Domain, [link](https://commons.wikimedia.org/w/index.php?curid=3564725).
```

As we can see, $A_{ \text{sb},n^{\pm} }$ depends only on $\beta_\text{max}$ but oscillate for increasing $\beta_\text{max}$!

## Bandwidth

We stated that there are infinite amount of side bands.
In practice that not the case.
Furthermore, the amplitude of many of these side bands might be too low to be recognized by our ears.

As a rule of thump, the following formula gives an approximation of the bandwidth (where all side bands are contained in) of the signal:

\begin{equation}
2 \cdot f_\text{mod} \cdot (1 + \beta_{ \text{max} } ).
\end{equation}

Again the *modulation index* will determine the bandwidth.
The larger the index, the larger the bandwidth.

## Summary

Given $f_\text{car}$, $r_\text{mod}$, $\beta_\text{max}$ we compute $f_\text{mod}$ and  $A_\text{mod}$ by

\begin{gather}
f_\text{mod} = f_\text{car} \cdot r^{-1}_\text{mod}\\
A_\text{mod} = f_\text{mod} \cdot \beta_\text{max}.
\end{gather}

## Example

The following is an example FM synth, heavily inspired by the [tutorial](https://www.youtube.com/channel/UCypLRZiSlIQjsT_7J4Vz35Q/featured) given by [Alik Rustamoff](https://reflectives.bandcamp.com/track/ikaere) 
It uses the relations above but instead of using only one modulator we use three.
In the code ``f`` is $f_\text{car}$, ``modFreq1`` is $f_\text{mod}$, ``\ratio1`` is $r_\text{mod}$ and ``\modIndex1`` represents $\beta_text{max}$.
Furthermore, we added some naturalization (distortion and more) to achieve a more gentle result.

```isc
(
SynthDef(\fm, {
    var sig, f, car, env;
    var modFreq1, modFreq2, modFreq3, mod1, mod2, mod3, ampmod1, ampmod2, ampmod3;

    // noisy envelope
    env = EnvGen.ar(Env.perc(
        \att.kr(0.015) * Rand(0.8,1.2),
        \rel.kr(4.0) * Rand(0.9, 1.1),
        curve: \curve.kr(-4)
    ),
    doneAction: Done.freeSelf);
    env = env * PinkNoise.ar(1!2).range( 0.1, 1 ).lag(0.01);

    // f = f_car
    f = \freq.kr(220);

    // (6.13a) f_mod = f_car * r^{-1}_mod + distortion
    modFreq1 = f * \ratio1.kr(2).reciprocal + {Rand(-2, 2)}.dup;
    modFreq2 = f * \ratio2.kr(3).reciprocal + {Rand(-2, 2)}.dup;
    modFreq3 = f * \ratio3.kr(4).reciprocal + {Rand(-2, 2)}.dup;

    // (6.13b) A_mod = f_mod + beta_max
    ampmod1 = modFreq1 * \modIndex1.kr(1);
    ampmod2 = modFreq2 * \modIndex2.kr(0.5);
    ampmod3 = modFreq3 * \modIndex3.kr(0.8);

    // (partly 6.2 multiplied with env) A_mod * sin(2pi*f_mod t)
    // effectively reduces the modulation index beta_max over time
    mod1 = SinOsc.ar(modFreq1) * ampmod1 * env;
    mod2 = SinOsc.ar(modFreq2) * ampmod2 * env;
    mod3 = SinOsc.ar(modFreq3) * ampmod3 * env;

    // (6.1 or 6.3) y(t) = A_car * sin(f_car + A_mid * sin(2pi*f_mod t) t)
    car = \amp.kr(0.5) * SinOsc.ar(
        // f_car
        f +
        // changes the effective carrier frequency over time (low frequency) [\pm 5 * 10^{-3} * f_car; 0]
        LFTri.ar(env.pow(0.5) * LFNoise1.kr(0.3).range(1,5), Rand(0.0,2pi), mul: env.pow(0.2) * f * 0.005) +
        // distortion [-f/8; +f/8] but the noise is smoothen (its more like a Brownian motion.
        WhiteNoise.ar(f/8!2).lag(0.001) +
        // f_mod
        [mod1,mod2,mod3].sum);

    // add some envelope
    sig = car * env;
    sig = HPF.ar(sig, f);
    Out.ar(0, sig);
}).add;
)
```

Let us play the synth:

```isc
(
Pbind(
    \instrument, \fm,
    \dur, Pshuf(2.pow((-4..1)), inf),
    \degree, Pshuf([0, 2, 5, 6, 8, 11], inf),
    \octave, Pstutter(3, Pseq([3,4,5], inf)),
).play;
)
```