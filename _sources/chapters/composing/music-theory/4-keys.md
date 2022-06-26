(sec-keys)=
# Keys

Nowadays, apart from *Ionian* (*major*) and *Aeolian* (*natural minor*), modes are no longer in broadly in use.
Since the introduction equally tempered piano, composers use *transpositions*, instead.

If a scale starts on any chromatic degree/note other than C, it is said to be *transposed*.
The diatonic scale can be transposed to any chromatic degree so long as the *[diatonic interval order](sec-diatonic-scale)* is preserved.
The degree to which the diatonic scale is transposed is called the *key*.

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

We also call that seven semitone interval a **perfect fifth**, which corresponds to a pair of pitches with a frequency ratio of 3:2, or very nearly so.
Adding seven semitones gives us the ratio 

$$2^{7/12} \approx 1.498 \approx 1.5 = 3/2.$$

Simple or close to simple ratios sound pleasing, while complex ratios sound unharmonic and can provide tension.

Because the *major-minor-intervals* are so prominent, we can also define the scales as minor scales.
For example, C major is, with respect to its notes, equivalent to A minor (A, B, C, D, E, F, G), but the keys are differently balanced in a piece.
The *tonic* (the "home" of the key), for example, is usually the first note of the key.
