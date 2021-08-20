(sec-am)=
# Amplitude Modulation

If we modulate (change a value over time) the amplitude of a audible signal we call this *amplitude modulation* (AM).
As we will see it the frequency range of the modulation has a great effect on the result.
But first, let's do some simple math.

## Theory

Within this section I use the the cosine function instead of the sine because the math becomes a little simpler.
Our basic waveform might be a simple cosine with an amplitude $A(t)$ and a frequency $f$:

\begin{equation}
y(t) = A(t) \cdot \cos(2 \pi f_\text{car} t)
\end{equation}

In AM the amplitude is itself a function over time $A(t)!
Let us assume

\begin{equation}
A(t) = A_\text{car} + A_\text{mod} \cdot \cos(2 \pi f_\text{mod} t)
\end{equation}

then our audio signal is defined by

\begin{equation}
y(t) = \left[A_\text{car} + A_\text{mod} \cdot \cos(2 \pi f_\text{mod} t) \right] \cdot \cos(2 \pi f_\text{car} t)
\end{equation}

which we can rewrite as

\begin{equation}
y(t) = A_\text{car} \cdot \cos(2 \pi f_\text{car} t) + A_\text{mod} \cdot \cos(2 \pi f_\text{mod} t) \cdot \cos(2 \pi f_\text{car} t)
\end{equation}

We can now use the cosine rule for multiplication, which gives us

\begin{equation}
\begin{split}
y(t) = \ & A_\text{car} \cdot \cos(2 \pi f_\text{car} t) \ + \\
\ & \frac{1}{2} A_\text{mod} \cdot \cos(2 \pi (f_\text{car} + f_\text{mod}) t) \ + \\
\ & \frac{1}{2} A_\text{mod} \cdot \cos(2 \pi (f_\text{car} - f_\text{mod}) t).
\end{split}
\end{equation}

This looks complicated but if we look at the Fourier transformation of $y(t)$ we can identify three frequencies within the spectrum:

1. the carrier frequency $f_\text{car}$ with an amplitude $A_\text{car}$,
2. the sum of the carrier and modulation frequency $f_\text{car} + f_\text{mod}$ with an amplitude of $1/2 A_\text{mod}$ and
3. the difference of the carrier and modulation frequency $f_\text{car} - f_\text{mod}$ with an amplitude of $1/2 A_\text{mod}$.

## Effect

If the modulation frequency is low, that is, in the range of $0$ and $20$ Hz, we can recognize a amplitude modulation by the change of amplitude in $y(t)$.
However, if we choose a modulation frequency in the range of audible frequencies, we no longer really modulate the amplitude of the signal $y(t)$ but the frequencies of the signal.

For example, if we use A_\text{car} = A_\text{mod} = 1$ and $f_\text{car} = 400$ Hz, $f_\text{mod} = 250$ Hz, the signal consists of three frequencies:

1. $400$ Hz (center)
2. $400 + 250 = 650$ Hz (sum) and
3. $400 - 250 = 150$ Hz (difference), compare {numref}`Fig. {number} <fig-am-frequencies>`.

We can listen to this effect using the following code:

```isc
(
Spec.add(\freq, [100, 600]);
Spec.add(\freqmod, [0.01, 600]);
Spec.add(\ampcar, [0, 1]);
Spec.add(\ampmod, [0, 1]);

Ndef(\am, {
    var sig, amp;
    amp = \ampcar.kr(1) + (\ampmod.kr(1) * SinOsc.ar(\freqmod.kr(5), 0.5*pi));

    sig = SinOsc.ar(\freq.kr(200), 0.5*pi);

    sig = sig * amp * (1/3) ! 2;
}).play;
)

Ndef(\am).gui
```

Try out different values and observe the resulting sound.


```{figure} ../../figs/sounddesign/am-frequencies.png
---
width: 200px
name: fig-am-frequencies
---
Snapshot of the stethoscope using a logarithmic frequency scale ($x$-axis).
I use $A_\text{car} = A_\text{mod} = 1$ and $f_\text{car} = 400$ Hz, $f_\text{mod} = 250$ Hz. 
```

## Techniques

In our example above we used a fixed modulation frequency, that is, if we change the carrier frequency it stays constant.

