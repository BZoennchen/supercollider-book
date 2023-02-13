(sec-intervals)=
# Intervals

If we push multiple piano keys, the color of the sound we perceive will be determined mainly by the relation between those keys, i.e., the generated *intervals*.
In that regard, compared to the exact pitches, *intervals* are much more important.
But instead of similarity we consider *consonant* and *dissonant* combinations of notes or more preceisly pitches.
For example, pressing two consequitive piano keys result in vibration, i.e., both strings vibrate with a similar frequency but they cause dissonance!

Building a beautiful melody revolves around finding a suitable sequence of a set interval of intervals.
It is a play around *dissonance* and *consonance*, between building up tension and realsing it by coming home to the literal root.
Intervals are, in fact, so crucial that musicians give certain intervals specific names and functionalities!

An interval can be described as *vertical* or **harmonic** if the two notes sound simultaneously.
If they sound successively we speak of *horizontal*, *linear* or **melodic** intervals.
These can be *ascending* and *descending*.

## Frequency Ratios

Since I am a computer scientist and not a musician I will start by looking at the relation of notes using my mathematical perspective first.
Before we talk about notes, chords, keys and so on, let us focus on the basics: frequencies!
Let $f_1 > f_2$ be some arbitrary frequencies, then the *ratio*

\begin{equation}
    \frac{f_1}{f_2}
\end{equation}

is the *interval* between $f_1$ and $f_2$.
We often notate an interval as $f_1$:$f_2$.
Consequently, an interval is defined as the ratio of two frequencies.
We can extend this concept to multiple frequencies $f_1, f_2, f_3$ for which we receive three intervals:

\begin{equation*}
    \frac{f_1}{f_2}, \frac{f_2}{f_3}, \frac{f_3}{f_1}.
\end{equation*}

In general, if we have $n$ distinct frequencies, we get $(n-1)^2$ intervals.

However, if we consider piano keys things get more complicated since the vibration of a single piano string result air pressure that can be represented by a signal with multiple frequencies.
We have to add many harmonics to the fundamental.
The actual pitch is a perceptual property and depends on the listener.
We generalise and claim that the fundamental frequency, i.e., the frequency of the lowest partial, is the actual pitch of the vibration the listener hears.
Consequently, in music theory, an *interval* may be loosely defined as the difference between two pitches, i.e., the ratio of two fundamentals.
Playing two piano keys gives the sound a specific color.
Relating multiple intervals by, for example, playing two times three different pitches in sequence, gives the resulting sound another quality.
It may evoke happiness, fear, darkness, melancholy, or tension.
It may be grounding, i.e., invoke a feeling of homecoming.

So, why do intervals have a psychological effect on us humans?
Everything starts with a *natural phenomenon* which has been referred to as *the basic miracle of music*.
After *unison* (an interval of 1:1), the *octave* (interval of 2:1) is the simplest interval in music.
An *octave* is the *interval* between one musical pitch and another double its frequency.
The human's (as well as monkey's, rat's, and infant's) ear tends to hear both frequencies/notes as being essentially the same due to closely related harmonics.
For this reason, pitches an *octave* apart are given the same note name in the *Western dystem of music notation*.

Compare the sound of the following two pattern.
Which melody sounds more harmonic and why?
Can you hear the difference?

