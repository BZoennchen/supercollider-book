# Music Theory

>I was lucky enough to be shown a Penderecki score and played polymorphia by a tutor. It was just really exciting. I didn't know you are allowed to do that. I didn't know you could be that free and you can just think of 48 musicians as being able to do anything. -- *Jonny Greenwood*

Faced with the need to communicate, humans developed languages, i.e., vowel and consonant sounds and the astonishing capability to recognize them.
It seems that consequently, our ears developed into highly sophisticated analyzers of frequency, loudness, harmony, and dissonance because, with languages, came the need to acknowledge slight differences.
Differentiation is a necessary condition to build an entity and its environment, i.e., what we can differentiate from the entity.
It reduces complexity to a point at which reality emerges -- without complexity reduction, reality would be an unstructured muddy see of noise.
Differentiation makes us but also disconnects us, a contrast we always struggle with and for which we employ music to overcome it, at least for a moment. 

Our hearing capabilities enable us to enjoy the art of music.
They enable us to recognize patterns of compression and rarefaction of molecules; 
a physical process that can be mathematically represented by the relation of numbers.
Music arises if there are multiple such relationships.
At its core, music is about the relation of numbers, i.e., *ratios*, related to other numbers, i.e., *intervals*.

*Music theory* is the science of these relationships in relation to the cultural, social, and emotional interpreting creature that lived during different centuries at different places.
It is the study of theoretical aspects as well as practices and possibilities of music and its notation in a cultural and historical context.
In its essence, it studies the cognition and perception of human beings; 
our cognition and perception;

Music theory developed historically a long time ago and has matured since then.
Consequently, there are numerous terms, often for the same thing, which makes it hard to start diving into it.
But to communicate ideas and concepts, the elaborate terminology is a valuable bridge in the same way mathematical notations allow us to convey ideas quickly and ambiguously.
To understand the literature and communicate effectively, one must learn the music theory terminology.

However, this does not mean that we have to adapt techniques or rules that emerged from the study of music.
It is easy to see that contrains can be helpful to explore the space of possibilities but innovation often relys on breaking out of the ordinary.
There is no hard limit, nothing is forbidden, everything is permitted.
A good example to observe the dissolution and evolution of musical rules is Western music tradition*.
Classical as well as popular music is guided by this tradition but we sometimes forget that these rules constrain us to only one specific set of our vast space of possibilities.
Importantly, these rules of generating well-received music changed over the centuries.
They tend to open up from a narrow perspective starting from *Pythagoreanism* (600 BC) to the *Gregorian mode* (early middle ages until 1600), the *major-minor-tonality* (1700-1900), *Schoneberg's* *atonality* and *serialism* (1900-1940) and *Penderecki's* experimentals compositions that are radical explorations of timbre.

In summary, music theory provides us with terminology to effectively convey and absorb musical ideas and concepts.
It provides knowledge about the relation of numbers and how these relations may affect the listener.
But it can also be limiting if taken too literally.
For example, it has the musician and its (analog) instrument in mind.
Therefore, until recently, its literature does not provide us with musical aspects that can not be realized by musicians that are constrained by their physical as well as mental ability to play an instrument.
Consequently, music theory is a valuable subject to grasp, but it should never be taken as definitive truth.

(sec-intervals)=
## Intervals

Let $f_1 > f_2$ be some arbitrary frequencies, then the *ratio*

\begin{equation}
    \frac{f_1}{f_2}
\end{equation}

is the *interval* between $f_1$ and $f_2$.
We often notate an interval as $f_1$:$f_2$.
The interval between two frequencies, i.e., notes, gives a sound quality and relating multiple intervals by, for example, playing two times three different notes in sequence, gives the resulting sound another quality.
It may evoke happiness, fear, darkness, melancholy, and tension.
It may be grounding.
Therefore, *intervals* are one of the most critical features to study.

Everything starts by a *natural phenomenon* which has been referred as to as *basic miracle of music*.
After *unison* (an interval of 1:1), the *octave* (interval of 2:1) is the simplest interval in music.
An *octave* is the *interval* between one musical pitch and another double its frequency.
The human (as well as money, rats, infants) ear tends to hear both frequencies/notes as being essentially the same, due to closely related harmonics.
For this reason, notes an *octave* apart are given the same note name in the *Western system of music notation*.