### Direct Current

If we use, for example, $f_\text{car} = f_\text{mod} = 100$ Hz we achieve frequencies equal to $0$, $100$ and $200$ Hz.
Zero means no oscillation which results in an offset ($y$-axis) of the signal.
We call this a DC (direct current).

The following code generates a plot such that you can observe this effect.

```isc
({
    var sig, amp;
    amp = \ampcar.kr(1) + (\ampmod.kr(1) * SinOsc.ar(\freqmod.kr(100), 0.5*pi));

    sig = SinOsc.ar(\freq.kr(100), 0.5*pi);
    sig = sig * amp * (1/3);
    sig
}.plot(1/100))
```

The result is depicted in {numref}`Fig. {number} <fig-am-dc-effect>`.
All values $y(t)$ are shifted up, that is, in positive $y$-'direction'.

```{figure} ../../figs/sounddesign/am-dc-effect.png
---
width: 600px
name: fig-am-dc-effect
---
DC (direct current) results in an offset of the signal.
```

This effect can be avoided by using the ``LeakDC`` unit generator

```isc
({
    var sig, amp;
    amp = \ampcar.kr(1) + (\ampmod.kr(1) * SinOsc.ar(\freqmod.kr(100), 0.5*pi));

    sig = SinOsc.ar(\freq.kr(100), 0.5*pi);
    sig = sig * amp * (1/3);
    sig = LeakDC.ar(sig);
    sig
}.plot(1/100))
```

gives

```{figure} ../../figs/sounddesign/am-avoided-dc-effect.png
---
width: 600px
name: fig-am-avoided-dc-effect
---
We can avoid DC (direct current) by using ``LeacDC``.
```

### Clangorous Sound

If we play different notes by changing the carrier frequency without changing the modulation frequency, we get a non-harmonic clangorous sound.
The relationship between the frequency remains fixed offset such that for a high carrier / center frequency, the sum and difference frequencies are closer to the center frequency compared to low center frequencies.

For almost all carrier frequencies there are no harmonics present in the signal.
This leads to a rather clangorous sound.
This can be used to create aggressive and conventionally 'unmusical' sounds that change dramatically as one plays up and down the keyboard.

We can control the amount of clangour by raising or lowering the level of the modulator $A_\text{mod}$.

### Harmonic and inharmonic timbres

Let us introduce a ratio $r$ between the carrier frequency and the modulation frequency such that:

\begin{equation}
f_\text{mod} = r \cdot f_\text{car}.
\end{equation}

which results in frequencies $f_\text{car}$ and

\begin{equation}
f_\text{car} \pm f_\text{mod} = f_\text{car} \pm r \cdot f_\text{car} = (1 \pm r) \cdot f_\text{car}.
\end{equation}

$r$ should be smaller or equals than $1$.

```isc
(
Spec.add(\freq, [100, 600]);
Spec.add(\ratio, [0.0, 10]);
Spec.add(\ampcar, [0, 1]);
Spec.add(\ampmod, [0, 1]);

Ndef(\am, {
    var sig, amp, freqmod;
    freqmod = \radio.kr(1) * \freq.kr(200);
    amp = \ampcar.kr(1) + (\ampmod.kr(1) * SinOsc.ar(freqmod, 0.5*pi));

    sig = SinOsc.ar(\freq.kr(200), 0.5*pi);

    sig = sig * amp * (1/3) ! 2;
}).play;
)
```

If the ratio is an integer we get a harmonic relationship but this is a special case!
In general the relationship is inharmonic and we increase the inharmonicity we use a ratio which is far away from a whole number!

Remember the frequencies the signal has are $(1 \pm r) \cdot f_\text{car}$ and $f_\text{car}$.
So the coefficients in order they are:

\begin{equation}
(1 - r), 1, (1 + r).
\end{equation}

For example, this gives us:

+ $r=1/4$: $3/4, 1, 5/4$
+ $r=1/2$: $1/2, 1, 3/2$
+ $r=1/1$: $0, 1, 2$
+ $r=2/1$: $-1, 1, 3$
+ $r=3/2$: $-1/2, 1, 5/2$
+ ...
