#!/usr/bin/env python
# coding: utf-8

# In[1]:


from music21 import *
from IPython.display import Image as img
from PIL import Image


# (sec-intervals)=
# # Intervals
# 
# >Our brains are wired to pick up the music that we expect, [and] generally music is consonant rather than dissonant, so we expect a nice chord. So when that chord is not quite what we expect, it gives you a little bit of an emotional frisson, because it's strange and unexpected. -- John Sloboda
# 
# If we push multiple piano keys, the color of the sound we perceive will be determined mainly by the relation between those keys, i.e., the generated *intervals*.
# In that regard, compared to the exact pitches, *intervals* are much more important.
# But instead of similarity we consider *consonant* and *dissonant* combinations of [notes](sec-notes) or more preceisly pitches.
# For example, pressing two consequitive piano keys result in vibration, i.e., both strings vibrate with a similar frequency but they cause dissonance!
# 
# Building a beautiful melody revolves around finding a suitable sequence of a set interval of intervals.
# It is a play around *dissonance* and *consonance*, between building up tension and realsing it by coming home to the *tonic* (the first note of a scale).
# Intervals are, in fact, so crucial that musicians give certain intervals specific names and functionalities!
# 
# An interval can be described as *vertical* or **harmonic** if the two notes sound simultaneously.
# If they sound successively we speak of *horizontal*, *linear* or **melodic** intervals.
# These can be *ascending* and *descending*.
# 
# ## Frequency Ratios
# 
# Since I am a computer scientist and not a musician, I will start by looking at the relation of notes using my mathematical perspective first.
# Before we talk about notes, chords, keys and so on, let us focus on the basics: frequencies!
# Let $f_1 > f_2$ be some arbitrary frequencies, then the *ratio*
# 
# \begin{equation*}
#     \frac{f_1}{f_2}
# \end{equation*}
# 
# is the *interval* between $f_1$ and $f_2$.
# We often notate an interval as $f_1$:$f_2$.
# Consequently, an interval is defined as the ratio of two frequencies.
# We can extend this concept to multiple frequencies $f_1, f_2, f_3$ for which we receive three intervals:
# 
# \begin{equation*}
#     \frac{f_1}{f_2}, \frac{f_2}{f_3}, \frac{f_3}{f_1}.
# \end{equation*}
# 
# In general, if we have $n$ distinct frequencies, we get $(n-1)^2$ intervals.
# 
# However, if we consider piano keys things get more complicated since the vibration of a single piano string result air pressure that can be represented by a signal with multiple frequencies.
# This is true for any analog instrument.
# We have to add many harmonics to the fundamental frequency to recreate the sound played by pushing one single piano key.
# Furthermore, the actual pitch is a perceptual property and depends on the listener.
# We generalise and claim that the fundamental frequency, i.e., the frequency of the lowest partial, is the actual pitch of the vibration the listener hears.
# 
# Consequently, in music theory, an *interval* may be loosely defined as the difference between two pitches, i.e., the ratio of two fundamentals.
# Playing two piano keys gives the sound a specific color.
# Relating multiple intervals by, for example, playing two times three different pitches in sequence, gives the resulting sound another quality.
# It may evoke happiness, fear, darkness, melancholy, or tension.
# It may be grounding, i.e., invoke a feeling of homecoming.
# 
# So, why do intervals have a psychological effect on us humans?
# Everything starts with a *natural phenomenon* which has been referred to as *the basic miracle of music*.
# After *unison* (an interval of 1:1), the *octave* (interval of 2:1) is the simplest interval in music.
# An *octave* is the *interval* between one musical pitch and another double its frequency.
# The human's (as well as monkey's, rat's, and infant's) ear tends to hear both frequencies/notes as being essentially the same due to closely related harmonics.
# For this reason, pitches that are an *octave* apart are given the same key name in the *Western system of music notation*.
# We say they belong to the same *pitch class*.
# The number after the letter of a note indicates its octave.
# For example, F4 means F (the key) in octave 4, while C5 means a C in octave 5.
# F4 and F5 are in the same *pitch class* but have different pitches.
# 
# Compare the sound of the following two pattern.
# Which melody sounds more harmonic and why?
# Can you hear the difference?
# 
# ```isc
# (
# var base = 300;
# Pbindef(\melody1,
#     \instrument, \default,
#     // complex ratios
#     \freq, Pseq([base, base*21/17, 
#                  base*37/17, base*11/7,
#                  base*11/17, base*39/17], 6),
#     \dur, 0.2,
#     \legato, 0.1
# ).play;
# )
# ```

# In[2]:


import IPython.display as ipd
audio_path = '../../../sounds/inharmonic-melody.mp3'
ipd.Audio(audio_path)


# ```isc
# (
# var base = 300;
# Pbindef(\melody2,
#     \instrument, \default,
#     // simple ratios
#     \freq, Pseq([base, base*5/3, base*2/3, base*4/3, base/2, base*6/5], 6),
#     \dur, 0.2,
#     \legato, 0.1
# ).play;
# )
# ```