```isc
(
var base = 300;
Pbindef(\melody1,
    \instrument, \default,
    // complex ratios
    \freq, Pseq([base, base*21/17, 
                 base*37/17, base*11/7,
                 base*11/17, base*39/17], 6),
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

## Cents

The cent is a logarithmic unit of measurement. 
If frequency is expressed in a logarithmic scale, and along that scale the distance between a given frequency and its double (also called octave) is divided into 1200 equal parts, each of these parts is one cent. 
In *twelve-tone equal temperament (12-TET)*, a tuning system in which all semitones have the same size, the size of one semitone is exactly 100 cents. 
Hence, in 12-TET the cent can be also defined as one hundredth of a semitone.

Mathematically, the size in cents of the interval from frequency $f_1$ to frequency $f_2$ is

$$1200 \cdot \log_2\left( \frac{f_1}{f_2} \right).$$

## Naming Convention

The following table lists special names for important intervals.
A lot of *augmented* and *dimished
In the table I list the *just temperament*, i.e., ratios of *rational numbers*.
For the *equal temperament* the ratios slightly differ; they are irrational.
For example, $6/5 = 1.2$ becomes $\sqrt[3]{2} \approx 1.1892$.

| Interval Name                      | Symbol | Multiple                      | (Just) Ratios         | Semitones |
| ---------------------------------- | ------ | ----------------------------- | --------------------- | --------- |
| Unison / diminished second         | I      | 1                             | 1:1                   | 0         |
| Minor second / augmented unison    | ii     | 1.778                         | 16:9                  | 1         |
| Major second / diminished third    | II     | 1.125                         | 9:8                   | 2         |
| Minor third / augmented second     | iii    | 1.2                           | 6:5                   | 3         |
| Major third / diminished fourth    | III    | 1.25                          | 5:4                   | 4         |
| Perfect fourth / augmented third   | IV     | 1.33                          | 4:3                   | 5         |
| Diminished fifth / tritone         |        | 1.4142                        | 45:32                 | 6         |
| Perfect fifth / diminished sixth   | V      | 1.5                           | 3:2                   | 7         |
| Minor sixth / augmented fifth      | vi     | 1.66                          | 5:3                   | 9         |
| Major sixth / diminished seventh   | VI     | 1.6                           | 8:5                   | 8         |
| Minor seventh / augmented sixth    | vii    | 1.8                           | 9:5                   | 10        |
| Major seventh / diminished octave  | VII    | 1.875                         | 15:8                  | 11        |
| Octave / augmented seventh         |        | 2                             | 2:1                   | 12        |

*Intervals* can sound pleasingly consonant or dissonant.
Simple **or** close to simple ratios tend to sound consonant while complicated ratios tend to sound dissonant.
An *octave* (2:1) sounds perfectly consonant.
The *perfect fifth* (3:2), the *perfect fourth* (4:3), and the *minor* and *major third* are consonant.
The *diminished* is dissonant.
While dissonance is less pleasing, it can create drama, excitement, and tension.
It is an important property to use in composing music.
Hermann von Helmholtz categorises the octave, perfect fifth, perfect fourth, major sixth, major third, and minor third as consonant, in decreasing value, and other intervals as dissonant.

```{figure} ../../../figs/composing/piano-keys-intervals.png
---
width: 800px
name: fig-piano-keys-intervals
---
Piano keys: the octave in blue, the perfect fourth in red, and the minor third in green. Note that only the distance between keys, i.e., their relation matters!
```

Why is an interval of four semitones called *major third*?
Well, to understand this concept, we have to first understand the [diatonic scale](sec-diatonic-scale).
Each name consists of two parts: a *quality* (major, minor, diminished, ...) and a *number* (second, third, fourth, ...).

### Numbering

The numbering system is also called *diatonic numbering* because they correspond to the degrees of the [diatonic scale](sec-diatonic-scale).
For instance, C-G is a *fifth* because the notes from C to the G above it encompass five letter names (C, D, E, F, G) and it encompass five notes of the diatonic scale, for example, C-Db-Eb-F-G for the *Ab major diatonic scale*.

Note that we start counting from one thus C-C is counted as one, even though there is no difference between the endpoints.

Adding accidentals to the notes that form an interval does not necessarily change its number.
For instance, the interval G-G# (spanning 8 semitones, i.e., a *minor sixth*) and C#-G (spanning 6 semitones, i.e., a *diminished*) can be regarded as fifths, like the corresponding *natural interval* C-G (7 semitones).

### Quality

The name of any interval is further qualified using the terms perfect (**P**), major (**M**), minor (**m**), augmented (**A**), and diminished (**d**).
This is called its *interval quality*.
Perfect intervals are consonant.
By definition, the inversion of a perfect interval is also perfect since 

$$12 - 7 + 2 = 7$$

All other intervals are less consonant.
The inversion of a minor interval is major and vice versa and the inversion of an augmented invertal is a dimished interval.
For example, a major third (4 semitones becames)

$$12-4 + 2 = 10$$

a minor seventh (10 semitones).