Notable, pitch can be perceived in a range which is approximately the same for each person.
If we assume the *twelve-tone equal temperament* as a ginven, an *octave* is divided into 12 *semitones* of 100 *cents* each.
Thus, an *octave* is divided into 1200 *cents*.
In a range from 10 to 25 *cents*, depending on the listeners hearing and musical education or exposer, pitch differences can be perceived.
In terms of a center frequency $f$, this gives us 

\begin{equation}
    f \cdot \lambda,
\end{equation}

with $\lambda \in [-\epsilon;\epsilon]$ and

\begin{equation}
   \epsilon \in \left[\frac{10}{1200}; \frac{25}{1200} \right] = \left[\frac{1}{120}; \frac{1}{48} \right] \approx \left[0.0083; 0.208 \right].
\end{equation}

Compare the sound of the following signals.
Can you hear the difference?

```isc
(
{
    var sig, freq = 440;
    sig = SinOsc.ar(freq!2);
    sig * 0.25;
}.play;
)

(
{
    var sig, freq = 440 * (1 + 48.reciprocal);
    sig = SinOsc.ar(freq!2);
    sig * 0.25;
}.play;
)
```

The following table lists special names for important intervals.

| Interval       | Multiple                      | (Just) Ratios         | Semitones |
| -------------- | ----------------------------- | --------------------- | --------- |
| Unison         | 1                             | 1:1                   | 0         |
| Octave         | 2                             | 2:1                   | 12        |
| Perfect fifth  | 1.5                           | 3:2                   | 7         |
| Perfect fourth | 1.33                          | 4:3                   | 5         |
| Major third    | 1.25                          | 5:4                   | 4         |
| Minor third    | 1.2                           | 6:5                   | 3         |
| Major sixth    | 1.66                          | 5:3                   | 9         |
| Minor sixth    | 1.6                           | 8:5                   | 8         |
| Major second   | 1.125                         | 9:8                   | 2         |
| Minor second   | 1.778                         | 16:9                  | 1         |
| Major seventh  | 1.875                         | 15:8                  | 11        |
| Minor seventh  | 1.8                           | 9:5                   | 10        |
| Diminished     | 1.4142                        | 45:32                 | 6         |

*Intervals* can sound pleasingly consonant or dissonant.
The table above contains all important intervals ordered by how consonant they are in ascending order.
Note that in *equal temperament* the ratios slightly differ.
For example, $6/5 = 1.2$ becomes $\sqrt[3]{2} \approx 1.1892$.
An *octave* (2:1) sounds perfectly consonant.
The *perfect fifth* (3:2), the *perfect fourth* (4:3), and the *minor* and *major* third are consonant.

While dissonance is less pleasing, it can create drama, excitement, and tension.
It is an important property to use in composing music.

Why is the interval of 4 semitones called *major third* called a *major third*?
Well, to understand this concept, we have to first understand [scales](sec-scales) and [keys](sec-keys).
Read these sections and come back.

You are ready?
Ok, let us move on.
An interval of $i$ semitones is called *major* if the note $n+i$ is **not** in the (major) key of $n$.
For example, let us look at C-E. 
Then E is not in the major key of C.
If it would be in the major key of C, it would be called **minor**.
For example, C is in the key of D# (major) thus C-D# is a **minor** interval.
If both notes defined by an interval are in the other's (major) key, the interval is **perfect**.

Furthermore, C-E spans three notes within the major key of C. 
Therefore it is called major **third**.

(sec-scales)=
## Scales

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

```{figure} ../../figs/composing/piano-keys.png
---
width: 400px
name: fig-piano-keys
---
The notes of an octave mapped on piano keys.
Each consecutive *interval* is equal to $\sqrt[12]{2}$.
The white keys give us the C major scale (diatonic scale).
Above one can see the number of semitones of each interval of the major scale.
```

### Chromatic Scale

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

The *interval order* 

\begin{equation}
    (2,2,1,2,2,2,1)_{\text{major}}