# In[3]:


audio_path = '../../../sounds/harmonic-melody.mp3'
ipd.Audio(audio_path)


# ## Cents
# 
# The *cent* is a logarithmic unit of measurement. 
# As we know, frequency is expressed in a logarithmic scale.
# Along that scale the distance between a given frequency and its double (an *octave*) is divided into 1200 equal parts, each of these parts is one *cent*. 
# In *twelve-tone equal temperament (12-TET)*, a [tuning system](sec-tuning) in which all semitones have the same size, the size of one *semitone* is exactly 100 cents. 
# Hence, in 12-TET the cent can be also defined as one hundredth of a semitone.
# 
# Mathematically, the size in cents of the interval from frequency $f_1$ to frequency $f_2$ is
# 
# $$1200 \cdot \log_2\left( \frac{f_1}{f_2} \right).$$
# 
# Notable, pitch can be perceived in a range which is approximately the same for each person.
# In a range from 10 to 25 *cents*, depending on the listeners hearing and musical education or exposer, pitch differences can be perceived.
# In terms of a center frequency $f$, this gives us an interval defined by
# 
# \begin{equation*}
#     f \cdot \lambda,
# \end{equation*}
# 
# with $\lambda \in [-\epsilon;\epsilon]$ and
# 
# \begin{equation*}
#    \epsilon \in \left[\frac{10}{1200}; \frac{25}{1200} \right] = \left[\frac{1}{120}; \frac{1}{48} \right] \approx \left[0.0083; 0.208 \right].
# \end{equation*}
# 
# Therefore, our perception ability widely outperforms the variants a musician can perform on a piano but it covers most of the consonant options.
# 
# 
# ## Musical Intervals
# 
# In music theory, intervals are the relationship between any **two notes**.
# Therefore, we limit ourselves to a few amount of possible intervals.
# But this limitations results in a good distinction between notes, chords, and scales.
# The name of the interval has two parts.
# First, the **type** of the interval and second the **distance** the two notes are from each other.
# 
# ### Distance
# 
# To determine the distance of an interval on a *staff*, we count the lines and gaps between the two notes including the positions of the notes.
# In the following we have a F4 and C5 on the *staff* and there are two lines and three gaps inbetween them.
# Therefore, the distance is a *fifth*.

# In[4]:


f = chord.Chord(['F4', 'C5'], duration=duration.Duration(4.0))
path = f.write('musicxml.png')
im = Image.open(path)
# (left, top, right, bottom)
im = im.crop((170, 310, 390, 450))
display(im)


# This is true regardless of the [scale](sec-scales) we are using!
# If we are in the key of C major (all white keys on the piano), F4 to C5 are 7 semitones (**perfect**) apart, while G4 to D5 are also 7 semitones apart.
# The staff below shows both (vertical) intervals:

# In[5]:


f1 = chord.Chord(['F4', 'C5'], duration=duration.Duration(4.0))
f2 = chord.Chord(['G4', 'D5'], duration=duration.Duration(4.0))
s = stream.Stream()
s.append(f1)
s.append(f2)
path = s.write('musicxml.png')
im = Image.open(path)
# (left, top, right, bottom)
im = im.crop((170, 310, 500, 450))
display(im)


# On the other hand, a *third* in the majaor scale can be 4 semitones apart (**major**), e.g. C to E or 3 semitones apart (**minor**), e.g. E to G.

# In[6]:


f1 = chord.Chord(['C4', 'E4'], duration=duration.Duration(4.0))
f2 = chord.Chord(['E4', 'G4'], duration=duration.Duration(4.0))
s = stream.Stream()
s.append(f1)
s.append(f2)
path = s.write('musicxml.png')
im = Image.open(path)
# (left, top, right, bottom)
im = im.crop((170, 310, 500, 450))
display(im)


