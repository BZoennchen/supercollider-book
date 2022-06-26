(sec-scales)=
# Scales

A *musical scale (Tonleiter)* is an ordered set of pitches, together with a formula for specifying their frequencies.
Each individual pitch of a scale is called a *degree (Tonstufe)*.

Most musical traditions use *octave intervals* to associate pitches that serve the same musical function (*unison*) such that a scale is completely defined by one *octave* because of *octave equivalence*, i.e., *The Basic Miracle of Music*.
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
The notes of an octave mapped onto piano keys.
Each consecutive key is a multiple of $\sqrt[12]{2}$ apart.
The white keys give us the C major scale ([diatonic scale](sec-diatonic-scale)).
Above, one can see the number of semitones of each interval of the major scale.
```

(sec-chromatic-scale)=
## Chromatic Scale

The *chromatic scale*, which translates to *colorful scale*, consists of all twelve keys we know from a piano:

$$\text{C, C#, D, D#, E, F, F#, G, G#, A, A#, B}.$$

It is an extension of the [diatonic scale](sec-diatonic-scale).
On an equally tempered piano, i.e., if the frequency of degree $d_i$ is $f_i$ then

\begin{equation}
    f_{i+1} = f_{i} \cdot 2^{1/12}
\end{equation}

for all $i$.
In that case, consecutive degrees are apart 100 [cents](sec-intervals).
Note that, for example, C# (C raised by a semitone) and Db (D lowered by a semitone) are represented by the same keys on the piano.
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

We can also print out the *cents* for each degree:

```isc
Scale.chromatic.cents;
```

```{figure} ../../../figs/composing/chromatic-scale.png
---
width: 800px
name: fig-chromatic-scale
---
The chromatic scale on a note sheet.
```

(sec-diatonic-scale)=
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

The *interval order* of the diatonic scale, defined by the following tuple,

\begin{equation}
    (2,2,1,2,2,2,1)_{\text{major}}
\end{equation}

is the sequence of whole and half steps in the scale.
Its *sparsity* (using only seven notes) gives each note in the scale a distinctive tone, while its *asymmetry* is an important property that gives each note in the scale a unique relation to the other notes; 
Together, *sparsity* and *asymmetry* provide the listener with a clear orientation within the scale.

The diatonic scale is reflected by the piano keys, but hidden by the notation of a note sheet, e.g., C and C# occupy the same note line.
The group $(2,2,1)$ is followed by $(2,2,2,1)$.

```{figure} ../../../figs/composing/diatonic-scale.png
---
width: 400px
name: fig-diatonic-scale
---
The diatonic scale on a note sheet.
```

## Minor Scales

The *minor scale*, also known as *natural minor scale*, uses the standard *diatonic interval order* but starts on degree 6 (counting from one).
We get the *minor interval order* by shifting the diatonic interval order by 2 to the right or by 5 to the left.
Therefore, it has the same *sparsity* as well as *asymmetry*. as the [diatonic scale](sec-diatonic-scale).

The *minor scale* is also called **natural minor** and is also known as the *Aolian [mode](sec-modes)*.

\begin{equation}
    (2,1,2,2,1,2,2)_\text{nat. minor}
\end{equation}

This gives us: C, D, Eb, F, G, Ab, Bb.

```{admonition} Counting in sclang
:name: attention-sc-counting
:class: attention
Note that in ``sclang``, we start counting from zero!
```

There is also the **harmonic minor scale** for which the seventh note is raised by one semitone. 

\begin{equation}
    (2,1,2,2,1,3,1)_\text{ham. minor}
\end{equation}

This gives us: C, D, Eb, F, G, Ab, B.

The last variation is the **melodic minor scale** for which the sith and seventh notes are always raised.

\begin{equation}
    (2,1,2,2,2,2,1)_\text{mel. minor}
\end{equation}

This gives us: C, D, Eb, F, G, A, B.

## SuperCollider Scales

Supercollider provides you with many well-known predefined scales.
You can look them up by calling:

```isc
Scale.directory
```

For example, we can use the *melodic minor* the following way:

```isc
(
Pbindef(\melody,
    \instrument, \default,
    \scale, Scale.melodicMinor,
    \degree, Pseq((0..7), inf),
    \octave, 4,
    \mtranspose, 0,
    \dur, 0.25,
    \amp, 1
).play;
)
```

But we can always create our own [Scale](https://doc.sccode.org/Classes/Scale.html).
It is defined by its *degrees*, the number of *pitches* per octave and the *tuninig* in semitones (100 cents).
In addition we can use ``descDegrees`` to play the scale differently when descending than when ascending.

In the following we define the *major scale*.

```isc
(
Scale(
    degrees: [0, 2, 4, 5, 7, 9, 11], 
    pitchesPerOctave: 12, 
    tuning: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0],
    descDegrees: nil,
    name: "my_minor"
);
)
```

If we want to use an *interval order* instead of *degrees* we can do so.
Let us first define a function that translates an order to degrees:

```isc
(
~intervalToDegrees = {arg array;
	var result = array.copy;
	var sum = 0;
	result[0] = 0;
	for(0, array.size-2, {arg i;
		result[i+1] = result[i]+array[i];
	});
	result;
}
)
```

We can call the function to generate degrees.

```isc
~majorIntervalOrder = [2,2,1,2,2,2,1]                // major interval order
~intervalToDegrees.(~majorIntervalOrder)             // major degrees
```