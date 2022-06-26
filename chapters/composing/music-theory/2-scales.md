(sec-scales)=
# Scales

A *musical scale (Tonleiter)* is an ordered set of pitches, together with a formula for specifying their frequencies.
Each individual pitch of a scale is called a *degree (Tonstufe)*.

Most musical traditions use *octave intervals* to associate pitches that serve the same musical function (inison) such that a scale is completely defined by one *octave* because of *octave equivalence*.
In that case, any *degree* is a member of a class that it shares with the same degree in all other octaves.
*Degrees* of a scale are sometimes called *pitch classes*.

```{admonition} Intervals and Pitches 
:name: remark-interval-vs-pitches
:class: remark
The actual pitches within a scale are less important than their relation, i.e. the *interval* between pitches/frequencies.
```

```{figure} ../../../figs/composing/piano-keys.png
---
width: 400px
name: fig-piano-keys
---
The notes of an octave mapped on piano keys.
Each consecutive *interval* is equal to $\sqrt[12]{2}$.
The white keys give us the C major scale (diatonic scale).
Above one can see the number of semitones of each interval of the major scale.
```

## Chromatic Scale

The *chromatic scale*, which translates to *colorful scale*, consists of all twelve keys we know from a piano:

$$\text{C, C#, D, D#, E, F, F#, G, G#, A, A#, B}.$$

On an equally tempered piano, i.e., if the frequency of degree $d_i$ is $f_i$ then

\begin{equation}
    f_{i+1} = f_{i} \cdot 2^{1/12}
\end{equation}

for all $i$.
Note that, for example, C# (C raised by a semitone) and Db (D lowered by a semitone) are represented by the same keys on the piano.
In that case, consecutive degrees are apart 100 [cents](sec-intervals).
Compare the following code that plays the *chromatic scale*.

```isc
(
Pbindef(\melody,
    \instrument, \default,
    \scale, Scale.chromatic,
    \degree, Pseq((0..11), inf),
    \octave, 3,
    \dur, 0.25,
    \amp, 1
).play;
)
```

We can also print out the *cents* for each degree.

```isc
Scale.chromatic.cents;
```

```{figure} ../../../figs/composing/chromatic-scale.png
---
width: 600px
name: fig-chromatic-scale
---
The chromatic scale on a note sheet.
```

## Diatonic Scale (Major Scale)

Western music's prototype of all scale system is the *diatonic scale*.
It is also known as the *major scale*.

```isc
Scale.major.cents;
```

Instead of twelve, it has only seven pitches per octave, named with the seven letters C, D, E, F, A, and B corresponding to the seven *degrees* of this scale.
In German, it's C, D, E, F, A, H.
The diatonic scale contains two-interval sizes, the *half step* (*semitone*) and the *whole step* where a *whole step* (*whole tone*) contains exactly two *half steps*.
A half step is equal to 100 and a whole step to 200 cents.

The *interval order* 

\begin{equation}
    (2,2,1,2,2,2,1)_{\text{major}}
\end{equation}

of the diatonic scale is the sequence of whole and half steps in the scale.
It is reflected by the piano keys but hidden by the notation of a note sheet.
The group $(2,2,1)$ is followed by $(2,2,2,1)$.
The unique order of whole and half steps provide a crucial asymmetry that our hearing exploits in order to orient ourselves.

## Minor Scales

The *minor scale*, also known as *natural minor scale*, uses the standard *diatonic interval order* but starts on degree 6 (counting from one).
The natural minor is also known as the *Aolian [mode](sec-modes)*.

\begin{equation}
    (2,1,2,2,1,2,2)_\text{nat. minor}
\end{equation}

This gives us: C, D, Eb, F, G, Ab, Bb.

```{admonition} Counting in sclang
:name: attention-sc-counting
:class: attention
Note that in ``sclang``, we start counting from zero!
```

There is also the *harmonic minor scale* for which the seventh note is raised by one semitone. 

\begin{equation}
    (2,1,2,2,1,3,1)_\text{ham. minor}
\end{equation}

This gives us: C, D, Eb, F, G, Ab, B.

The last variation is the *melodic minor scale* for which the sith and seventh notes are always raised.

\begin{equation}
    (2,1,2,2,2,2,1)_\text{mel. minor}
\end{equation}

This gives us: C, D, Eb, F, G, A, B.