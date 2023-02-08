(sec-intervals)=
# Intervals

If we push multiple keys on a piano, the color of the sound we perceive will be determined mainly by the relation between those keys, i.e., the generated *intervals*.
In that regard, compared to the exact pitches, *intervals* are much more important.
Building a beautiful melody revolves around finding a suitable sequence of a set interval of intervals.
They are, in fact, so crucial that musicians give certain intervals specific names!

## Frequency Ratios

Let $f_1 > f_2$ be some arbitrary frequencies, then the *ratio*

\begin{equation}
    \frac{f_1}{f_2}
\end{equation}

is the *interval* between $f_1$ and $f_2$.
We often notate an interval as $f_1$:$f_2$.
The interval between two frequencies, i.e., pitches, gives a sound quality.
Relating multiple intervals by, for example, playing two times three different pitches in sequence, gives the resulting sound another quality.
It may evoke happiness, fear, darkness, melancholy, or tension.
It may be grounding, i.e., invoke a feeling of homecoming.

The most common number of pitches within a [chord](sec-chords) is the triad $f_1, f_2, f_3$ which generates three intervals:

\begin{equation*}
    \frac{f_1}{f_2}, \frac{f_2}{f_3}, \frac{f_3}{f_1}.
\end{equation*}

In general, if we play $n$ keys on a piano simultaneously, we create $(n-1)^2$ intervals.
So, why do intervals have a psychological effect on us humans?

Everything starts with a *natural phenomenon* which has been referred to as *the basic miracle of music*.
After *unison* (an interval of 1:1), the *octave* (interval of 2:1) is the simplest interval in music.
An *octave* is the *interval* between one musical pitch and another double its frequency.
The human's (as well as monkey's, rat's, and infant's) ear tends to hear both frequencies/notes as being essentially the same due to closely related harmonics.
For this reason, notes an *octave* apart are given the same note name in the *Western dystem of music notation*.

Compare the sound of the following two pattern.
Which melody sounds more harmonic and why?
Can you hear the difference?

```isc
(
var base = 300;
Pbindef(\melody1,
    \instrument, \default,
    // complex ratios
    \freq, Pseq([base, base*21/17, base*37/17, base*11/7, base*11/17, base*39/17], 6),
    \dur, 0.2,
    \legato, 0.1
).play;
)

(
var base = 300;
Pbindef(\melody2,
    \instrument, \default,
    // simple ratios
    \freq, Pseq([base, base*5/3, base*2/3, base*4/3, base/2, base*6/5], 6),
    \dur, 0.2,
    \legato, 0.1
).play;
)
```

Notable, pitch can be perceived in a range which is approximately the same for each person.
If we assume the *twelve-tone equal temperament* as a given, then an *octave* is divided into 12 *semitones* of 100 *cents* each.
Thus, an *octave* is divided into 1200 *cents*.
In a range from 10 to 25 *cents*, depending on the listeners hearing and musical education or exposer, pitch differences can be perceived.
In terms of a center frequency $f$, this gives us an interval defined by

\begin{equation}
    f \cdot \lambda,
\end{equation}

with $\lambda \in [-\epsilon;\epsilon]$ and

\begin{equation}
   \epsilon \in \left[\frac{10}{1200}; \frac{25}{1200} \right] = \left[\frac{1}{120}; \frac{1}{48} \right] \approx \left[0.0083; 0.208 \right].
\end{equation}

Therefore, our perception ability widely outperforms the variants a musician can perform on a piano but it covers most of the consonant options.

## Naming Convention

The following table lists special names for important intervals.
In the table I list the *just temperament*, i.e., ratios of *rational numbers*.
For the *equal temperament* the ratios slightly differ; they are irrational.
For example, $6/5 = 1.2$ becomes $\sqrt[3]{2} \approx 1.1892$.

| Interval Name  | Multiple                      | (Just) Ratios         | Semitones |
| -------------- | ----------------------------- | --------------------- | --------- |
| Unison         | 1                             | 1:1                   | 0         |
| Minor second   | 1.778                         | 16:9                  | 1         |
| Major second   | 1.125                         | 9:8                   | 2         |
| Minor third    | 1.2                           | 6:5                   | 3         |
| Major third    | 1.25                          | 5:4                   | 4         |
| Perfect fourth | 1.33                          | 4:3                   | 5         |
| Diminished     | 1.4142                        | 45:32                 | 6         |
| Perfect fifth  | 1.5                           | 3:2                   | 7         |
| Major sixth    | 1.66                          | 5:3                   | 9         |
| Minor sixth    | 1.6                           | 8:5                   | 8         |
| Minor seventh  | 1.8                           | 9:5                   | 10        |
| Major seventh  | 1.875                         | 15:8                  | 11        |
| Octave         | 2                             | 2:1                   | 12        |

*Intervals* can sound pleasingly consonant or dissonant.
Simple **or** close to simple ratios tend to sound consonant while complicated ratios tend to sound dissonant.
An *octave* (2:1) sounds perfectly consonant.
The *perfect fifth* (3:2), the *perfect fourth* (4:3), and the *minor* and *major third* are consonant.
The *diminished* is dissonant.
While dissonance is less pleasing, it can create drama, excitement, and tension.
It is an important property to use in composing music.

```{figure} ../../../figs/composing/piano-keys-intervals.png
---
width: 800px
name: fig-piano-keys-intervals
---
Piano keys: the octave in blue, the perfect fourth in red, and the minor third in green. Note that only the distance between keys, i.e., their relation matters!
```

Why is an interval of four semitones called *major third*?
Well, to understand this concept, we have to first understand [scales and keys](sec-scales-and-keys).
First read these sections and come back later.

Are you ready?
Ok, let us move on.
An interval of $i \in \mathbb{N}$ semitones is called *major*, if the note $n+i$ is **not** in the (major) key of $n$.
For example, let us look at C-E. 
Then E is not in the major key of C.
If it were in the major key of C, it would be called **minor**.
For example, C is in the key of D# (major); thus, C-D# is a **minor** interval.
If both notes defined by an interval are in the other's (major) key, the interval is **perfect**.

Furthermore, C-E spans three notes within the major key of C. 
Therefore it is called major **third**.