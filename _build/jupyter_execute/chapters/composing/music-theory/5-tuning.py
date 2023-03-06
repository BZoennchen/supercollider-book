#!/usr/bin/env python
# coding: utf-8

# (sec-tuning)=
# # Tuning System
# 
# Tuning is the process of adjusting the pitch of one or many tones from musical instruments to establish typical intervals between these tones. Tuning is usually based on a fixed reference, such as A = 440 Hz. 
# The term "out of tune" refers to a pitch/tone that is either too high (sharp) or too low (flat) in relation to a given reference pitch.
# 
# A *tuning system* is the system used to define which tones, or pitches, to use when playing music.
# In other words, it is the choice of number and spacing of frequency values used.
# 
# (sec-just-tuning)=
# ## Just Intonation
# 
# TODO
# 
# (sec-p-tuning)=
# ## Pythagorean Tuning
# 
# As mentioned in section [Intervals](sec-intervals) the consonant frequency ratio is 2:1.
# The next most consonant frequency ratio is 3:1 than 4:1 and so on.
# When building a scale we desire the absence of beating when two sounds are played together.
# Since a frequency ratio of 2:1 appears when we play the same note one octave apart, we know that our scale should span no more than twice the frequency of the root frequency.
# 
# Therefore, we use the 3:1 ratio to build our scale.
# Let us start with 440 Hz.
# Using the 3:1 ratio we add one frequency below $440 \cdot 4/3 \approx 586.66$ and one above $440 \cdot 3 / 2 = 660$
# We can repeat this process to create even more frequencies: $586.66 \cdot 2/3 \approx 391.11$ and $660 \cdot 3/4 = 495$.
# 
# Overall we end up with the following notes five.
# 
# | Frequency   | 391.11 | 440.00 | 495.00 | 586.66 | 660.00 | 
# | ----------- | ------ | ------ | ------ | -------| ------ |
# | **Note**    | G      | A      | B      | D      | E      |
# | **Ratio**   | 1:1    | 9:8    | 81:64  | 3:2    | 27:16  |
# 
# 3/2 * 3/4 = 9/16
# 
# Which forms the *petatonic scale* of *G major*.
# The jump from 391.11 to 440 Hz equates to 2 semitones.
# The interval between 391.11 to 495.00 equates to 4 semitones and going from the root to 586.66 spans 7 semitones.
# 391.11 to 660 gives us 9 semitones.
# 
# ```isc
# 440.cpsmidi-391.11.cpsmidi;     //  2.0391492001631
# 495.00.cpsmidi-391.11.cpsmidi;  //  4.0782492174708
# 586.66.cpsmidi-391.11.cpsmidi;  //  7.0194024592495
# 660.00.cpsmidi-391.11.cpsmidi;  //  9.058699208817
# ```
# 
# ```isc
# (
# Pbind(
#   \scale, Scale.majorPentatonic,
#   \degree, Pseq((0..5), 1),
#   \dur, 0.5
# ).play
# )
# ```

# In[1]:


import IPython.display as ipd
audio_path = '../../../sounds/pentatonic-scale.mp3'
ipd.Audio(audio_path)


# From there we can add two more notes by dividing 391.11 by 3/4 and multiplying 495 by 3/2, i.e. $391.11 \cdot 4/3 = 521.48$ and $495 \cdot 3 / 2 = 742.5$ and we end up with the scale of G major.
# 
# ```isc
# 521.48.cpsmidi-391.11.cpsmidi; //  4.9804499913461
# 742.5.cpsmidi-391.11.cpsmidi;  //  11.097799226125
# ```
# 
# | Frequency   | 391.11 | 440.00 | 495.00 | 521.48 | 586.66 | 660.00 | 742.5   |
# | ----------- | ------ | ------ | ------ | ------ | -------| ------ | ------- |
# | **Note**    | G      | A      | B      | C      | D      | E      | F#      |
# | **Ratio**   | 1:1    | 9:8    | 81:64  | 4:3    | 3:2    | 27:16  | 243:128 |
# 
# The technique we just used to build a scale is called *Pythagorean tuning* or *Pythagorean just intonation*.
# It is close to the [12-TET](sec-tet-tuning) but uses whole number ratios.
# Overall it does not offer much advantage for tonal harmony.
# We get all the intervals by consecutively multiplying by $3/2$ (ascending fifth), $2/3$ (descending fifth), or their [inversion](sec-inversion) $4/3$ or $3/4$ respectively.
# The *Pythagorean tuning* involves ratios of very large numbers, corresponding to natural harmonics very high in the harmonic series that do not occur widely in physical phenomena.
# The primary reason for its use is that it is extremely easy to tune, as its building block, the perfect fifth, is the simplest and consequently the most consonant interval after the octave and unison.
# 
# (sec-tet-tuning)=
# ## Equal Temperament
# 
# TODO
# 
# *Pythagoreans* were obsessed with *simple ratios*, i.e., ratios formed by small prime numbers.
# They build a *just-tuning* by using these ratios, which lead to a strong dissonance for some combinations of notes.
# In 1584 *Zhu Zaiyu* achieved an exact calculation of the well-known *twelve-tone equal temperament tuning (12-TET)* in China.
# One year later, the Flemish mathematician *Simon Stevin* was also able to develop this flexible *tuning*.
# Instead of using *simple ratios* *equal temperament tunings*, use real numbers such that an *octave* is divided in equally tempered (equally spaced) on a logarithmic scale.
# In the case of the *twelve-tone*, the ratio is equal to the 12th root of 2, i.e.,
# 
# \begin{equation}
#     \sqrt[12]{2} = 2^{1/12} \approx 1.05946.
# \end{equation}
# 
# In modern times, 12-TET is usually tuned relative to a standard pitch of 440 Hz, called A440.
# Note A is tuned to 440 hertz, and all other notes are defined as some multiple of semitones apart from it, either higher or lower in frequency.
# However, the standard pitch has not always been 440 Hz, and there is still a lot of dispute and discussion.
# This development is a comparatively recent development in the musical community, and the agreement is still fragile among musicians {cite}`loy:2006`.
# 
# Interstingly, if we look at the intervals between harmonics we spot *simple ratios* for 12-TET.
# From the fundamental $\omega$ to the first overtone $2\omega$ we get the ratio $2/1$.
# From the first $2\omega$ to the second overtone $3\omega$ we get another simple ratio, i.e., $3/2$ following the intervals $4/3$, $5/4$ and $6/5$.
# In general the $i$-th interval is equal to 
# 
# \begin{equation}
#     \frac{i+1}{i},
# \end{equation}
# 
# which gives us *simple ratios* for small $i$.
