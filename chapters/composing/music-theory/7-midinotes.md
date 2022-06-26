# Midi Notes

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