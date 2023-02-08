(sec-scales)=
# Scales, Modes and Keys

As a beginner coming from a rigorous discipline, I found the terms *scales*, *keys*, and *modes*, confusing because they seem to blend into one another.
Let me start with a clear differentiation between *scales* and *keys*.

Sometimes musicians speak of a scale and sometimes of a key as if these two terms are interchangeable.
A scale places the notes in a **specific order**, up and down the keyboard, while *key* refers to all the notes of the same *scale* in **any order**
and all possible combinations.
For example, if we play multiple notes, we play these in the *key of C*.
We also use the note from the C major *scale*.
We think of notes that make up a scale but do not think of them in any particular order, we think of 'the key of C'.

(sec-scales-and-keys)=
## Scales & Keys

A *musical scale (Tonleiter)* is an **ordered** set of pitches, together with a formula for specifying their frequencies.
Each individual pitch of a scale is called a *degree (Tonstufe)*.

Most musical traditions use *octave intervals* to associate pitches that serve the same musical function (*unison*) such that a scale is completely defined by one *octave* because of *octave equivalence*, i.e., the basic miracle of music*.
In that case, any *degree* is a member of a class that it shares with the same degree in all other octaves.
*Degrees* of a scale are sometimes called *pitch classes*.

(sec-chromatic-scale)=
### Chromatic Scale

The *chromatic scale*, which translates to *colorful scale*, consists of all twelve pitches (within an octave) we know from a piano:

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
### Diatonic Scale (Major Scale)

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

```{figure} ../../../figs/composing/piano-keys-major-scales.png
---
width: 800px
name: fig-piano-keys-major-scales
---
C major scale (or keys of C major) in blue and D# major scale in red.
The ones mark the beginning of the scales.
```

The diatonic scale is reflected by the piano keys, but hidden by the notation of a note sheet, e.g., C and C# occupy the same pitch line.
The group $(2,2,1)$ is followed by $(2,2,2,1)$.

```{figure} ../../../figs/composing/diatonic-scale.png
---
width: 400px
name: fig-diatonic-scale
---
The diatonic scale on a note sheet.
```

### Minor Scales

The *minor scale*, also known as *natural minor scale*, uses the standard *diatonic interval order* but starts on degree 6 (counting from one).
We get the *minor interval order* by shifting the diatonic interval order by 2 to the right or by 5 to the left.
Therefore, it has the same *sparsity* as well as *asymmetry*. as the [diatonic scale](sec-diatonic-scale).

The *minor scale* is also called **natural minor** and is also known as the *Aolian [mode](sec-modes)*.

\begin{equation}
    (2,1,2,2,1,2,2)_\text{nat. minor}
\end{equation}

This gives us: C, D, Eb, F, G, Ab, Bb.

```{figure} ../../../figs/composing/piano-keys-minor-scales.png
---
width: 800px
name: fig-piano-keys-minor-scales
---
C minor scale (or keys of C minor) in blue and D# minor scale in red.
The ones mark the beginning of the scales.
```


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

If a scale starts on any chromatic degree/pitch other than C, it is said to be *transposed*.
The diatonic scale can be transposed to any chromatic degree so long as the *[diatonic interval order](sec-diatonic-scale)* is preserved.
For example, the diatonic scale transposed to G by the introduction of F# is the *key of G*.
We also say that we play a certain piece in the *G major key* or the *key of G major* or just *G major*.
The untransposed diatonic scale is the *key of C*.

In SuperCollider, we can transpose by adding degree to ``\degree`` or by using ``\mtransposes`` in the ``Pbind``.

```isc
(
Pbindef(\melody,
    \instrument, \default,
    \scale, Scale.major,
    \degree, Pseq((0..7), inf),
    \octave, 3,
    \mtranspose, 3, // key of D#
    \dur, 0.25,
    \amp, 1
).play;
)
```

Let us consider the degrees of *major scale* (key of C) with respect to the chromatic scale:

$$C_\text{major} = (1, 3, 5, 6, 8, 10, 12) = (\text{C, D, E, F, G, A, B }).$$

Transposing the scale by the interval of seven semitones upwards, gives us

