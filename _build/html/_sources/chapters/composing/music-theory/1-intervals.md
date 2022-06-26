(sec-intervals)=
# Intervals

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