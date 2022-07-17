(sec-intervals)=
# Intervals

Let $\omega_1 > \omega_2$ be some arbitrary frequencies, then the *ratio*

\begin{equation}
    \frac{\omega_1}{\omega_2}
\end{equation}

is the *interval* between $\omega_1$ and $\omega_2$.
We often notate an interval as $\omega_1$:$\omega_2$.
The interval between two frequencies, i.e., notes, gives a sound quality.
Relating multiple intervals by, for example, playing two times three different notes in sequence, gives the resulting sound another quality.
It may evoke happiness, fear, darkness, melancholy, or tension.
It may be grounding, i.e., invoke a feeling of homecoming.
Therefore, *intervals* are one of the most critical features to study.

Everything starts with a *natural phenomenon* which has been referred to as *The Basic Miracle of Music*.
After *unison* (an interval of 1:1), the *octave* (interval of 2:1) is the simplest interval in music.
An *octave* is the *interval* between one musical pitch and another double its frequency.
The human's (as well as monkey's, rat's, and infant's) ear tends to hear both frequencies/notes as being essentially the same due to closely related harmonics.
For this reason, notes an *octave* apart are given the same note name in the *Western System of Music Notation*.

Notable, pitch can be perceived in a range which is approximately the same for each person.
If we assume the *Twelve-tone Equal Temperament* as a ginven, an *octave* is divided into 12 *semitones* of 100 *cents* each.
Thus, an *octave* is divided into 1200 *cents*.
In a range from 10 to 25 *cents*, depending on the listeners hearing and musical education or exposer, pitch differences can be perceived.
In terms of a center frequency $\omega$, this gives us an interval defined by

\begin{equation}
    \omega \cdot \lambda,
\end{equation}

with $\lambda \in [-\epsilon;\epsilon]$ and

\begin{equation}
   \epsilon \in \left[\frac{10}{1200}; \frac{25}{1200} \right] = \left[\frac{1}{120}; \frac{1}{48} \right] \approx \left[0.0083; 0.208 \right].
\end{equation}

Compare the sound of the following signals.
Listen to each sine wave seperately. 
Can you hear the difference?
What happens if you listen to both of them at the same time?

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
The *perfect fifth* (3:2), the *perfect fourth* (4:3), and the *minor* and *major* third are consonant.
The *diminished* is dissonant.
While dissonance is less pleasing, it can create drama, excitement, and tension.
It is an important property to use in composing music.

In the table I list the *just temperament*, i.e., ratios of *rational numbers*.
For the *equal temperament* the ratios slightly differ; they are irrational.
For example, $6/5 = 1.2$ becomes $\sqrt[3]{2} \approx 1.1892$.

Why is an interval of four semitones called *major third*?
Well, to understand this concept, we have to first understand [scales](sec-scales) and [keys](sec-keys).
First read these sections and come back.

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