$$G_\text{major} = (8, 10, 12, 1, 3, 5, 7) = (\text{G, A, B, C, D, E, F#})$$

and transposing it by 7 semitones downwards gives results in

$$F_\text{major} = (6, 8, 10, 11, 1, 3, 5) = (\text{F, G, A, A#, C, D, E}).$$

Transposing again and again by seven semitones will add additional sharps and flats.
Consecutive transposes (by seven) sound similar.
The following code generates all *major* scales by trasposing by seven semitones:

```isc
(
~translate = {arg degree;
    var result = Array.fill(7, '');
    var sum = degree;
    var majorIntervals = [2, 2, 1, 2, 2, 2];
    var chromaticKeys = [
        "C", "C#", "D", "D#", 
        "E", "F", "F#", "G", 
        "G#", "A", "A#", "B"];
    var rotation = 0;
    result[0] = chromaticKeys[degree % 12];
    for(0, majorIntervals.size-1, {arg i;
        result[i+1] = chromaticKeys[(sum+majorIntervals[i])%12];
        sum = sum + majorIntervals[i];
    });
    result;
});

(
(0..12).do({ arg i;
	~translate.(i*7).postln;
});
)
```

The circular result is depicted in the following table.
After F major everything is repeated.

| Scale         | Pitches                            | Sharps | Flats  |
| ------------- | ---------------------------------- | ------ | ------ |
| C major       | C, D, E, F, G, A, B                | 0      | 0      |
| G major       | G, A, B, C, D, E, F#               | 1      |        |
| D major       | D, E, F#, G, A, B, C#              | 2      |        |
| A major       | A, B, C#, D, E, F#, G#             | 3      |        |
| E major       | E, F#, G#, A, B, C#, D#            | 4      |        |
| B major       | B, C#, D#, E, F#, G#, A#           | 5      | 7      |
| F# major      | F#, G#, A#, B, C#, D#, F (E#)      | 6      | 6      |
| C# major      | C#, D#, F (E#), F#, G#, A#, C (B#) | 7      | 5      |
| G# major      | G#, A#, C, C#, D#, F, G            |        | 4      |
| D# major      | D#, F, G, G#, A#, C, D             |        | 3      |
| A# major      | A#, C, D, D#, F, G, A              |        | 2      |
| F major       | F, G, A, A#, C, D, E               |        | 1      |

In general, A# equals Bb, D# equals Eb, G# equals Ab, C# equals Db and F# equals Gb.
We call that seven semitone [interval](sec-intervals) a **perfect fifth**, which corresponds to a pair of pitches with a frequency ratio of 3:2, or very nearly so.
Adding seven semitones gives us the ratio 

$$2^{7/12} \approx 1.498 \approx 1.5 = 3/2.$$

As already mentioned, simple or close to simple ratios sound pleasing, while complex ratios sound unharmonic and can provide tension.

Because the *major-minor-intervals* are so prominent, we can also define the *keys* as *minor keys*.
For example, the keys of C major are equivalent to the keys of A minor (A, B, C, D, E, F, G), but they are differently balanced in a piece.
The *tonic/root* (the "home" of the *keys*), for example, is usually the first note in the respective *scale*.

(sec-modes)=
## Modes

Starting a *diatonic scale* other than from degree 1 or 6 produces additional *scales* that share the diatonic interval order.
These variations are called *modes*.
We get the different *modes* by shifting the *interval order* of the *diatonic scale*.
In SuperCollider we can achieve this by *array rotation* using ``rotate``:

```isc
// generation of different modes
~majorIntervalOrder = [2,2,1,2,2,2,1]                // major interval order
~minorIntervalOrder = [2,1,2,2,1,2,2]                // (nat.) minor interval order
~intervalToDegrees.(~majorIntervalOrder)             // major degrees
~intervalToDegrees.(~minorIntervalOrder)             // (nat.) minor degrees
~intervalToDegrees.(~majorIntervalOrder.rotate(2))   // (nat.) minor degrees (by rotation)
```

*Major* and *minor scales* are synonyms for *Ionian* and *Aeolian modes* -- a quite elaborate naming convention.
The initial degree of a mode is called *final* because typically, music in a mode would end on that note.
For example, the *final* of the *Aeolian mode* is 6.

Since the order matters for a *scale*, we have to change the *interval order*.
Adding a fixed number of semitones/half steps does not suffice because we would change the *root*.
If we do so, we change the *root* (the 'home note'), i.e., achieve another transformation called *transposition* by switching from, e.g., C major to D major.
However, if we disregard the order, i.e., if we look at the *keys* in which we play, we can get the same by transposing the *keys*.
For example, as you can observe in the above illustrations, the keys of C minor are the keys of D# major.

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