# Terms

## Sound Waves

In nature, *sound* is produced by a vibrating object.
These vibrations cause air molecules to oscillate.
They bump into each other at some areas (compression) and tend to leave other areas (rarefaction).
A pattern of lower and higher molecule density emerges.

On a larger scale, this change in air pressure is a mechanical wave that travels from the object to other objects.
Overall, we can think of sound as a mechanical wave that propagates from one place through the medium of transportation.
The wave is energy that deforms the medium, i.e., it transfers energy from one place to the other.

## Signal

A *signal* is a function that conveys information about a phenomena.

## Waveform

The *waveform* of a *signal* is the shape of its graph as a function of time, independent of its time and magnitude scales and of any displacement in time.
Waveforms can be *periodic* or *aperiodic*.
A periodic waveform can be *simple* (e.g. a single sine wave) or *complex* and an aperiodic waveform can be *continuous* (e.g. noise) or *transient* (e.g. impulse).

The simplest and most fundamental waveform is the sine wave

\begin{equation}
    y(t) = A \cdot \sin(2\pi \cdot f \cdot t + \phi),
\end{equation}

where the *frequency* $f$ is the inverse of the period $T$.
The period is the time at which the waveform repeats itself and the frequency $f = 1/T$ is measured in herz (circles per second).
$A$ is the amplitude and $\phi$ the phase of the waveform.

The *frequency* of a waveform determines the perceived *pitch* of the sound it produces.
The higher the frequency the higher the pitch.
Pitch is perceived on a logarithmic scale, that is, two frequencies are perceived similarly if they differ by a power of 2.
440 Hz is one octave above 220 Hz but we perceive it as the same *tone*.

The *amplitude* of a waveform determines the perceived loudness of the sound.
The higher the amplitude the louder the sound. 

## Midi notes

Midi notes are just numbers on a piano.
We simply number the different keys in an ascending order from left to right.
The note A0 corresponds to the midi note 21, A2 corresponds to 33 and so on.
The key pattern of a piano repeats itself.
Twelve keys form an octave C, C# D, D#, E, F, F#, G, G#, A, A#, B.
The letter gives us the *tone* while number tells us in which octave we are.
In combination we get a *pitch*.

A1 and A3 have the same tone but A3 is two octaves higher thus its pitch is higher.
Additionally, the frequency of A3 is equal to the frequency of A1 multiplied by $2^2 = 4$.
The mapping between frequency $f$ and pitch $p$ is a logarithmic one.

\begin{equation}
    f(p) = 2^\frac{p-69}{12} \cdot 440
\end{equation}

Since the frequency doubles after 12 keys, we have to multiply the frequency of pitch $p$ by $2^{\frac{1}{12}}$ to get $p+1$. In other words

\begin{equation}
    \frac{f(p+1)}{f(p)} = 2^{\frac{1}{12}}.
\end{equation}

Since there are the same number of keys for each octave but higher octaves cover a much larger range of frequencies, we can conclude that high frequencies are likely to appear much sparser in a piano piece.

## Cent

An octave is divided into 1200 cents.
Therefore one semitone is 100 cents.
Notable pitch differences can be perceived in a range from 10 to 25 cents, depending on the listeners hearing and musical education or exposer.

## Hearing Range

Hearing range is the range of frequency that a being can perceive.
The hearing range of humans is 20 Hz to 20kHz where cats go up to 75kHz and bats up to 200kHz.

## Sound Power

The sound power is a physical measure.
It is the energy per unit of time emitted by a sound source in all directions.
The sound power is measured in watt (W) and it is surprisingly small.
For example, a complete concert orchestra and a thunder have ruffly the power of only 1 watt.

## Sound Intensity

Sound intensity is sound power per unit area, i.e. watt per square meters.
The sound we can perceive can have is surprisingly intensity.
The threshold of hearing $TOH$ is

\begin{equation}
    THO = 10^{-12} \,\text{W/m}^2.
\end{equation}

On other end, the threshold of pain $TOP$ is 

\begin{equation}
    TOP = 10 \,\text{W/m}^2.
\end{equation}

At that intensity we start suffering from pain.

The sound intensity is measured in *decibel* (dB) which is a relative unit of measurement.
It is one-tenth of a bel: 1 dB equals 0.1 B.
It expresses the ratio of two values of a power or root-power quantity on a logarithmic scale using 10 as the base.

Since the measure is relative, we have to fix it, if we want to use a decibel scale.
It is convenient to start with 

+ 0 dB as the sound intensity of the threshold of hearing $THO$
+ a whisper is about 15 dB
+ a library 45 dB
+ a normal conversation 60 dB
+ a toilet flushing 75-85 dB
+ a noisy restaurant 90 dB
+ a baby crying 110 dB
+ a jet engine 120 dB
+ a ballon popping 157 dB

If we follow that convention we can compute the decibels of a sound intensity $I$ by

\begin{equation}
    db(I) = 10 \cdot \log_{10}\left( \frac{I}{I_{TOH}} \right),
\end{equation}

where $I_{TOH}$ is the sound intensity of the threshold of hearing.

The measurement is motivated by the perception of loudness of the human ear.
**Increasing the perceived loudness by a factor of 2 equates to rise of +3 dB.**
In other words: every increase of 3 dB represents a doubling of sound intensity or acoustic power.

We can use db instead of amplitude (amp) to control the loudness in **sclang**.
To convert db to amp use ``dbamp`` and ``ampdb`` to do the reverse operation.

```isc
0.dbamp; // equals 1 amp 
1.dbamp; // 1.122018454302
(-3).dbamp; // 0.70794578438414
3.dbamp; // 1.4125375446228
```

For example, the sound generated by

```isc
{SinOsc.ar(400!2) * (-3).dbamp;}.play
```

should be approximately perceived half the level of  

```isc
{SinOsc.ar(400!2)}.play
```

## Loudness

Loudness is a subjective perception of sound intensity.
It depends on the duration and frequency of a sound, the age and other subjective properties of the lister.
We perceive short lasting sounds and sounds with a low frequency less loud than long lasting high frequency sounds.
Therefore, the sound intensity can be the same but the loudness can be very different.
It is measured in phons.

## Timbre

(sec-envelope)=
## Envelopes

(sec-lfo)=
## Low Frequency Oscillator

A low frequency oscillator (LFO) is, as its name suggests, an oscillator that oscillates with a low frequency, that is, a frequency that is below the audible frequency.
LFO's are often used to control some argument of another oscillator, for example, to control its amplitude.

(sec-rm)=
## Ring Modulation

Ring modulation (RM) is often used as a synonym for [amplitude modulation (AM)](sec-am).
Sometimes the term RM is used when the modulator is bipolar (the amplitude becomes positive as well as negative) and AM refers to a unipolar amplitude modulation.
However, I stick to the term [amplitude modulation (AM)](sec-am) to refer to both.