\end{equation}

of the diatonic scale is the sequence of whole and half steps in the scale.
It is reflected by the piano keys but hidden by the notation of a note sheet.
The group $(2,2,1)$ is followed by $(2,2,2,1)$.
The unique order of whole and half steps provide a crucial asymmetry that our hearing exploits in order to orient ourselves.

### Minor Scales

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

(sec-modes)=
## Modes

Starting a scale from other than degree 1 or 6 produces additional scales that share the diatonic interval order.
These variations are called *modes*.
We also get the different modes by shifting the *interval order* of the *diatonic scale*.
Its initial degree is called *final* because typically, music in a mode would end on that note.
Major and minor scales are synonyms for *Ionian* and *Aeolian modes* -- a quite elaborate naming convention.

(sec-keys)=
## Keys

Nowadays, apart from *Ionian* (*major*) and *Aeolian* (*minor*), modes are no longer in broadly in use.
Instead, composers use *transpositions*.
If a scale starts on any chromatic degree other than C, it is said to be *transposed*.
The diatonic scale can be transposed to any chromatic degree so long as the diatonic interval order is preserved.
The degree to which the diatonic scale is transposed is called the *key*.

For example, the diatonic scale transposed to G by the introduction of F# is the *key of G*.
We also say that we play a certain piece in the *G major key* or the *key of G major*.
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

## Tuning

*Pythagoreans* were obsessed with *simple ratios*, i.e., ratios formed by small prime numbers.
They build a *just-tuning* by using these ratios, which lead to a strong dissonance for some combinations of notes.
In 1584 *Zhu Zaiyu* achieved an exact calculation of the well-known *twelve-tone equal temperament tuning (12-TET)* in China.
One year later, the Flemish mathematician *Simon Stevin* was also able to develop this flexible *tuning*.
Instead of using *simple ratios* *equal temperament tunings*, use real numbers such that an *octave* is divided in equally tempered (equally spaced) on a logarithmic scale.
In the case of the *twelve-tone*, the ratio is equal to the 12th root of 2, i.e.,

\begin{equation}
    \sqrt[12]{2} = 2^{1/12} \approx 1.05946.
\end{equation}

In modern times, 12-TET is usually tuned relative to a standard pitch of 440 Hz, called A440.
Note A is tuned to 440 hertz, and all other notes are defined as some multiple of semitones apart from it, either higher or lower in frequency.
However, the standard pitch has not always been 440 Hz, and there is still a lot of dispute and discussion.
This development is a comparatively recent development in the musical community, and the agreement is still fragile among musicians {cite}`loy:2006`.

Interstingly, if we look at the intervals between harmonics we spot *simple ratios* for 12-TET.
From the fundamental $f$ to the first overtone $2f$ we get the ratio $2/1$.
From the first $2f$ to the second overtone $3f$ we get another simple ratio, i.e., $3/2$ following the intervals $4/3$, $5/4$ and $6/5$.
In general the $i$-th interval is equal to 

\begin{equation}
    \frac{i+1}{i},
\end{equation}

which gives us *simple ratios* for small $i$.

## Chords

Similar to diatonic scale where notes are numbered from one to seven, we also use numbers to denote the position of a chord relative to its key (e.g. scale of key E).
The most prominant chords called *triads* consist of three notes, where we start at some note and take two times every other note.
In other words, chords are fully defined by the used *key* and a combination of degrees (*scale note positions*).
If $d$ is the degree of the first note then

$$(d, d+2, d+4)$$

constitute a *triad*.
For example, for a major scale in the key of C (all white key on a piano),

$$(\text{E, G, B})$$

constitutes the iii-minor scale within this key.
Roman numerals (I, ii, iii, IV, V, vi, vii) are used to label chord positions.
We use capitalized roman numerals if we refer to a major chord, otherwise we use lowercase numerals.
The numbers translate to the degrees of the key.
In the following first table I use the major scale in the key of A:

| Major Key | I     | ii    | iii   | IV    | V     | vi    | vii           |
| --------- | ----- | ----- | ----- | ----- | ----- | ----- | ------------- |
|           | major | minor | minor | major | major | minor | diminished    |
| Intervals | 4,3   | 3,4   | 3,4   | 4,3   | 4,3   | 3,4   | 3,3           |
| A major   | A     | B     | C#    | D     | E     | F#    | G#            |