# The distance is also called *diatonic numbering* because the distance correspond to the degrees of the [diatonic scale](sec-diatonic-scale).
# For instance, C-G is a *fifth* because the notes from C to G encompass five letter names (C, D, E, F, G) and it encompass five notes of the diatonic scale, for example, C-Db-Eb-F-G for the *Ab major diatonic scale*.
# 
# Again, note that if we compute the **distance**, we start counting from one.
# Therefore, C4-C4 is counted as one (*unison*), even though there is no difference between the endpoints!
# 
# Adding accidentals to the notes that form an interval does not necessarily change its distance.
# For instance, the interval G-G# (spanning 8 semitones, i.e., a minor sixth) and C#-G (spanning 6 semitones, i.e., a diminished) can be regarded as fifths like the corresponding natural interval C-G (7 semitones).
# 
# ### Quality
# 
# The name of any interval is further qualified using the terms **perfect** (**P**), **major** (**M**), **minor** (**m**), **augmented** (**A**/$+$), and **diminished** (**dim**/$\circ$).
# This is called the *interval quality*.
# 
# In any [major scale](sec-diatonic-scale), the *unison*, *fourth*, *fifth* and *octave* from the *tonic* (of the scale) to the respective other note in the scale are **perfect** and all other intervals are **major**.
# In any [(natural) minor scale](sec-minor-scale) on the other hand, the *unison*, *fourth*, *fifth* and *octave* stay **perfect** but the *third*, *sixth* and *seventh* are **minor**.
# The *second* stays a **major**.
# 
# A **minor** interval is one half step / 1 semitone / 100 cents smaller than a **major** interval.
# And if we make a minor interval even one half step smaller, it becomes **diminished**.
# In the contrary, by making a major one half step larger it becomes **augmented**.
# There is however no minor interval version of a perfect interval.
# Lowering a **perfect** by one half step makes it **diminished**.
# When making it one half step larger, it becomes **augmented**.
# 
# Perfect intervals are consonant.
# By definition, the inversion of a perfect interval is also perfect since 
# 
# $$12 - 7 + 2 = 7.$$
# 
# All other intervals are less consonant.
# The inversion of a minor interval is major and vice versa and the inversion of an augmented invertal is a dimished interval.
# For example, a major third (4 semitones becames)
# 
# $$12-4 + 2 = 10$$
# 
# a minor seventh (10 semitones).
# 
# ### Overview
# 
# The following table lists special names for important intervals.
# As you can see there are many intervals with multiple names depending on the musical context they have been used.
# In the table I list the *just temperament*, i.e., ratios of *rational numbers*.
# For the *equal temperament* the ratios slightly differ; they are irrational.
# For example, $6/5 = 1.2$ becomes $\sqrt[3]{2} \approx 1.1892$.
# 
# | Interval Name                      | Symbol | Multiple                      | (Just) Ratios         | Semitones |
# | ---------------------------------- | ------ | ----------------------------- | --------------------- | --------- |
# | Unison / diminished second         | I      | 1                             | 1:1                   | 0         |
# | Minor second / augmented unison    | ii     | 1.778                         | 16:9                  | 1         |
# | Major second / diminished third    | II     | 1.125                         | 9:8                   | 2         |
# | Minor third / augmented second     | iii    | 1.2                           | 6:5                   | 3         |
# | Major third / diminished fourth    | III    | 1.25                          | 5:4                   | 4         |
# | Perfect fourth / augmented third   | IV     | 1.33                          | 4:3                   | 5         |
# | Diminished fifth / tritone         | ?      | 1.4142                        | 45:32                 | 6         |
# | Perfect fifth / diminished sixth   | V      | 1.5                           | 3:2                   | 7         |
# | Minor sixth / augmented fifth      | vi     | 1.66                          | 5:3                   | 9         |
# | Major sixth / diminished seventh   | VI     | 1.6                           | 8:5                   | 8         |
# | Minor seventh / augmented sixth    | vii    | 1.8                           | 9:5                   | 10        |
# | Major seventh / diminished octave  | VII    | 1.875                         | 15:8                  | 11        |
# | Octave / augmented seventh         |        | 2                             | 2:1                   | 12        |
# 
# *Intervals* can sound pleasingly consonant or dissonant.
# Simple **or** close to simple ratios tend to sound consonant while complicated ratios tend to sound dissonant.
# An *octave* (2:1) sounds perfectly consonant.
# The *perfect fifth* (3:2), the *perfect fourth* (4:3), and the *minor* and *major third* are consonant.
# The *diminished* is dissonant.
# While dissonance is less pleasing, it can create drama, excitement, and tension.
# It is an important property to use in composing music.
# Hermann von Helmholtz categorises the octave, perfect fifth, perfect fourth, major sixth, major third, and minor third as consonant, in decreasing value, and other intervals as dissonant.
# 
# ```{figure} ../../../figs/composing/piano-keys-intervals.png
# ---
# width: 800px
# name: fig-piano-keys-intervals
# ---
# Piano keys: the octave in blue, the perfect fourth in red, and the minor third in green. Note that only the distance between keys, i.e., their relation matters!
# ```
# 
# ## The Devil’s Tritone
# 
# Some regard the *tritone* (aka diminished fifth) as *the devil's interval* because it is highly dissonant and has inspired composers to explore the dark side of music.
# Music listeners' almost instinctive desire to hear a song through to its rhythmic and harmonic conclusion can be an effective (if torturous) tool throughout the fields of music composition and scoring.
# The dissonant intervals of the *devil's tritone* are particularly affecting because of this listener's instinct to find resolution in music and the fact that we are used to getting it.
# Music, in that sense, is a play around expectations and a balance between repetition and surprise;
# The expectancy violation makes us a little upset, and we ask for a resolution.
# Thus music can be violent, it can lure us into desires;
# keeping us thirsty in the desert of silence.