In the second table I use the minor scale in the key of A:

| Minor Key | i     | ii         | III   | iv    | v     | VI    | VII   |
| --------- | ----- | ---------- | ----- | ----- | ----- | ----- | ------|
|           | minor | diminished | major | minor | minor | major | major |
| Intervals | 3,4   | 3,3        | 4,3   | 3,4   | 3,4   | 4,3   | 4,3   |
| A minor   | A     | B          | C     | D     | E     | F     | G     |

Following the formula, we call (B, D, F#) the *B minor* (in the key of major A) and (D, F, A) the *D major* (in the key of minor A).
Note that all *triads within a key* are unique.
In a major key, a major chord is defined an interval order of (4,3), the minor chord is defined by (3,4) and the deminished is defined by (3,3).
If we look at all resulting intervals for the major and minor chord we get: 3 semitones (**minor third**), 4 semitones **major third** and 7 semitones (**perfect fifth**).
In frequencies of an equally tempered octave this equates to 

\begin{equation}
\begin{split}
2^{3/12} &\approx 1.189 \approx 1.2,\\
2^{4/12} &\approx 1.259 \approx 1.25,\\
2^{7/12} &\approx 1.498 \approx 1.5.
\end{split}
\end{equation}

All these ratios are relatively simple; thus, the tone is consonant. For the diminished chord, we get two intervals of 3 semitones (**minor third**) and an interval of 6 semitones (**minor seventh**) resulting tone a little more dissonant.
In frequencies of an equally tempered octave this equates to 

\begin{equation}
\begin{split}
2^{3/12} &\approx 1.189 \approx 1.2,\\
2^{6/12} &\approx 1.4142 \approx 1.25.
\end{split}
\end{equation}

Note that we can categorize the chord into major, minor, or diminished solely by the *interval order*.
Therefore, a chord is fully defined by this order and the first note.
Consequently, we do not know the *key*.
We can name the chord by the *first note* and the *interval order*, e.g., B minor chord (*Bm*) is equal to (B, D, F#).
Musicians use only the note symbol, such as F, to denote the major chord of that note, e.g., F major.
This can be confusing because scales and keys are denoted similarily.

By relating chords via a *chord progression* they can have different types of emotional effects across a piece of music.

Consonant
: A stable or relaxing sound which can be used to begin or end a piece of music (*major/minor*)

Dissonant
: An unstable (tension producing) sound which wants to resolve back into stability (*augmented/diminished*)

## Midi Notes

Midi notes are just numbers on a piano.
Modern pianos follow the *twelve-tone equal temperament tuning (12-TET)*.
The different keys are numbered in an ascending order from left to right.
The note A0 corresponds to the midi note 21, A2 corresponds to 33 and so on.
The key pattern of a piano repeats itself.
Twelve keys form an octave C, C# D, D#, E, F, F#, G, G#, A, A#, B.
The letter gives us the *tone* while number tells us in which *octave* we are.
In combination we get a *pitch*.

A1 and A3 have the same tone but A3 is two octaves higher thus its pitch is higher.
Additionally, the frequency of A3 is equal to the frequency of A1 multiplied by $2^2 = 4$.
The mapping between frequency $f$ and pitch $p$ is a logarithmic one.
For *12-TET* and a standard pitch of A440 we get the following formula:

\begin{equation}
    f(p) = 2^\frac{p-69}{12} \cdot 440,
\end{equation}

where $p$ is the midinote number, i.e., the midinote 69 maps to 440 Hz (A4).
Since the frequency doubles after 12 keys, we have to multiply the frequency of pitch $p$ by $2^{\frac{1}{12}}$ to get $p+1$. In other words

\begin{equation}
    \frac{f(p+1)}{f(p)} = 2^{\frac{1}{12}}.
\end{equation}

Since there are the same number of keys for each octave but higher octaves cover a much larger range of frequencies, we can conclude that high frequencies are likely to appear much sparser in a piano piece.